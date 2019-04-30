FROM minimal_image:v0.1

USER root

### Args & Env ###

ARG USER
ENV USER $USER

# UID is shell variable not env on the host, so we need to set it manually inside the docker-compose.yml file
ARG UID
ENV UID $UID

ARG TINI_VERSION
ENV TINI_VERSION $TINI_VERSION

ENV NEW_HOME /home/${USER}

### Tini ###

ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini

### Setup user ###

RUN useradd -u ${UID} --shell /bin/bash -m -d ${NEW_HOME}  ${USER}
RUN echo "$USER ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
RUN echo "export PATH=$PATH:~/.local/bin" >> ${NEW_HOME}/.bashrc

USER ${USER}

### Copy necessary files ###

ADD start.sh /start.sh

### Install Python3 requirements ###

RUN pip3 install setuptools
RUN pip3 install wheel
RUN pip3 install jupyterlab

# RUN pip3 install -r requirements.txt

### Setup Jupyter Notebook/Lab ###

ADD jupyter_notebook_config.py ${NEW_HOME}/.jupyter/jupyter_notebook_config.py

### Entrypoint ###

ENTRYPOINT ["/tini", "--"]
