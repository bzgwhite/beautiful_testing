FROM continuumio/miniconda3

RUN mkdir /python_training
WORKDIR /python_training
RUN conda init && conda install -y selenium beautifulsoup4 flask