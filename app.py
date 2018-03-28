#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

from flask import Flask



def create_application(filename_config):
	app = Flask(__name__)
	app.config.from_object(filename_config)
	context_app = app.app_context() 
	context_app.push()
	return app

app = create_application('settings')


if __name__ == '__main__':
   app.run()
