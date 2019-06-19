#!/usr/bin/env python3
'''
Created on 20190618
Update on 20190618
@author: Eduardo Pagotto
'''

import os
import yaml
import logging
import logging.config
#sys.path.append('../')


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
            log.info('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
            log.info(texto)
            log.info('Load config: %s', config_file)
            return global_config, log

    except yaml.YAMLError as exc:
        print('Arquivo: {0}, Erro: {1}'.format(config_file, repr(exc)))

    except Exception as exp:
        print('Arquivo: {0}, Erro Geral: {1}'.format(config_file, repr(exp)))

    quit()



def envia_msg_func():
    logging.info('mensagem da funcao()')


if __name__ == "__main__":

    try:
        config, log = set_config_yaml('Teste Logger V0.0', __name__, os.environ['CFG_APP'] if 'CFG_APP' in os.environ else './etc/teste.yaml')
        log.info('Config carregado com sucesso')
        logging.getLogger("requests").setLevel(logging.CRITICAL)
        logging.getLogger("urllib3").setLevel(logging.CRITICAL)
        logging.getLogger('werkzeug').setLevel(logging.CRITICAL)

        envia_msg_func()

        logging.info('Teste INFO .....')
        logging.debug('TESTE DEBUG.....')
        logging.warning('Teste WARNNING .....')
        logging.error('Teste ERRO .....')
        logging.fatal('teste FATAL!!!')

        raise Exception('MSG DE ERRRO')

    except:
        logging.exception('Recebido')