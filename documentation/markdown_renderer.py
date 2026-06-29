def build_markdown_table(headers: list[str], rows: list[list[str]]) -> str:
    if not headers:
        return ""

    output = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]

    for row in rows:
        safe_row = [str(value or "") for value in row]
        output.append("| " + " | ".join(safe_row) + " |")

    return "\n".join(output)


def build_features_list() -> str:
    features = [
        "FastAPI-based REST API",
        "Metadata-driven model and router generation",
        "Auto-discovery of generated routers",
        "OData-style query options: `$select`, `$filter`, `$orderby`, `$top`, `$skip`, `$count`",
        "Metadata API endpoints",
        "Department-based RBAC using `X-Department`",
        "OpenAPI governance extensions",
        "Metadata-driven smoke test suite",
        "Documentation Engine powered by metadata",
    ]

    return "\n".join(f"- {feature}" for feature in features)


def build_architecture_diagram() -> str:
    return """```mermaid
flowchart TD
    A[Metadata JSON] --> B[Metadata Loader]
    B --> C[Model Generator]
    B --> D[Router Generator]
    C --> E[Pydantic Models]
    D --> F[Generated Routers]
    F --> G[Router Registry]
    G --> H[FastAPI App]
    H --> I[OpenAPI / Swagger]
    H --> J[Metadata-Driven Smoke Tests]
    H --> K[Documentation Engine]
```"""


def build_rbac_diagram() -> str:
    return """```mermaid
flowchart TD
    A[API Request] --> B[X-Department Header]
    B --> C[Security Service]
    C --> D[Department Access Catalog]
    D --> E{Allowed?}
    E -->|Yes| F[Return Data]
    E -->|No| G[403 Forbidden]
```"""


def build_odata_diagram() -> str:
    return """```mermaid
flowchart TD
    A[Request Query Params] --> B[OData Parser]
    B --> C[$filter]
    C --> D[$select]
    D --> E[$orderby]
    E --> F[$top / $skip]
    F --> G[$count]
    G --> H[JSON Response]
```"""
