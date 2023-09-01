#!/bin/bash
# pip install greenlet --only-binary :all:
pip install --no-cache-dir -r /app/requirements.txt

exec uvicorn main:app --host 0.0.0.0 --port 8002