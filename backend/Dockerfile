# Use Python 3.11 image as a parent image
FROM python:3.11.9-slim

# Set the working directory in the container
WORKDIR /app

# Install any needed packages specified in requirements.txt
COPY requirements.txt . 

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . . 

# Set the environment variable for Flask
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

# Expose the port Flask will run on
EXPOSE 5000

# Command to run the application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
