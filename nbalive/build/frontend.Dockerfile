FROM node:11.5.0

# Read argument passed in from docker compose
ARG REACT_ENV

# Create application directory
RUN mkdir /app
WORKDIR /app

# Install dependencies
COPY ./frontend/package*.json ./
RUN npm install

# Setup codebase
ADD ./frontend ./

# Configure port
EXPOSE 3000

# Add scripts for handling entry
ADD ./build/bootstrap/frontend/${REACT_ENV}_entrypoint.sh ./entrypoint.sh

# Configure command
CMD bash ./entrypoint.sh
