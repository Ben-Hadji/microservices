# 
FROM python:3.9

# 
WORKDIR /code

# 
COPY . /code/redis

# 
COPY requirements.txt /code/redis/requirements.txt


# 
RUN pip install --no-cache-dir --upgrade -r /code/redis/requirements.txt

#
Expose 80


# 

#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
CMD ["python", "home/app.py"]