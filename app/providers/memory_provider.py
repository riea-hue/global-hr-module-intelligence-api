from app.providers.base_provider import BaseProvider


class MemoryProvider(BaseProvider):
    def __init__(self):

        self.data = {
            "workers": [
                {
                    "worker_id": "W0001",
                    "employee_id": "100001",
                    "first_name": "Pablo",
                    "last_name": "Martinez",
                    "worker_status": "Active",
                },
                {
                    "worker_id": "W0002",
                    "employee_id": "100002",
                    "first_name": "Ana",
                    "last_name": "Lopez",
                    "worker_status": "Active",
                },
            ]
        }

    def get_all(self, entity_name: str):

        return self.data.get(entity_name, [])

    def get_by_id(self, entity_name: str, entity_id: str):

        rows = self.get_all(entity_name)

        for row in rows:
            if row.get("worker_id") == entity_id:
                return row

        return None
