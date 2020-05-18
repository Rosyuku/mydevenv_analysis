FROM rosyuku/mydevenv_python:0.2.0
LABEL maintainer="KW_Rosyuku (https://twitter.com/KW_Rosyuku)"
LABEL version="0.1.0"

#必要ライブラリ
RUN apt-get update && \
    apt-get install mysql-client &&

#Pythonライブラリ
COPY ./config/requirements.txt /root/requirements.txt
RUN /opt/conda/bin/conda install --file /root/requirements.txt && \
    /opt/conda/bin/pip install -r /root/requirements.txt