FROM python:3.9-alpine

ENV TZ=Asia/Ho_Chi_Minh

WORKDIR /app



RUN apk update \
    && apk add gcc

# install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


# copy project
COPY . .

EXPOSE 8000
CMD ["manage.py", "runserver",  "0.0.0.0:8000"]
ENTRYPOINT ["python"]