FROM python:3.11-slim

WORKDIR /opt

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY ./app ./app

# ⏳ Temporary simple solution: wait 5 seconds to allow the DB service to start before launching the app.
# 🔧 For production, replace this with a proper health check or a wait-for-db script (e.g. wait-for-it.sh or pg_isready).
CMD ["sh", "-c", "sleep 5 && uvicorn app.main:app --host 0.0.0.0 --port 8000"]
