# Dockerfile for React Frontend

# Use Node.js official image as a parent image
FROM node:16

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and package-lock.json files
COPY package.json package-lock.json ./

# Install any needed packages specified in package.json
RUN npm install

# Copy the rest of the frontend code
COPY . .

# Expose the port React will run on
EXPOSE 3000

# Command to run the app
CMD ["npm", "start"]