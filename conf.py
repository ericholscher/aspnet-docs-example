# -*- coding: utf-8 -*-

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'dotnetexample'
copyright = u'2015, rtfd'
author = u'rtfd'
version = '0.1'
release = '0.1'
language = None
exclude_patterns = ['_build']
pygments_style = 'sphinx'
todo_include_todos = False
html_theme = 'sphinx_rtd_theme'
htmlhelp_basename = 'dotnetexampledoc'
extensions = ['autoapi.extension', 'sphinxcontrib.dotnetdomain']

autoapi_type = 'dotnet'
# autoapi_keep_files = False
autoapi_dir = 'example/Identity/src/'
