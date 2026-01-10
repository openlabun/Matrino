# In order to be sure that we always have a functional version, we pin 
# the sage version instead of using 'latest'
FROM --platform=linux/amd64 sagemath/sagemath:10.8

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /api

COPY requirements.txt .

RUN sage --pip install -r requirements.txt

COPY . .

USER root
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

ENV PORT=3000

EXPOSE ${PORT}

# Critical! We run as non-root user for security
USER sage

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:3000/health || exit 1

CMD ["sage", "-python", "-m", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "3000"]
