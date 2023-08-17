FROM    python:3.10-alpine3.17
ENV     PYTHONBUFFERED=1
WORKDIR /home
COPY    ./requirements.txt .
COPY    * ./
RUN     pip install -r requirements.txt \
        && adduser --disabled-password --no-create-home doe
USER    doe
EXPOSE  8080
CMD     ["uvicorn", "main:app", "--port", "8080", "--host", "0.0.0.0"]