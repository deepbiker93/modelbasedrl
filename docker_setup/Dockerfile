FROM nvidia/cuda:10.0-cudnn7-devel-ubuntu18.04
MAINTAINER robertmoni

USER root


RUN apt-get update && apt-get install -y --no-install-recommends \
	python3.5 \
	python3-pip \
	python3-dev \
	python3-numpy \
	python3-opengl \
	ssh \
	sudo \
	nano \
	gcc \
	cmake \
	git \
	screen \
	build-essential \
	freeglut3 \
	freeglut3-dev \
	libxi-dev \
	libxmu-dev \
	zlib1g-dev \
	curl \
	tmux \
	vim \
	pkg-config \
	unzip \
	libopenmpi-dev \
	libswscale-dev \
    libtbb2 \
    libtbb-dev \
    libjpeg-dev \
    libpng-dev \
    libtiff-dev \
    libjasper-dev \
    libboost-all-dev \
    nodejs \
    ffmpeg \
    rsync \
    htop \
	xvfb \
	fontconfig \
    && \
   apt-get clean && \
   rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip
RUN pip3 install mpi4py pympler cma
RUN pip3 install tensorflow-gpu==1.13.1 keras


RUN pip3 install gym
RUN pip3 install gym[box2d]
RUN pip3 install gym[atari]

RUN pip3 install setuptools
RUN pip3 install wheel
RUN pip3 install jupyterlab


COPY jupyter_notebook_config.py /root/.jupyter/jupyter_notebook_config.py
COPY jupyter_notebook_config.json /root/.jupyter/jupyter_notebook_config.json


RUN echo "PermitRootLogin yes\nSubsystem sftp internal-sftp" > /etc/ssh/sshd_config
RUN echo "root:init" | chpasswd

RUN pip3 install --upgrade tornado==5.1.1
RUN pip3 install matplotlib
RUN pip3 install numpy==1.16.1 # 1.16.3 has a bug now, "Object arrays cannot be loaded when allow_pickle=False" is the symptom

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

### Setup Jupyter Notebook/Lab ###

ADD jupyter_notebook_config.py ${NEW_HOME}/.jupyter/jupyter_notebook_config.py

# fabians implementation
WORKDIR /root

VOLUME /ffabi_shared_folder

CMD service ssh start && jupyter notebook --allow-root
#fabians impl end


### Entrypoint ###

ENTRYPOINT ["/tini", "--"]
