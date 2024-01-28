FROM tiangolo/meinheld-gunicorn-flask:python3.9
RUN pip install --upgrade setuptools
ENV STATIC_URL /static
ENV STATIC_PATH /app/static

# Set the working directory in the Docker image
WORKDIR /app
COPY . /app/.
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt
