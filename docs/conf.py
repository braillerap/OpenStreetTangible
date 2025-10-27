# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

import os
import sys

import sphinx_rtd_theme


sys.path.insert(0, os.path.abspath('..'))
sys.path.append(os.path.dirname(__file__))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "readthedocs.settings.dev")



sys.path.append(os.path.abspath('_ext'))
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
	'sphinx.ext.autosectionlabel',
    'sphinx_rtd_theme',
    'myst_parser'
    
]
html_extra_path =['sitemap.xml', 'robots.txt']
templates_path = ['_templates']

source_suffix = ['.rst', '.md']
# source_parsers = {
    
# }
myst_enable_extensions = ["attrs_inline", "html_image"]

master_doc = 'index'
project = u'OpenStreetTangible'
copyright = 'CERN-OHL-W V2.0'

version = '0.1.1'
release = '0.1.1'
exclude_patterns = ['_build']
default_role = 'obj'
pygments_style = 'sphinx'

#intersphinx_mapping = {
#    'python': ('http://python.readthedocs.io/en/latest/', None),
#    'django': ('http://django.readthedocs.io/en/1.8.x/', None),
#    'sphinx': ('http://sphinx.readthedocs.io/en/latest/', None),
#}
htmlhelp_basename = 'OpenStreetTangibledoc'
latex_documents = [
    ('index', 'OpenStreetTangible.tex', u'OpenStreetTangible Documentation',
     u'BrailleRap Team / MyHuman Kit', 'manual'),
]

#man_pages = [
#    ('index', 'read-the-docs', u'Read the Docs Documentation',
#     [u'Eric Holscher, Charlie Leifer, Bobby Grace'], 1)
#]

exclude_patterns = [
    # 'api' # needed for ``make gettext`` to not die.
]

language = 'fr' 

locale_dirs = [
    'locale/',
]
gettext_compact = False
gettext_uuid = False

html_theme = 'sphinx_rtd_theme'
#html_static_path = ['_static']
#html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
#html_theme_path = ["_themes"]
#html_logo = 'IMG/logo.svg' 

html_theme_options = {
    'logo_only': False,
    'display_version': True,
}


def setup(app):
    #app.add_stylesheet('css/custom.css')
    app.add_css_file('css/custom.css')
    app.add_config_value('google-site-test', '', 'html')
    app.connect('html-page-context', add_google_tag)
    


def add_google_tag(app, pagename, templatename, context, doctree):
    metatag = '<meta name="google-site-verification" content="ZMkdTv3yP7NWK3wqkQMwbT6tY_VjSnMPlmmi_CfZhbE" />'
    
    context['metatags'] = context.get('metatags', '') + metatag


