# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'RTD-test'
copyright = '2022, Seongbin Ga'
author = 'Seongbin Ga'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []


import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output


#html_theme = 'alabaster'
html_theme ='sphinx_rtd_theme'
html_static_path = ['_static']
extensions = [
        'myst_parser',
        'sphinx.ext.autodoc',
        'sphinx.ext.mathjax',
        'sphinx.ext.autosummary',
        #'sphinx.ext.doctest',
        'sphinx.ext.intersphinx',
        'sphinx.ext.todo',
        'sphinx.ext.coverage',
        'sphinx.ext.napoleon',
        'sphinx.ext.viewcode',
        'sphinx.ext.githubpages',
        #'recommonmark',
        ]
source_suffix = {
        '.rst': 'restructuredtext',
        '.txt': 'markdown',
        '.md': 'markdown',
        }

