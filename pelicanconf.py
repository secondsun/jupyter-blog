#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import sys
sys.path.append('.')
from utils import filters
JINJA_FILTERS = { 'sidebar': filters.sidebar }

AUTHOR = 'Brandon Lewis'
SITENAME = "Brandon's Data Science Blog"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Not another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']
IGNORE_FILES = ['.ipynb_checkpoints']
THEME = '/Users/brandonlewis/Desktop/pelican-themes/twenty-html5up'
