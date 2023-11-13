FROM python:3.9
WORKDIR /project
#this is the working directory in the container.


COPY ./requirements.txt /project/requirements.txt
#copy all the code and files from this container to the container.
RUN pip install -r /project/requirements.txt
#install all requirements.
COPY ./app /project/app

EXPOSE 8000

CMD ["uvicorn", "main:app", "--reload"]

