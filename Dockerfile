ARG PYTHON_VERSION=3.11-slim-bullseye

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /code

WORKDIR /code

COPY requirements.txt /tmp/requirements.txt

RUN set -ex && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /root/.cache/

COPY her_tech_collective /code

ENV SECRET_KEY "HS9WvV3AOPFHt4sQgPj4DKVhAMHHe2Wb7g4csBUN33xET6d4EC"

RUN python manage.py collectstatic --noinput
RUN chmod +x /code/run.sh

EXPOSE 8000

# CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "her_tech_collective.wsgi"]
CMD ["/code/run.sh"]
