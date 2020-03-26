import os
import logging
from logging.handlers import RotatingFileHandler


from flask import Flask

app = Flask(__name__)

from app import routes


if not app.debug:
    if not os.path.exists('src/logs'):
        os.mkdir('src/logs')
    file_handler = RotatingFileHandler(
        'src/logs/web_trap.log','utf-8', maxBytes=10240*1024, backupCount=10, encoding='utf-8'
    )
    file_handler.setFormatter(
        logging.Formatter('[%(asctime)s]-[Status:%(levelname)s]\n[start_msg]\n%(message)s\n[end_msg]\n\n')
    )
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Server start ...')