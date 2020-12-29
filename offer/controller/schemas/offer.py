__all__ = ["create_offer_schema", "get_offer_schema"]

base_schema = {
    "title": "offer schema",
    "type": "object",
}

create_offer_schema = {
    **base_schema,
    "properties": {
        "user_id": {"type": "number"},
        "title": {"type": "string"},
        "text": {"type": "string"},
    },
    "required": ["user_id", "title", "text"]
}

get_offer_schema = {
    **base_schema,
    "properties": {
        "user_id": {"type": "number"},
        "offer_id": {"type": "number"},
    },
}
