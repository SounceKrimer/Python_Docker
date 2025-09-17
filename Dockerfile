FROM python:3.10.0-slim
WORKDIR /Hluschenko_Vlad
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt || true
COPY Lab2_Hluschenko.py .
CMD ["python", "Lab2_Hluschenko.py"]