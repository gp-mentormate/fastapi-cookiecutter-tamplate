FROM python:3.11-alpine

# set workdir
WORKDIR /var/www/app

# enable python logging
ENV PYTHONUNBUFFERED 1
ENV LANG en_US.utf8

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements/* ./

ARG ENV
RUN if [ "$ENV" = "dev" ]; then \
	pip install --no-cache-dir -r development.txt; \
    else \
	pip install --no-cache-dir -r production.txt; \
    fi

COPY . .
# expose 8000 and start the guvicorn server
EXPOSE 8000
ENTRYPOINT ["./start.sh"]
