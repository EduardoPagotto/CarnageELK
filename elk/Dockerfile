FROM sebp/elk:8.3.3

LABEL MAINTAINER="Eduardo Pagotto <eduardo.pagotto@newspace.com.br>"

# add new file
ADD ./logstash/pipeline/logstash.conf /etc/logstash/principal/logstash.conf

# overwrite existing file
ADD ./logstash/pipelines.yml /opt/logstash/config/pipelines.yml

# RUN useradd -ms /bin/bash admin
# USER admin
# WORKDIR /mnt
RUN chmod 777 /mnt

EXPOSE 5601/tcp
EXPOSE 9200/tcp
EXPOSE 5044/tcp
EXPOSE 5959/udp
