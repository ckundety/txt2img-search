# Use an official Python runtime as the base image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Install required packages from requirements.txt
COPY requirements.txt /app/
COPY *.py /app/
RUN pip install --no-cache-dir -r requirements.txt

# ... (other Dockerfile instructions)

# Run your Streamlit app
CMD ["streamlit", "run", "app.py"]
