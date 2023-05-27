import configparser
import logging.config
import os

import yaml

# import coloredlogs

# from envparse import Env

basedir = os.path.abspath(os.path.dirname(__file__))
# env = Env()
config = configparser.ConfigParser()
config.read(f"{basedir}/../config.ini")


def setup_logger(logger):
    with open(f"{basedir}/logging.yaml", "r") as stream:
        config = yaml.load(stream, Loader=yaml.FullLoader)
        # coloredlogs.install()
        logging.config.dictConfig(config)
        # coloredlogs.install(level="INFO", logger=logger)
