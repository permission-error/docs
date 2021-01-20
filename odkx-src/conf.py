#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# ODK-X documentation build configuration file, created by
# sphinx-quickstart on Wed May 24 09:46:59 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('../'))
import video

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx_tabs.tabs',
    'sphinxcontrib.spelling',
    'video']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'ODK-X'
copyright = '2020, ODK-X. This document is licensed under a Creative Commons Attribution 4.0 International License'
author = 'ODK-X'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '1.0'
# The full version, including alpha/beta/rc tags.
# release = '1.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'incl']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'default'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# suppress warnings for unknown options
suppress_warnings = ['ref.option']

# Smart (q)uotes, (D)ashes, and (e)llipses
smartquotes = True
smartquotes_action = 'De'

# Print suggestions for misspelled words.
spelling_show_suggestions = True

# Change image preference for DirectoryHTMLBuilder
from sphinx.builders.html import DirectoryHTMLBuilder
DirectoryHTMLBuilder.supported_image_types = [
    'image/svg+xml',
    'image/gif',
    'image/png',
    'image/jpeg'
]

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add logo stuff
html_logo = '_static/img/logo-wide.png'
html_theme_options = {
    'logo_only': True,
    'display_version': False,
}
html_title = "ODK-X Docs"

html_favicon = "_static/img/favicon.ico"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add paths that contain extra files which are not directly related to the
# documentation and which are copied to the output directory.
# html_extra_path = []

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'ODKXdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    'pointsize': '12pt',

    # Additional stuff for the LaTeX preamble.
    'preamble': r'''
    \usepackage{fontspec}
    \newcommand{\changefont}{%
      \fontsize{8}{10}\selectfont
    }
    \makeatletter
      \fancypagestyle{normal}{
        \fancyhf{}
        \fancyfoot[LE,RO]{{\py@HeaderFamily\thepage}}
        \fancyhead[LO]{{\py@HeaderFamily\nouppercase{\rightmark}}}
        \fancyhead[RE]{{\py@HeaderFamily\nouppercase{\leftmark}}}
        \fancyfoot[CE,CO]{{\changefont{Our documentation is updated frequently. Get the latest version at \href{https://docs.odk-x.org/odk-x}{https://docs.odk-x.org/odk-x}.}}}
        \renewcommand{\headrulewidth}{0.4pt}
        \renewcommand{\footrulewidth}{0.4pt}
      }
      \fancypagestyle{plain}{
        \fancyhf{}
        \fancyfoot[LE,RO]{{\py@HeaderFamily\thepage}}
        \fancyfoot[CE,CO]{{\changefont{Our documentation is updated frequently. Get the latest version at \href{https://docs.odk-x.org/odk-x}{https://docs.odk-x.org/odk-x}.}}}
        \renewcommand{\headrulewidth}{0pt}
        \renewcommand{\footrulewidth}{0.4pt}
      }
    \makeatother
    \renewcommand{\release}{}
    ''',

    # disable font inclusion
    'fontpkg': '',
    'fontenc': '',

    # Fix Unicode handling by disabling the defaults for a few items
    # set by sphinx
    'inputenc': '',
    'utf8extra': '',

    # Latex figure (float) alignment
    'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'ODK-X.tex', 'ODK-X Documentation',
     'ODK-X', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'odkx', 'ODK-X Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'ODK-X', 'ODK-X Documentation',
     author, 'ODK-X', 'One line description of project.',
     'Miscellaneous'),
]



# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']



# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    # 'py': ('https://docs.python.org/', None),
    'odkx': ('https://docs.odk-x.org/', None)
}

# Add custom CSS

def setup(app):
    app.add_css_file('css/custom.css')
    app.add_js_file('js/custom.js')

# At top of every document

rst_prolog="""
.. role:: th
    :class: th

.. role:: tc
    :class: tc

.. role:: formstate
    :class: formstate

.. role:: gesture
    :class: gesture
"""

# At bottom of every document
download_pdf = """

Download this documentation as a PDF.

"""
odkx_pdf = """

_downloads/ODK-X-Documentation.pdf

"""
prob_in_doc = """

If you find a problem with this documentation, please

"""
file_issue = """

file an issue

"""
file_issue_here = """

https://github.com/odk-x/tool-suite-X/issues

"""
contri_start = """

You are also encouraged to

"""
fork_repo = """

fork our Github repo

"""
repo_here = """

https://github.com/odk-x/docs/

"""
join = """

and

"""
contri = """

become a contributor

"""
contri_guide = """

/contributing/

"""
faq_help = """

If you still need help, you can ask support questions in the

"""
forum = """

ODK Forum

"""
forum_here = """

https://forum.odk-x.org/

"""

rst_epilog = """

.. |docs-issue| replace:: issue
.. _docs-issue: https://github.com/odk-x/tool-suite-X/issues

.. |forum| replace:: ODK-X Forum
.. _forum: https://forum.odk-x.org

.. |contrib-guide| replace:: contributors guide
.. _contrib-guide: https://docs.odk-x.org/contributing/

"""

html_context = {'download_pdf' : download_pdf,
                'odkx_pdf' : odkx_pdf,
                'prob_in_doc' : prob_in_doc ,
                'contri_start' : contri_start ,
                'join' : join ,
                'faq_help' : faq_help ,
                'file_issue' : file_issue ,
                'fork_repo' : fork_repo ,
                'contri' : contri ,
                'forum' : forum ,
                'file_issue_here' : file_issue_here ,
                'repo_here' : repo_here ,
                'contri_guide' : contri_guide ,
                'forum_here' : forum_here ,
                'display_github' : True,
                'github_user' : "odk-x", # Username
                'github_repo' : "docs", # Repo name
                'github_version' : "master", # Version
                'conf_py_path' : "/odkx-src/" # Path in the checkout to the docs root
            }
