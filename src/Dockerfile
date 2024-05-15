FROM python:3.11-slim

RUN apt-get update && apt-get install -y ncat
WORKDIR /code
COPY . /code/

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install poetry==1.6.1

RUN poetry config virtualenvs.create false

RUN poetry install --no-interaction --no-ansi -vvv

ENV PYTHONUNBUFFERED 1
ENV PORT 8000
ENV PYTHONPATH "${PYTHONPATH}:/code"
ENV CONF_PATH "/code/config/config_prod.yaml"

EXPOSE $PORT

COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
