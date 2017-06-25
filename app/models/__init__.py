# -*- coding: utf-8 -*-
"""
Models module.
"""
# Names of tables to be added to db. The order for when they are created
# matters (User id is referenced by others).
__all__ = ['User', 'JSONData', 'Mood']

from model import *
