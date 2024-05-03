FROM python:3.10-slim
WORKDIR /app
COPY req.txt .
RUN pip install --no-cache-dir -r req.txt
COPY shop_app /app/shop_app
COPY static /app
COPY sql_app.db /app
CMD ["uvicorn", "shop_app.main:app", "--host", "0.0.0.0", "--port", "8000"]