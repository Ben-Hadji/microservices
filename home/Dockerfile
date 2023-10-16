# 
FROM python:3.9
# 
WORKDIR /code
# 
COPY . /code/home
# 
COPY requirements.txt /code/home/requirements.txt
# 
RUN pip install --no-cache-dir --upgrade -r /code/home/requirements.txt
#
Expose 80
# 
#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
CMD ["python", "home/app.py"]