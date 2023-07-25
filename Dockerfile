FROM python:3.8
LABEL maintainer="Muktadiur Rahman"
WORKDIR /app
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
