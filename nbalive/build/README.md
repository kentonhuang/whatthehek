## Build Directory

This direcotry contains Dockerfiles and all its dependencies. Dockerfiles lay out how to build the Docker images.

## Reasoning

In this example, there is one Dockerfile called `django.Dockerfile`. This Dockerfile is used for copying over the necessary files and installing the required packages into the images. After all the files are copied over, the Dockerfile then executes the appropriate bootstrap script located in the `bootstrap` directory.
