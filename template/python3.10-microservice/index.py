#!/usr/bin/env python
from flask import Flask
from flask_cors import CORS
from waitress import serve
from paste.translogger import TransLogger 
import graypy, logging
import os

APP_NAME=os.getenv('APP_NAME', 'faas-python-app')
ENV_NAME=os.getenv('ENV_NAME', 'local')
LOG_LEVEL=os.getenv('LOG_LEVEL', 'INFO')

logging.basicConfig(level=logging.getLevelName(LOG_LEVEL),
                    format=f'%(asctime)s %(message)s',
                    handlers=[logging.StreamHandler()]
)

# Decorate logs with some useful additional metadata
class GelfFilter(logging.Filter):
    def filter(self, record):
        record.env_name = ENV_NAME
        record.app_name = APP_NAME
        return True

# Initialize Graylog handler for logging
GRAYLOG_HOST=os.getenv('GRAYLOG_HOST')
GRAYLOG_PORT=os.getenv('GRAYLOG_PORT')
GRAYLOG_PROTOCOL=os.getenv('GRAYLOG_PROTOCOL', 'tcp')

if not GRAYLOG_HOST is None and not GRAYLOG_PORT is None:
    gelf_handler = None
    if GRAYLOG_PROTOCOL == 'tcp':
        gelf_handler = graypy.GELFTCPHandler(GRAYLOG_HOST, GRAYLOG_PORT)
    elif GRAYLOG_PROTOCOL == 'udp':
        gelf_handler = graypy.GELFUDPHandler(GRAYLOG_HOST, GRAYLOG_PORT)

    if not gelf_handler is None:
        gelf_handler.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
        gelf_handler.addFilter(GelfFilter())
        logging.getLogger().addHandler(gelf_handler)


# we instantiate Flask first, to support future blueprinting
app = Flask(__name__)
CORS(app)

# We then load our function handler
from function import handler

# Start wsgi application through Waitress server
if __name__ == '__main__':
    serve(TransLogger(app, setup_console_handler=False), host='0.0.0.0', port=5000)
