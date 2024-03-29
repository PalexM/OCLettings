# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
import django

django.setup()
sys.path.insert(0, os.path.abspath(".."))

os.environ["DJANGO_SETTINGS_MODULE"] = "oc_lettings_site.settings"


project = "OC Lettings"
copyright = "2024, Alexandru Pop"
author = "Alexandru Pop"
release = "1.0"


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",  # Adaugă linkuri către codul sursă
    "sphinx.ext.todo",  # Permite inserarea de TODO-uri în documentație
    "sphinx.ext.intersphinx",  # Permite legături între documentații diferite Sphinx
    "sphinx.ext.autosummary",  # Generează sumare automate; opțional
    "sphinx.ext.napoleon",  # Suport pentru Google style docstrings
]


templates_path = ["_templates"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]
