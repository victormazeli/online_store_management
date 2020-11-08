FROM python:3.8-alpine

# create work directory
WORKDIR /usr/src/app

# create the app user
RUN addgroup -S zeusgroup && adduser -S zeus -G zeusgroup

#install dependencies
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev gcc python3-dev musl-dev \
    && apk del build-deps \
    && apk --no-cache add musl-dev linux-headers g++

COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# create neccesary directories
RUN mkdir -p /usr/src/app/static
RUN mkdir -p /usr/src/app/media


#copy project 
COPY . .

#chow users to group
RUN chown -R zeus:zeusgroup /usr/src/app

USER zeus

# CMD ["python", "/usr/src/app/manage.py runserver"]