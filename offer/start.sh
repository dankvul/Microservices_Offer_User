uvicorn main:app --host 0.0.0.0 --port 8001 --loop 'uvloop' --lifespan on --reload --proxy-headers --reload-dir /app
