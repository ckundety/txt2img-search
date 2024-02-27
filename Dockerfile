FROM python:3.10

WORKDIR /app

COPY requirements.txt /app/
COPY *.py /app/
RUN pip install --no-cache-dir -r requirements.txt

CMD ["streamlit", "run", "app.py"]
