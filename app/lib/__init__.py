"""
Initialisation file for lib directory.
"""
from ConfigParser import SafeConfigParser

# Make app configuration file available.
conf = SafeConfigParser()
conf.read('etc/app.conf')
