FROM python:3.12-alpine
WORKDIR /app
COPY app.py /app/app.py
ENV PORT=8000
RUN addgroup -S app && adduser -S app -G app
USER app
EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/healthz', timeout=3).read()"
CMD ["python", "app.py"]
