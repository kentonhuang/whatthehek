## Envs Directory

Contains all the environment variables that will be injected into the created Docker images. These are separated by environment.

`development.env` - Environment variables for Development environment.

`staging.env` - Environment variables for Staging environment.

`production.env` - Environment variables for Production environment.

## Reasoning

Each one of the `.env` files contain the environment variable `DJANGO_SETTINGS_MODULE`. This tells Django which setting module to load on bootstrap. There is an extra `DJANGO_KEY` variable in `production.env` as the production environment should be deployed with a unique key. This key is usually kept off of version control for security purposes.