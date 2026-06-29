import time
import requests

BASE_URL = "http://127.0.0.1:8000"

ALLOWED_DEPARTMENT = "HR Operations"
DENIED_DEPARTMENT = "Payroll"

ALLOWED_HEADERS = {"X-Department": ALLOWED_DEPARTMENT}

MAX_RESPONSE_MS = 2000


def assert_status(response, expected_status, test_name):
    if response.status_code != expected_status:
        raise AssertionError(
            f"{test_name} failed | Expected {expected_status}, "
            f"got {response.status_code} | {response.text}"
        )


def assert_response_time(start_time, max_ms, test_name):
    elapsed_ms = (time.time() - start_time) * 1000
    if elapsed_ms > max_ms:
        raise AssertionError(
            f"{test_name} failed | Response time {elapsed_ms:.2f}ms exceeded {max_ms}ms"
        )


def get_entities_catalog():
    response = requests.get(
        f"{BASE_URL}/api/v1/entities",
        headers=ALLOWED_HEADERS,
    )
    assert_status(response, 200, "Entities catalog discovery")
    data = response.json()

    if isinstance(data, dict) and "entities" in data:
        return data["entities"]

    if isinstance(data, list):
        return data

    raise AssertionError(f"Unexpected entities catalog format: {data}")


def normalize_entity_name(entity):
    if isinstance(entity, str):
        return entity

    for key in ["entity", "name", "source_table", "table", "entity_name"]:
        if key in entity:
            return entity[key]

    raise AssertionError(f"Unable to determine entity name from: {entity}")


def discover_accessible_entities():
    entities = get_entities_catalog()
    accessible = []

    for entity_item in entities:
        entity = normalize_entity_name(entity_item)

        response = requests.get(
            f"{BASE_URL}/api/v1/{entity}?$top=1",
            headers=ALLOWED_HEADERS,
        )

        if response.status_code == 200:
            accessible.append(entity)

    if not accessible:
        raise AssertionError(
            f"No accessible entities found for department: {ALLOWED_DEPARTMENT}"
        )

    return accessible


def discover_denied_case(accessible_entities):
    entities = get_entities_catalog()

    for entity_item in entities:
        entity = normalize_entity_name(entity_item)

        if entity in accessible_entities:
            continue

        response = requests.get(
            f"{BASE_URL}/api/v1/{entity}?$top=1",
            headers={"X-Department": DENIED_DEPARTMENT},
        )

        if response.status_code == 403:
            return entity

    fallback_cases = [
        ("applications", "Payroll"),
        ("payroll_results", "Talent Acquisition"),
        ("benefit_enrollments", "Talent Acquisition"),
    ]

    for entity, department in fallback_cases:
        response = requests.get(
            f"{BASE_URL}/api/v1/{entity}?$top=1",
            headers={"X-Department": department},
        )

        if response.status_code == 403:
            return entity, department

    raise AssertionError("No valid denied RBAC case found.")


def test_health():
    start = time.time()
    response = requests.get(f"{BASE_URL}/")
    assert_status(response, 200, "Health check")
    assert_response_time(start, 1000, "Health check")


def test_metadata():
    start = time.time()
    response = requests.get(f"{BASE_URL}/api/v1/$metadata", headers=ALLOWED_HEADERS)
    assert_status(response, 200, "Metadata endpoint")
    assert_response_time(start, 1500, "Metadata endpoint")


def test_entities_catalog():
    start = time.time()
    entities = get_entities_catalog()

    if not entities:
        raise AssertionError("Entities catalog is empty.")

    assert_response_time(start, 1500, "Entities catalog")


def test_entity_allowed_access(accessible_entities):
    for entity in accessible_entities:
        start = time.time()
        response = requests.get(
            f"{BASE_URL}/api/v1/{entity}?$top=1",
            headers=ALLOWED_HEADERS,
        )

        assert_status(response, 200, f"Allowed RBAC access for {entity}")
        assert_response_time(
            start, MAX_RESPONSE_MS, f"Allowed RBAC access for {entity}"
        )


def test_entity_denied_access(accessible_entities):
    denied_case = discover_denied_case(accessible_entities)

    if isinstance(denied_case, tuple):
        entity, department = denied_case
    else:
        entity = denied_case
        department = DENIED_DEPARTMENT

    response = requests.get(
        f"{BASE_URL}/api/v1/{entity}?$top=1",
        headers={"X-Department": department},
    )

    if response.status_code != 403:
        raise AssertionError(
            f"Denied RBAC access for {entity} failed | "
            f"Department: {department} | Expected 403, got {response.status_code} | "
            f"{response.text}"
        )


def test_missing_department_header(accessible_entities):
    for entity in accessible_entities:
        response = requests.get(f"{BASE_URL}/api/v1/{entity}?$top=1")

        if response.status_code not in [401, 403]:
            raise AssertionError(
                f"Missing header test for {entity} failed | "
                f"Expected 401/403, got {response.status_code} | {response.text}"
            )


def test_odata_select(accessible_entities):
    entity = accessible_entities[0]

    response = requests.get(
        f"{BASE_URL}/api/v1/{entity}?$top=1",
        headers=ALLOWED_HEADERS,
    )
    assert_status(response, 200, f"OData base check for {entity}")

    data = response.json()

    if isinstance(data, dict) and "value" in data and data["value"]:
        first_record = data["value"][0]
    elif isinstance(data, list) and data:
        first_record = data[0]
    else:
        return

    first_column = list(first_record.keys())[0]

    response = requests.get(
        f"{BASE_URL}/api/v1/{entity}?$select={first_column}&$top=1",
        headers=ALLOWED_HEADERS,
    )

    assert_status(response, 200, f"OData $select for {entity}")


def test_odata_top_count(accessible_entities):
    entity = accessible_entities[0]

    response = requests.get(
        f"{BASE_URL}/api/v1/{entity}?$top=5&$count=true",
        headers=ALLOWED_HEADERS,
    )

    assert_status(response, 200, f"OData $top and $count for {entity}")


def run_all():
    print("Global HR Intelligence API - Metadata-Driven Smoke Test Suite")
    print("=" * 70)

    accessible_entities = discover_accessible_entities()

    print(
        f"Discovered {len(accessible_entities)} accessible entities "
        f"for department: {ALLOWED_DEPARTMENT}"
    )

    tests = [
        ("test_health", lambda: test_health()),
        ("test_metadata", lambda: test_metadata()),
        ("test_entities_catalog", lambda: test_entities_catalog()),
        (
            "test_entity_allowed_access",
            lambda: test_entity_allowed_access(accessible_entities),
        ),
        (
            "test_entity_denied_access",
            lambda: test_entity_denied_access(accessible_entities),
        ),
        (
            "test_missing_department_header",
            lambda: test_missing_department_header(accessible_entities),
        ),
        ("test_odata_select", lambda: test_odata_select(accessible_entities)),
        ("test_odata_top_count", lambda: test_odata_top_count(accessible_entities)),
    ]

    passed = 0

    for test_name, test_func in tests:
        test_func()
        print(f"PASS | {test_name}")
        passed += 1

    print("=" * 70)
    print(f"Smoke tests completed successfully: {passed}/{len(tests)}")


if __name__ == "__main__":
    run_all()
