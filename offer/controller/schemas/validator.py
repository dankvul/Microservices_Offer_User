from jsonschema import validate, ValidationError
from typing import Optional


class SchemaValidator:
    def __init__(self, schema: dict) -> None:
        self.schema = schema

    async def validate_json(self, target_json: dict) -> Optional[str]:
        try:
            validate(instance=target_json, schema=self.schema)
        except ValidationError as e:
            return e.message
        return None
