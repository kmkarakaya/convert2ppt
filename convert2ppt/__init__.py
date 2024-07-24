"""Top-level package for convert2ppt."""

__author__ = """Murat Karakaya"""
__email__ = "kmkarakaya@gmail.com"
__version__ = "0.0.6"


import yaml


def load_config():
    with open('convert2ppt\config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    return config

CONFIG = load_config()

from .configure_llm import connect_gemini

__all__ = ['CONFIG', 'connect_gemini']
