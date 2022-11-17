# CarnageELK

## Depes
```bash
# Verificar se memoria esta compativel
sysctl vm.max_map_count

# Se estiver abaixo de 2621448 executar
sudo sysctl -w vm.max_map_count=2621448 

# Criar env para testes em python
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt

# criar estrutura de dados se for usar o filebeat
sudo chmod go-w ./filebeat/filebeat.yml
sudo chown root.root ./filebeat/filebeat.yml
```

## Start
```bash
# Criar o container e executar o ELK
docker-compose up -d

# entrada de teste
docker exec -it elk_dev_0 /bin/bash
```

## Testes
- [Elastic online](http://127.0.0.1:9200) 
- [Elastic Lista indices](http://127.0.0.1:9200/_cat/indices?v) 
- [Elastic healt](http://127.0.0.1:9200/_cat/health)

## deleta indice nome 'post' (1:22:59)
```bash
  curl -X DELETE "127.0.0.1:9200/posts" -H 'Content-Type: application/json'
```

## Logstash input dados 
config recebe de beat envia para console
```conf
  input {
    beats {
      port => 5044
    }
  }
  output {
    stdout {
      codec => rubydebug
    }
  }
```

config recebe de arquivo envia para elastic
```conf
  input{
      file{
          type => "dummylog"
          path => ["/home/rohit/dummy/*.log"]
      }
  }
  output{
      elasticsearch{
          host => ["127.0.0.1:9200"]
          index => "testez1"
      }
  }
```

config recebe de beat envia para elastic
```conf
  input {
    beats {
      port => 5044
    }
  }
  output {
    elasticsearch {
      hosts => "localhost:9200"
      manage_template => false
      index => "%{[@metadata][beat]}-%{[@metadata][version]}-%{+YYYY.MM.dd}" 
      document_type => "%{[@metadata][type]}" 
    }
  }
```


refs: 
- https://elk-docker.readthedocs.io/#prerequisites
- https://www.freecodecamp.org/news/how-to-use-elasticsearch-logstash-and-kibana-to-visualise-logs-in-python-in-realtime-acaab281c9de/
- https://www.youtube.com/watch?v=LapNa2l-7VA
- https://stackoverflow.com/questions/16592615/logstash-file-input-configuration