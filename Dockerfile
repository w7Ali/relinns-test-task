FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install --upgrade langchain langchain-huggingface
COPY . .
ENV PYTHONUNBUFFERED=1
CMD ["python", "main.py"]
