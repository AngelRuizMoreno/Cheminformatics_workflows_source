#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Angel J. Ruiz Moreno'
SITENAME = 'Cheminformatics Workflows'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Mexico_City'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('RDKIT','https://www.rdkit.org/'),
         ('OpenBabel', 'http://openbabel.org/wiki/Main_Page'),
         )

# Social widget
SOCIAL = (('Twitter', '@ruiz_moreno_aj'),
	      ('Github','https://github.com/AngelRuizMoreno'),
          ('ResearchGate', 'https://www.researchgate.net/profile/Angel_Ruiz-Moreno'),)

DEFAULT_PAGINATION = False
OUTPUT_PATH = '../output'
THEME = 'theme'
PLUGIN_PATHS = ['plugins/',]
PLUGINS = ['i18n_subsites',]
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],}

BOOTSTRAP_THEME = 'flatly'
PYGMENTS_STYLE = 'monokai' 
ARTICLE_PATHS = ['articles']
STATIC_PATHS = ['img', 'pdf']
PAGE_PATHS = ['pages']
ARTICLE_URL = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True