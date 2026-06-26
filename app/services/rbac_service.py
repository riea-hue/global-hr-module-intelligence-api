import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[2]
METADATA_DIR = BASE_DIR / "metadata"


class RBACService:
    def __init__(self):
        self.access_catalog = self._load_json("department_access_catalog.json")

    def _load_json(self, file_name: str) -> dict:
        file_path = METADATA_DIR / file_name

        if not file_path.exists():
            raise FileNotFoundError(f"Metadata file not found: {file_path}")

        with file_path.open("r", encoding="utf-8") as file:
            return json.load(file)

    def get_department_profile(self, department: str) -> dict | None:
        departments = self.access_catalog.get("departments", [])

        for profile in departments:
            if profile.get("department", "").lower() == department.lower():
                return profile

        return None

    def can_access_csv(self, department: str, csv_file: str) -> bool:
        profile = self.get_department_profile(department)

        if not profile:
            return False

        allowed_files = profile.get("csv_files", [])
        return "*" in allowed_files or csv_file in allowed_files

    def get_access_context(self, department: str) -> dict:
        profile = self.get_department_profile(department)

        if not profile:
            return {
                "department": department,
                "authorized": False,
                "reason": "Department profile not found.",
            }

        return {
            "department": profile.get("department"),
            "authorized": True,
            "access_level": profile.get("access_level"),
            "domains": profile.get("domains", []),
            "csv_files": profile.get("csv_files", []),
        }