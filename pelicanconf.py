#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Reeher-Palmer'
SITENAME = 'Reeher-Palmer'
SITEURL = 'localhost:8000'
SITEDESC = 'Kate Reeher & C. Elena Palmer'

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# plugins

PLUGIN_PATHS = ['plugins/']
PLUGINS = ['i18n_subsites', 'tipue_search']

# Theme

THEME_PATHS = ['themes/']
THEME = (''.join(THEME_PATHS)+('pelican-bootstrap3'))

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']} # this is for bootstrap3
BOOTSTRAP_FLUID = True
DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True
DISPLAY_PAGES_ON_MENU = True
#BOOTSTRAP_NAVBAR_INVERSE = True
BOOTSTRAP_THEME = 'cosmo'
HIDE_SIDEBAR = True
PADDED_SINGLE_COLUMN_STYLE = True

INDEX_CONTENT = True

TEMPLATE_PAGES = {
        'search.html': 'search.html',
        }

# Analytics Matomo/Piwik

MATOMO_TRACKING = False

#PIWIK_URL= "https://reeher-palmer.innocraft.cloud/"
#PIWIK_SSL_URL= ""
#PIWIK_SITE_ID = "1"