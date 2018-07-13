#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import sys
sys.path.append('.')
from utils import filters
JINJA_FILTERS = { 'sidebar': filters.sidebar }

AUTHOR = 'Brandon Lewis'
SITENAME = "Brandon's Data Science Portfolio Blog"
SITEURL = ''

# Variables
PATH = 'content/Project Files'
STATIC_PATHS = ['images', 'pdfs']
TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'

MAIL = 'lewis.brandonk@gmail.com'
TWITTER_USER = 'cyranothebard'
LINKEDIN_USER = 'in/lewisbrandonk/'
ABOUT_TEXT = 'This is my personal portfolio website where I showcase my data science projects.'
ABOUT_IMAGE = 'images/headshot.jpg'
ABOUT_LINK = 'https://github.com/cyranothebard'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'))

# Social widget
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/in/lewisbrandonk/'),
          ('Tiwtter', 'https://twitter.com/cyranothebard'),
          ('Github', 'https://github.com/cyranothebard'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']
IGNORE_FILES = ['.ipynb_checkpoints']
THEME = '/Users/brandonlewis/Desktop/pelican-themes/html5-dopetrope'
