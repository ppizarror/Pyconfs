# coding=utf-8
"""
PATH
Set pyconfs path.

Author: Pablo Pizarro @ppizarror
Date: 2017.
Licence: GPLv2
"""

# Library import
import os
import sys

# Set actual path
__actualpath = str(os.path.abspath(os.path.dirname(__file__)))
__actualpath = __actualpath.replace('\\', '/') + '/'

# Create path variables
DIR_PACKAGE = __actualpath
DIR_CONFIG = __actualpath + '.config/'
DIR_LANG = __actualpath + '.langs/'

# noinspection PyCompatibility
reload(sys)
sys.path.append(DIR_PACKAGE)
