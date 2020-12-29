__all__ = ["signup_schema", "login_schema"]

base_schema = {
    "title": "user schema",
    "type": "object",
}

signup_schema = {
    **base_schema,
    "properties": {
        "username": {"type": "string"},
        "email": {"type": "string"},
        "password": {"type": "string"},
    },
    "required": ["username", "email", "password"]
}

login_schema = {
    **base_schema,
    "properties": {
        "username": {"type": "string"},
        "password": {"type": "string"},
    },
    "required": ["username", "password"]
}
