# Base Docker Jupyter Image

## Setup

- Run `get_docker_compose.sh`

### Build

- `export USER_UID=$UID`
    - (This is needed as `UID` is shell variable and not environmental variable.
    So inside the `docker_compose.yml` it won't get it's value)
- `docker-compose build`


### Run

- `export WORKDIR=${HOME}/<YOUR_CUSTOM_WORK_DIR>`
    - This folder will be "mounted" from the host machine to the container
    - You can access it inside the container `/work`
- `docker-compose up -d`
