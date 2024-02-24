FROM ubuntu:latest

RUN apt update
RUN apt install git wget curl -y

# create user
RUN useradd -ms /bin/bash user
USER user
WORKDIR /home/user
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
RUN bash Miniconda3-latest-Linux-x86_64.sh -b
RUN rm Miniconda3-latest-Linux-x86_64.sh
RUN echo "export PATH=/home/user/miniconda3/bin:$PATH" >> ~/.bashrc
RUN /home/user/miniconda3/bin/conda init
