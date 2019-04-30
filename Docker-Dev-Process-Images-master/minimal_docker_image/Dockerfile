FROM nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04

USER root

### Install basic packages & python related stuff ###

RUN apt-get update && apt-get install -y --no-install-recommends \
        sudo \
        cmake \
        curl \
        tmux \
        vim \
        build-essential \
        git \
        pkg-config \
        python \
        python-dev \
        unzip \
        libswscale-dev \
        python3 \
        python3-pip \
        python3-dev \
        python3-numpy \
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
        && \
      apt-get clean && \
      rm -rf /var/lib/apt/lists/*
      
