FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py model.joblib /app/
EXPOSE 5000
CMD ["python", "app.py"]
