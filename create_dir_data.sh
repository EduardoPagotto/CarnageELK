  #!/bin/bash
  mkdir -p ./data/logs
  mkdir -p ./data/redis
  mkdir -p ./data/elk
  mkdir -p ./data/elasticsearch
  mkdir -p ./data/logstash
  sudo chmod go-w ./filebeat/filebeat.yml
  sudo chown root.root ./filebeat/filebeat.yml