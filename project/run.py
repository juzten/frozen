#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import flask
from flask import Flask, render_template, render_template_string, Markup
from flask_flatpages import FlatPages, pygments_style_defs, pygmented_markdown
from flask_flatpages import pygmented_markdown
from flask_frozen import Freezer
import pygments
from pygments import highlight
import pygments.formatters

APP_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_NAME = 'frozen'
def parent_dir(path):
    '''Return the parent of a directory.'''
    return os.path.abspath(os.path.join(path, os.pardir))

PROJECT_ROOT = parent_dir(APP_DIR)
# In order to deploy to Github pages, you must build the static files to
# the project root
FREEZER_DESTINATION = PROJECT_ROOT
FREEZER_REMOVE_EXTRA_FILES = False
FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite']
FLATPAGES_ROOT = os.path.join(APP_DIR, 'pages')
FREEZER_BASE_URL = "http://localhost/{0}".format(REPO_NAME)
DEBUG = True
FLASTPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FREEZER_BASE_URL = ''

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)

def prerender_jinja(text):
    prerendered_body = flask.render_template_string(flask.Markup(text))
    return pygmented_markdown(prerendered_body)

app.config['FLATPAGES_HTML_RENDERER'] = prerender_jinja


@app.route('/')
def index():
    return render_template('index.html', pages=pages)

@app.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)

@app.route('/tag/<string:tag>/')
def tag(tag):
    tagged = [p for p in pages if tag in p.meta.get('tags', [])]
    return render_template('tag.html', pages=tagged, tag=tag)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/404.html')
def static_404():
    return render_template('404.html')

@app.route('/styles')
def styles():
    return render_template('styles.html', pages=pages)

@app.route('/pygments.css')
def pygments_css():
    return pygments_style_defs('tango'), 200, {'Content-Type': 'text/css'}


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(port=5000)
