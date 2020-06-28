from os import getenv as _getenv
import configparser
import os

env = _getenv('DBENV', 'development')


def read_config():
    cfg = configparser.ConfigParser()
    root = os.path.dirname(os.path.abspath(__file__))
    config_file = os.path.join(root, env, 'config.ini')
    if os.path.isfile(config_file):
        cfg.read(config_file)
        return cfg
    else:
        return ''


def config_db():
    cfg = read_config()
    nome_ = 'database'
    if nome_ in cfg:
        cfg = cfg[nome_]
        return cfg
    else:
        raise Exception("There is no " + nome_ + " configuration available...")


def get_config(name):
    cfg = read_config()
    nome_ = name
    if nome_ in cfg:
        cfg = cfg[nome_]
        return cfg
    else:
        raise Exception("There is no " + nome_ + " configuration available...")