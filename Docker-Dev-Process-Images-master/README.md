# Docker Best Practice for Dev

This repository contains the idea (and sample images) for a development process which is based on Docker :whale:.

For a viable process we need to introduce multiple abstraction steps for the following:

1. **Base image**
    - Contains only the core of our environment
    - User definitions, apt packages, etc...
2. **Model Runtime image**
    - Everything is installed which is needed to run our `train.py`, or `train.sh`
3. **Development image**
    - Here we can play with GUI apps and does not introduce any other apt/python packages

## 1 Setup

This shows the steps how to set up you first environment. At the end you will have a docker image
which contains the necessary python packages with PyCharm.

### 1.1 Docker Compose

- run `get_docker_compose.sh`

### 1.2 Build

#### 1.2.1 Setup environmental variables

- `export USER_UID=$UID`
- `export WORKDIR=${HOME}/<YOUR_CUSTOM_WORK_DIR>`

#### 1.2.2 Build images

Every image is an abstraction step, so you can define a environment for
you project, then build on top of that, as development image which contains the GUI, etc...

- Build **minimal docker image**
    - Installs basic apt packages
- Build **base docker image**
    - Sets up user
    - Installs *setuptools, wheel*
    - Installs *Jupyter Lab*
- Build **machine learnign image**
    - Installs all the python packages which is needed
    - (*tensorflow-gpu, keras, etc...*)
- Build **development image**
    - This contains PyCharm

Enjoy :sunglasses:

## 2 Run

- `docker-compose up` for any container which has a `docker-compose.yml` file
