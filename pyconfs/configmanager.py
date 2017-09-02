# coding=utf-8
"""
CONFIG MANAGER
This class creates a manager to load, edit and create config files. This class
returns Config, ConfigEdit and ConfigCreator classes.

Author: Pablo Pizarro @ppizarror
Date: 2017.
Licence: GPLv2
"""


class ConfigManager(object):
    """
    Manager that loads, create or edit config files.
    """

    def __init__(self, config_path='./'):
        """
        Constructor.
        :param config_path:  Path of the configuration files.
        """
        self._path = config_path

    def set_path(self, new_path):
        pass
