# Use a standard Python image as the base
FROM python:3.11-slim

# Install system dependencies (libpq-dev for PostgreSQL)
RUN apt-get update && apt-get install -y \
    postgresql-client \
    libpq-dev \
    gcc \
    # Clean up afterwards to keep the image small
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /usr/src/app

# Copy the requirements file and install Python dependencies
# This leverages Docker's layer caching
COPY requirements.txt .

# Your combined pip install command, now that OS dependencies are installed
RUN pip install -r requirements.txt --extra-index-url https://download.pytorch.org/whl/cpu

# Copy the rest of your application code
COPY . .

# Set environment variable (important for gunicorn/Django)
ENV PYTHONUNBUFFERED 1
ENV PORT 10000

# Specify the command to run the web service (gunicorn)
CMD ["gunicorn", "got_no_beans.wsgi"]