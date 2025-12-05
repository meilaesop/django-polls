# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
from pathlib import Path

# 添加项目路径到 sys.path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

# -- 项目信息 -----------------------------------------------------
project = 'django-polls'
copyright = '2025, meilaesop'
author = 'meilaesop'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

#启用 intersphinx 扩展
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    # ...
    "django": (
        "https://docs.djangoproject.com/en/stable/",
        None,
    ),
}

# -- 路径配置 -----------------------------------------------------
templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# -- 主题配置 -----------------------------------------------------
html_theme = 'alabaster'
html_static_path = ['_static']
