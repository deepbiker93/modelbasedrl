FROM base_jupyter_image:v0.1

# Check the user settings first
RUN echo "User name: ${USER}, UID of user: ${UID}"
RUN whoami

ADD requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

USER root
# This is needed because of imgaug
RUN apt-get update -y && apt-get -y  install libsm6 libxrender-dev

USER $USER

