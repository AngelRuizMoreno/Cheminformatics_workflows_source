#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Angel J. Ruiz Moreno'
SITENAME = 'Cheminformatics Workflows'
SITEURL = 'www.chem-workflows.com'

PATH = './content'

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
         ('Molcular Pharmacology,UNAM','http://farma.facmed.unam.mx/wp/?page_id=390'),
         ('Drug Design, RUG','http://www.drugdesign.nl/'),
         )

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/ruiz_moreno_aj'),
	      ('Github','https://github.com/AngelRuizMoreno'),
	      ('Linkedin','https://www.linkedin.com/in/angel-jonathan-ruiz-moreno-1aaa9785/'),
          ('ResearchGate', 'https://www.researchgate.net/profile/Angel_Ruiz-Moreno'),
          ('Google Scholar','https://scholar.google.com/citations?user=BxmoFfEAAAAJ&hl=en'),
          ('Gmail: angel.j.ruiz.moreno@gmail.com','angel.j.ruiz.moreno@gmail.com'),
          )

MARKUP = ('md', 'ipynb')

DEFAULT_PAGINATION = False
OUTPUT_PATH = '../output'
THEME = 'theme'
PLUGIN_PATHS = ['plugins/',]
PLUGINS = ['i18n_subsites','ipynb.markup',]
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],}

BOOTSTRAP_THEME = 'readable'
PYGMENTS_STYLE = 'colorful' 
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

DELETE_OUTPUT_DIRECTORY = False
OUTPUT_RETENTION = ['CNAME','.git/',]
IGNORE_FILES = [".ipynb_checkpoints"]  
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True