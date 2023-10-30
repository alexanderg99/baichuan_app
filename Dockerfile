FROM python:3.9
WORKDIR /project
#this is the working directory in the container.


COPY ./requirements.txt /project/requirements.txt
#copy all the code and files from this container to the container.
RUN pip install --no-cache-dir -r /project/requirements.txt
#install all requirements.
COPY ./app /project/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

