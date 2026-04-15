#Stage 1: Build Stage 
FROM python:3.14-slim 

WORKDIR /my_app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#Stage 2: Production Stage

COPY . .

EXPOSE 5002

CMD ["python", "my_app.py"]