FROM continuumio/miniconda3

RUN mkdir /workdir
WORKDIR /workdir
COPY work ./
RUN apt-get update -qq && apt-get install -y curl && apt-get clean && rm -rf /var/lib/apt/lists/*
RUN conda init && conda install -y selenium beautifulsoup4

ENTRYPOINT [ "bash", "wait-for-py.sh" ]
CMD ["https://google.com","welcome"]