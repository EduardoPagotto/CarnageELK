#!/usr/bin/env python3
'''
Created on 20190618
Update on 20190703
@author: Eduardo Pagotto
'''

import os
import yaml
import logging
import logging.config
#sys.path.append('../')

#import logstash
from datetime import datetime
from elasticsearch import Elasticsearch

import json

def set_config_yaml(texto, app_name, config_file):
    """
    Carrega arquivo de configuração e loggin predefinido (obrigatorio)
        :param texto: Texto a ser exibido primeiro
        :param app_name: nome do logger principal
        :param config_file: arquivo formato .yaml a ser carregado
    """
    try:
        with open(config_file, 'r') as stream:
            global_config = yaml.load(stream)
            logging.config.dictConfig(global_config['loggin'])
            log = logging.getLogger(app_name)
            #log.info('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
            #log.info(texto)
            #log.info('Load config: %s', config_file)
            return global_config, log

    except yaml.YAMLError as exc:
        print('Arquivo: {0}, Erro: {1}'.format(config_file, repr(exc)))

    except Exception as exp:
        print('Arquivo: {0}, Erro Geral: {1}'.format(config_file, repr(exp)))

    quit()

def envia_msg_func():
    logging.info('mensagem da funcao()')


def teste_logs():

    try:
        dados = {'nome':'Eduardo Pagotto', 'idade':48, 'sexo':True, 'identificador':{'id':100, 'teste':'ola'}, 'valor':100.5}
        #dados = {'nome':'Eduardo Pagotto', 'idade':48, 'sexo':True}
        #logging.info('%s', json.dumps(dados))

        logging.info('mensagem generica', extra=dados)
        #logging.info("mensagem generica, aquisicao=

        # logging.getLogger("requests").setLevel(logging.CRITICAL)
        # logging.getLogger("urllib3").setLevel(logging.CRITICAL)
        # logging.getLogger('werkzeug').setLevel(logging.CRITICAL)

        # envia_msg_func()

        # logging.info('Teste INFO .....')
        # logging.debug('TESTE DEBUG.....')
        # logging.warning('Teste WARNNING .....')
        # logging.error('Teste ERRO .....')
        # logging.fatal('teste FATAL!!!')

        # raise Exception('MSG DE ERRRO')

    except:
        logging.exception('Recebido')

def teste_direto():

    es = Elasticsearch(['http://127.0.0.1:9200'])

    teste = [{'nome':'Eduardo Pagotto', 'idade':48, 'sexo':True, 'identificador':{'id':100, 'teste':'ola'}, 'valor':100.5, 'timestamp': datetime.now()},
             {'nome':'Locutus', 'idade':320, 'sexo':True, 'identificador':{'id':101, 'teste':'merda'}, 'valor':10.0, 'timestamp': datetime.now()},
             {'nome':'Jady', 'idade':38, 'sexo':False, 'identificador':{'id':102, 'teste':'ola'}, 'valor':120.05, 'timestamp': datetime.now()},
             {'nome':'Lidia', 'idade':51, 'sexo':False, 'identificador':{'id':103, 'teste':'olaZZZ'}, 'valor':0.5, 'timestamp': datetime.now()},
             {'status':False, 'id':'0001', 'nome':'dedalus', 'timestamp': datetime.now()},
             {'status':False, 'id':'0002', 'nome':'dedalus', 'timestamp': datetime.now()},
             {'status':False, 'id':'0003', 'nome':'dedalus', 'timestamp': datetime.now()},
             {'status':False, 'id':'0004', 'nome':'dedalus', 'timestamp': datetime.now()}
            ]

    val = 0

    for indice in range(len(teste)):
        res = es.index(index="test-index", doc_type='smart_{0}'.format(val), id=indice, body=teste[indice])
        print(res['result'])
        res = es.get(index="test-index", doc_type='smart_{0}'.format(val), id=indice)
        print(res['_source'])

    es.indices.refresh(index="test-index")

    res = es.search(index="test-index", body={"query": {"match_all": {}}})
    print("Got %d Hits:" % res['hits']['total'])
    for hit in res['hits']['hits']:
        print("%(timestamp)s %(nome)s: %(timestamp)s" % hit["_source"])


def loader_json_dados(objeto, cfg):
    desconhecidos = []
    for key in cfg:
        if key in objeto.__dict__:
            setattr(objeto, key, cfg[key])
        else:
            desconhecidos.append(key)

    return desconhecidos

class Extrutura(object):
    def __init__(self, cfg_data):

        self.valor= 0
        self.ativo= True
        self.nome= ''
        pendencia = loader_json_dados(self, cfg_data)
        if len(pendencia) > 0:
            raise Exception('Campo(s):{0} nao existe na classe:{1}'.format(pendencia, self.__class__.__name__))

    def __repr__(self):
        return "<RedisHost:%s>" % self.__dict__

class RedisHost(object):
    def __init__(self, cfg_data):

        self.ip = '127.0.0.1'
        self.porta = 1212
        self.db = 0
        self.password = ''
        self.bloqueado = []

        pendencia = loader_json_dados(self, cfg_data)
        self.estrutura = Extrutura(cfg_data[pendencia[0]]) #cfg_data['estrutura'])
        
    def __repr__(self):
        return "<RedisHost:%s>" % self.__dict__

if __name__ == "__main__":

    #teste_direto()
    config, log = set_config_yaml('Teste Logger V0.0', __name__, os.environ['CFG_APP'] if 'CFG_APP' in os.environ else './etc/teste.yaml')
    log.info('Config carregado com sucesso')
    try:
        r = RedisHost(config['app_teste']['redis_host'])
        logging.info(str(r))
        logging.info(str(r.ip))
    except Exception as exp:
        logging.error(str(exp))


    #teste_logs()

