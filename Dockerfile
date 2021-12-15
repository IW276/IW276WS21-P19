FROM python:3.6-bullseye as builder

RUN apt-get update \
    && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
    pkg-config \
    tesseract-ocr \
    tesseract-ocr-deu \
    libtesseract-dev \
    libleptonica-dev

RUN pip install poetry

WORKDIR /usr/src/app
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-dev

COPY etc etc
RUN poetry run python etc/preload-models.py

COPY . .
RUN poetry build

FROM nvcr.io/nvidia/l4t-pytorch:r32.5.0-pth1.7-py3

RUN apt-get update \
    && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
    pkg-config \
    tesseract-ocr \
    tesseract-ocr-deu \
    libtesseract-dev \
    libleptonica-dev

COPY --from=builder /root/stanza_resources /root/stanza_resources

COPY --from=builder /usr/src/app/dist/*.whl /tmp
RUN pip3 install /tmp/*.whl

ENV PYTHONIOENCODING=utf-8
ENTRYPOINT ["oae"]
CMD ["--skip-download-models", "/data"]
