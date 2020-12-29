__all__ = ["add_user_schema"]

base_schema = {
    "title": "user schema",
    "type": "object",
}

add_user_schema = {
    **base_schema,
    "properties": {
        "user_id": {"type": "number"},
        "username": {"type": "string"},
        "secret": {"type": "string"},
    },
    "required": ["user_id", "username", "secret"]
}

