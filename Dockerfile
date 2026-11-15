FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY frontend ./frontend
COPY backend ./backend
COPY data ./data
COPY docs ./docs
COPY notes ./notes
COPY cloudflare ./cloudflare
COPY run.py prepare_data.py MANIFEST.json README_*.md PAPERS_NOT_INCLUDED.json PACKAGE_TRANSFORMATIONS.json EXTERNAL_DEPENDENCIES.json start_windows.cmd ./
RUN python prepare_data.py && useradd --uid 10001 --create-home flame && chown -R flame:flame /app
USER flame
ENV PORT=8080 PYTHONUNBUFFERED=1
EXPOSE 8080
CMD ["python", "cloudflare/container_server.py"]
