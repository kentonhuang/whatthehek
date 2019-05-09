## Docker Compose with Django example

This project gives an example of how to set up Django with multiple configuration files and deploy it via Docker containers using Docker Compose.

The Git commits are organized in a way to isolate each step to gain visibility on what's being done.

## Requirements

- Docker w/ Docker Compose
- Pipenv is needed in order to be able to install package dependencies.

## Getting Started

1. Install Pipenv if not available already:

    ```pip install pipenv```

2. Install all required packages:

    ```pipenv install```

To start Django server locally:

  1. First get into the pipenv virtual environment:

      ```pipenv shell```

  2. Start Django:

      ```python manage.py runserver```

To build images and deploy containers:

  `development` can be replaced with either `staging` or `production` in the following examples.

  1. Build images:
  
      ```docker-compose -f compose/development.yml build```

  2. Deploy containers:
  
      ```docker-compose -f compose/development.yml up -d```

  3. Verify containers are running:

      ```docker ps```

## Author's Notes

This is a learning process for me as well. If there is anything that is lacking or unclear please let me know and I will address them.