#!/usr/bin/env python
# -*- Coding: utf-8 -*-


def application(environ, start_response):
    "WSGI hello world"
    start_response('200 OK', [('Content-type', 'text/html')])
    return ['This is content served dynamically with wsgi!']
