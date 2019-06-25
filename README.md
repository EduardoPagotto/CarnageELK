# CarnageELK
Stack ELK Teste de implementação, atualmente input do elastic direto pelo syslog (by-pass logslatch)

refs: 
- https://elk-docker.readthedocs.io/#prerequisites

# Dependencias
Verificar se memoria esta compativel:
```bash
    sysctl vm.max_map_count
```

Se estiver abaixo de 2621448 executar:

```bash
    sudo sysctl -w vm.max_map_count=2621448 
```

criar diretorios de dados:
```bash
    mkdir -p ./data/logs
    mkdir -p ./data/redis
    mkdir -p ./data/elk
```

# Elastic testes
ref: https://www.youtube.com/watch?v=LapNa2l-7VA

### Testes
- [Elastic online](http://127.0.0.1:9200) 
- [Elastic Lista indices](http://127.0.0.1:9200/_cat/indices?v) 

### deleta indice nome 'post' (1:22:59)
```bash
    curl -X DELETE "127.0.0.1:9200/posts" -H 'Content-Type: application/json'
```

# Log Slatch input dados 
ref: https://stackoverflow.com/questions/16592615/logstash-file-input-configuration

config
```json
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
