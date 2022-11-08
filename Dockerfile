FROM python:3.8.10-alpine
RUN mkdir /app
COPY . /app
WORKDIR /app
RUN pip install tk
CMD [ "python", "./welcome_page.py" ]