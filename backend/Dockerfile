FROM osgeo/gdal:ubuntu-small-3.2.0
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY . /code/

RUN apt-get update && apt-get install -y \
    python3-pip

RUN pip install -U pip
RUN pip install -r requirements.txt

RUN apt-get -y --no-install-recommends install libsqlite3-dev libsqlite3-mod-spatialite

RUN apt-get -y --no-install-recommends install libgdal-dev gdal-bin

