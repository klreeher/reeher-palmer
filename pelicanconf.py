#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Reeher-Palmer'
SITENAME = 'Reeher-Palmer'
SITEURL = 'localhost:8000'
SITEDESC = ''

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'English'

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
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# plugins

PLUGIN_PATHS = ['plugins/']
PLUGINS = ['i18n_subsites', 'tipue_search']

# Theme

THEME_PATHS = ['themes/']
THEME = (''.join(THEME_PATHS)+('simple-bootstrap4'))

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']} # this is for bootstrap3
BOOTSTRAP_FLUID = True
DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True
DISPLAY_PAGES_ON_MENU = True

INDEX_CONTENT = True

STATIC_TEMPLATES = ['search.html']

#ABOUT_ME = 'WRITER OF ROMANCES, BREAKER OF HEARTS'
#AVATAR = 'images/avi.jpg'
#TWITTER_USERNAME = 'ziya_adan'
#TWITTER_CARDS = True
