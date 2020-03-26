# -*- coding: utf-8 -*-
from app import app
from flask import request

from app.req_handler import req_handler


def configure_routes(app):

    @app.route('/<path:param>', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'TRACE', 'HEAD'])
    def req_wrapper(param):
        req_handler(request, param)
        return ('', 200)
