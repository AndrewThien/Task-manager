FROM pypy:latest
WORKDIR /app
COPY . /app
CMD python task_manager_updated.py