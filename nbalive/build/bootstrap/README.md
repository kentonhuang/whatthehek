## Bootstrap Directory

This directory contains the scripts that are executed when a container is deployed. In this example, these files are `bash` scripts split up based on environment.

## Reasoning

Docker images are usually designed to execute a command which kicks off a long standing process for the lifecycle of a container. When the process is terminated, so is the container. In these bootstrap scripts, a command is given to start the `Django` server on port `8000` and run it as long as needed.
