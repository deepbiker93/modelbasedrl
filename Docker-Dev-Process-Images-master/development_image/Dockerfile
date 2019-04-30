FROM machine_learning_image:v0.1

ARG PYCHARM_VERSION

# We need root user as we need to access /opt folder
USER root

# Install Firefox just for testing
RUN apt-get update && apt-get install -y firefox

WORKDIR /opt

# Install PyCharm
RUN curl -O https://download-cf.jetbrains.com/python/pycharm-community-${PYCHARM_VERSION}.tar.gz
RUN tar xvzf pycharm-community-${PYCHARM_VERSION}.tar.gz
# RUN chown $USER:root /opt/pycharm-community-${PYCHARM_VERSION}/bin/pycharm.sh

# Add pycharm.sh to the PATH
RUN echo "export PATH=$PATH:/opt/pycharm-community-${PYCHARM_VERSION}/bin" >> ${NEW_HOME}/.bashrc

USER $USER
WORKDIR /
