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

# Collect static files (optional, depending on your project)
RUN python manage.py collectstatic --noinput

# Expose necessary port (for Django development, typically 8000)
EXPOSE 8000

# Default command to run when the container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
