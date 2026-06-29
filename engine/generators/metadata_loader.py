import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[2]
METADATA_DIR = BASE_DIR / "metadata"


class MetadataLoader:
    def __init__(self):
        self.api_catalog = self._load_json("global_hr_api_catalog.json")
        self.dataverse_model = self._load_json(
            "global_hr_dataverse_metadata_model.json"
        )
        self.data_product_contract = self._load_json(
            "global_hr_data_product_contract.json"
        )

    def _load_json(self, file_name: str):
        file_path = METADATA_DIR / file_name

        if not file_path.exists():
            raise FileNotFoundError(f"Metadata file not found: {file_path}")

        with file_path.open("r", encoding="utf-8") as file:
            return json.load(file)

    def get_api_resource(self, source_table: str):
        resources = self.api_catalog.get("resources", [])

        for resource in resources:
            if resource.get("source_table") == source_table:
                return resource

        raise ValueError(f"API resource not found for source_table: {source_table}")

    def get_dataverse_entity(self, source_table: str):
        entities = self.dataverse_model.get("entities", [])

        for entity in entities:
            if entity.get("source_table") == source_table:
                return entity

        raise ValueError(f"Dataverse entity not found for source_table: {source_table}")

    def get_data_product_by_domain(self, domain: str):
        data_products = self.data_product_contract.get("data_products", [])

        for product in data_products:
            if product.get("domain") == domain:
                return product

        return None

    def normalize_primary_key(self, api_resource: dict, dataverse_entity: dict):
        dataverse_pk = dataverse_entity.get("primary_key_source_column")
        if dataverse_pk:
            return dataverse_pk

        api_pk = api_resource.get("primary_key")

        if isinstance(api_pk, dict):
            return (
                api_pk.get("source_column")
                or api_pk.get("name")
                or api_pk.get("column")
                or api_pk.get("logical_name")
            )

        return api_pk

    def build_entity_definition(self, source_table: str):
        api_resource = self.get_api_resource(source_table)
        dataverse_entity = self.get_dataverse_entity(source_table)
        data_product = self.get_data_product_by_domain(
            api_resource.get("domain") or dataverse_entity.get("domain")
        )

        csv_file = dataverse_entity.get("csv_file") or api_resource.get("csv_file")
        primary_key = self.normalize_primary_key(api_resource, dataverse_entity)

        if not csv_file:
            raise ValueError(
                f"CSV file could not be resolved for source_table: {source_table}"
            )

        if not primary_key:
            raise ValueError(
                f"Primary key could not be resolved for source_table: {source_table}"
            )

        return {
            "source_table": source_table,
            "domain": api_resource.get("domain") or dataverse_entity.get("domain"),
            "owner_team": api_resource.get("owner_team")
            or dataverse_entity.get("owner_team"),
            "classification": api_resource.get("classification"),
            "csv_file": csv_file,
            "primary_key": primary_key,
            "dataverse_entity": (
                dataverse_entity.get("logical_name")
                or dataverse_entity.get("dataverse_entity_logical_name")
                or api_resource.get("dataverse_entity_set")
            ),
            "base_path": api_resource.get("base_path"),
            "attributes": dataverse_entity.get("attributes", []),
            "filters": api_resource.get("supported_methods", {})
            .get("GET_collection", {})
            .get("recommended_filters", []),
            "default_select": api_resource.get("supported_methods", {})
            .get("GET_collection", {})
            .get("default_select", []),
            "allowed_departments": (
                api_resource.get("security", {}).get("allowed_departments")
                or dataverse_entity.get("allowed_departments", [])
            ),
            "data_product_id": (
                api_resource.get("data_product_id")
                or data_product.get("data_product_id")
                if data_product
                else None
            ),
            "data_product_name": (
                data_product.get("name") if data_product else source_table
            ),
        }


if __name__ == "__main__":
    loader = MetadataLoader()

    for source_table in ["applications", "workers", "candidates"]:
        entity = loader.build_entity_definition(source_table)

        print("-" * 60)
        print(f"Source table: {entity['source_table']}")
        print(f"Domain: {entity['domain']}")
        print(f"CSV file: {entity['csv_file']}")
        print(f"Primary key: {entity['primary_key']}")
        print(f"Dataverse entity: {entity['dataverse_entity']}")
        print(f"Attributes: {len(entity['attributes'])}")
