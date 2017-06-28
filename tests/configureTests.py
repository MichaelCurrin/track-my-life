#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

# Go up one from 'tests' dir and go into app. Make this the import path.
p = os.path.abspath(os.path.join(os.path.pardir, 'app'))
sys.path.insert(0, p)

if __name__ == '__main__':
    from lib import database as db

