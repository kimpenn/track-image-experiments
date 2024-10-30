FROM python:3.12.5

WORKDIR /app

# set some environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /app/.
RUN pip install --no-cache-dir -r requirements.txt

# copy project
COPY ./main /app/.

EXPOSE 8000

RUN python manage.py migrate

#CMD ["gunicorn", "main.wsgi", "--bind", "0.0.0.0:8000"]
CMD ["gunicorn", "main.wsgi"]
#CMD ["gunicorn", "--config", "gunicorn.conf.py", "main.wsgi"]
