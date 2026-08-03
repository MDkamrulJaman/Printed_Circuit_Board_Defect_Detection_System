FROM python:3.10-slim

# 1. Environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8000

# 2. Set working directory
WORKDIR /app

# 3. Install system dependencies (OpenCV/GUI dependencies)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    && rm -rf /var/lib/apt/lists/*

# 4. Copy requirements file (FIXED: matching filename)
COPY requirements-docker.txt .

# 5. Upgrade build tools and install dependencies (FIXED: installing matching requirements-docker.txt)
RUN python -m pip install --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r requirements-docker.txt

# 6. Copy application code
COPY api ./api
COPY runs ./runs

# 7. Expose app port
EXPOSE 8000

# 8. Start Uvicorn app (FIXED: uses shell execution to allow $PORT binding)
CMD sh -c "uvicorn api.main:app --host 0.0.0.0 --port ${PORT}"