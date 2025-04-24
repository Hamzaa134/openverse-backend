# Start from a Python base image
FROM python:3.13-alpine

# Set the working directory in the container
WORKDIR /app

# Copy only the necessary files (requirements and manage.py)
COPY backend/manage.py /app/manage.py
COPY requirements.txt /app/

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the backend application
COPY backend/ /app/

# Optional: collect static files if you're using Django's static files
RUN python manage.py collectstatic --noinput || true

# Expose necessary port
EXPOSE 8000

# Default command: run migrations and then start the server
CMD sh -c "python manage.py migrate --noinput && python manage.py runserver 0.0.0.0:8000"
