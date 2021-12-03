FROM python:3.6-bullseye as builder

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends tesseract-ocr libtesseract-dev libleptonica-dev pkg-config
RUN pip install poetry

WORKDIR /usr/src/app
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-dev

COPY . .
RUN poetry build

FROM nvcr.io/nvidia/l4t-pytorch:r32.5.0-pth1.7-py3

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends tesseract-ocr libtesseract-dev libleptonica-dev pkg-config

COPY --from=builder /usr/src/app/dist/*.whl /tmp
RUN pip3 install /tmp/*.whl

ENV PYTHONIOENCODING=utf-8
CMD ["oae", "/data"]
