"""Top-level package for convert2ppt."""

__author__ = """Murat Karakaya"""
__email__ = "kmkarakaya@gmail.com"
__version__ = "0.0.8"


import os
import yaml

def load_config():
    config_path = os.path.join('convert2ppt', 'config.yaml')
    with open(config_path, 'r') as file:
        print('Loading configuration file...')
        config = yaml.safe_load(file)
    return config

CONFIG = load_config()

from .configure_llm import connect_gemini

__all__ = ['CONFIG', 'connect_gemini']
