FROM    python:3.11-slim
ENV     PYTHONBUFFERED=1
WORKDIR /social-app
COPY    . .
RUN     pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD     ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]