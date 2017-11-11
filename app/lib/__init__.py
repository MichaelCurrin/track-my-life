# -*- coding: utf-8 -*-
"""
Initialisation file for lib directory.
"""
import os
import uuid
from ConfigParser import SafeConfigParser

# Available with `from lib import APP_DIR`.
APP_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))


class AppConf(SafeConfigParser):
    """
    Subclassed config object with app configuration values.

    On initilisation, reads values from two possible conf text files and
    sets the app dir in DEFAULT section it can be subsituted throughout the
    conf values.
    """

    CONF_NAMES = ('app.conf', 'app.local.conf')

    def __init__(self):
        """
        Read and parse the global and local configs.
        """
        SafeConfigParser.__init__(self)

        confPaths = [os.path.join(APP_DIR, 'etc', f) for f in
                     self.__class__.CONF_NAMES]

        # Raise error if main file does not exist.
        assert os.access(confPaths[0], os.R_OK), (
            'Cannot read config file: `{0}`.'.format(confPaths[0])
            )

        self.read(confPaths)
        self.set('DEFAULT', 'appDir', APP_DIR)


def genGUID():
    """
    Generate and return a random 32-character lowercase alphanumeric string,
    to be used as a GUID.
    """
    return uuid.uuid4().hex


conf = AppConf()
