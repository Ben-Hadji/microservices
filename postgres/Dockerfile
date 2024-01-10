FROM postgres:latest

# Install Python and pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Install psycopg2-binary
RUN pip3 install psycopg2-binary

# Set environment variables
ENV POSTGRES_DB=ben_flask
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=Benhadji99

# Copy the Python script into the Docker image
COPY ./init_db.py /init_db.py

# Run the Python script after the container starts
CMD ["postgres", "-c", "shared_preload_libraries='auto_explain'", "-c", "auto_explain.log_min_duration=0", "-c", "auto_explain.log_analyze=1", "&", "python3", "/init_db.py"]

EXPOSE 5432