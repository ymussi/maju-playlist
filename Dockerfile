FROM python:3.6
LABEL fileversion=v0.1

ARG RUN_ENVIRONMENT
ENV DBENV=${RUN_ENVIRONMENT}
ENV PYTHONUNBUFFERED=0
ENV FLASK_ENV=${RUN_ENVIRONMENT}
ENV ENV=${RUN_ENVIRONMENT}
ENV DBENV=${RUN_ENVIRONMENT}
ENV TZ=America/Sao_Paulo

WORKDIR /app/maju/

COPY . .

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN pip install -r requirements.txt && \
    python setup.py develop

RUN wget -O /bin/wait-for-it https://github.com/vishnubob/wait-for-it/raw/54d1f0bfeb6557adf8a3204455389d0901652242/wait-for-it.sh; \
    chmod +x /bin/wait-for-it

ENTRYPOINT ["/bin/sh","/app/maju/entrypoint.sh"]