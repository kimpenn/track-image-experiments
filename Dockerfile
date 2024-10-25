FROM python:3.12.5

# set some environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY ./main .

EXPOSE 8000
CMD ["gunicorn", "main.wsgi:application", "--bind", "0.0.0.0:8000"]