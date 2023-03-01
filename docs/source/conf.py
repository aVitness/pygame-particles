# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
import re
import sys

sys.path.insert(0, os.path.abspath("../.."))
# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Pygame Particles'
copyright = '2023, Vitness'
author = 'Vitness'
with open("../../pyproject.toml") as file:
    release = re.search(r'version = "([\d.]+)"', file.read()).group(1)
# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc'
]

autodoc_member_order = 'bysource'
templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sizzle'
html_static_path = ['_static']
