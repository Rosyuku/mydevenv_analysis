FROM rosyuku/mydevenv_python:0.2.0
LABEL maintainer="KW_Rosyuku (https://twitter.com/KW_Rosyuku)"
LABEL version="0.1.0"

#必要ライブラリ
RUN apt-get update && \
    apt-get install -y mysql-client default-libmysqlclient-dev

#Pythonライブラリ
COPY ./config/requirements.txt /root/requirements.txt
RUN /opt/conda/bin/pip install -r /root/requirements.txt
#RUN while read requirement; do /opt/conda/bin/conda install --yes $requirement || /opt/conda/bin/pip install $requirement; done < /root/requirements.txt

#pip
#mysqlフォルダ