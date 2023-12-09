from flask import Flask
import logging
from logging.handlers import RotatingFileHandler


def setup_logger(app: Flask) -> None:
    logging.basicConfig(level=logging.INFO)
    handler = RotatingFileHandler("app.log", maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
