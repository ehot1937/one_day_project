FROM python:3.10

ENV APP_HOME="/user/service"
ENV PYTHONPATH=${APP_HOME}
RUN mkdir -p ${APP_HOME}
WORKDIR ${APP_HOME}

COPY . ${APP_HOME}

RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    rm -rf /root/.cache/pip

EXPOSE 8000

