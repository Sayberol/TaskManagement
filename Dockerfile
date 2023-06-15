FROM python:3.10-alpine

WORKDIR /app

# Install system dependencies
RUN apk update && apk add --no-cache build-base libffi-dev openssl-dev

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY ./todolist /app

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]