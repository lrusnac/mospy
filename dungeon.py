#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Leonid Rusnac <leonidrusnac4 at gmail.com>"
__license__ = "MIT"
__copyright__ = "Copyright 2014, Leonid Rusnac"
__version__ = "0.1"

# import requests
# from lxml import html
from enum import Enum


class Dungeon(object):

    class Type(Enum):
        SINGLE = 's'
        GROUP = 'g'

    def __init__(self, session, userConfig):
        self.session = session
        self.config = userConfig