FROM ghcr.io/deephaven/server:0.13.0

COPY app.d /app.d
COPY secrets/google-key.json /google-key.json
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
