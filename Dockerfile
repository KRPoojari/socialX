FROM python:3.10.2-slim-buster as base
FROM base as builder
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        build-essential
RUN pip install --upgrade pip
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN pip install --no-cache-dir "uvicorn[standard]" 
ADD ./requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt



FROM base
COPY --from=builder /opt/venv /opt/venv
COPY . ./app/
WORKDIR /app/
ENV PYTHONPATH="${PYTHONPATH}:/app"
ENV PATH=/opt/venv/bin/:$PATH

CMD ["./start.sh"]
