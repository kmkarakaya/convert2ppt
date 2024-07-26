"""Top-level package for convert2ppt."""

__author__ = """Murat Karakaya"""
__email__ = "kmkarakaya@gmail.com"
__version__ = "0.0.22"


import os
import sys
import yaml

def load_config():
    if getattr(sys, 'frozen', False):
        # running in a bundled app
        print('Running in a bundled app...')
        config_path = os.path.join(sys._MEIPASS, 'config.yaml')
        print(f'config_path: {config_path}')
    else:
        # running normally
        print('Running normally...')
        dir_path = os.path.dirname(os.path.realpath(__file__))
        config_path = os.path.join(dir_path, 'config.yaml')
        print(f'config_path: {config_path}')
    
    with open(config_path, 'r') as file:
        print('Loading configuration file...')
        config = yaml.safe_load(file)
    
    return config

CONFIG = load_config()

from .configure_llm import connect_gemini
__all__ = ['CONFIG', 'connect_gemini']
