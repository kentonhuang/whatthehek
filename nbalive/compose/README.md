## Compose Directory

This directory contains all files used by docker-compose.

`development.yml` - Development environment Dockerfile.

`staging.yml` - Staging environment Dockerfile.

`production.yml` - Production environment Dockerfile.

`envs` - Directory that contains all the environment variables that will be injected into the containers.

## Reasoning

Two images are created in each one of these YAML files: `db` and `app`. The `db` image defaults to Postgres but can be changed to any desired database server. The `app` image contains the Django application and all dependencies.

In the `development.yml` file, both containers are specified to be deployed with ports ports exposed-- `5432` for `db` and `8000` for `app`. This allows debugging through the host machine.