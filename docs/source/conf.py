# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Office of Personnel Management Department LSPD'
copyright = '2025, Office of Personnel Management LSPD'
author = 'Orlando Castello'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser'
]

templates_path = ['_templates']
exclude_patterns = []

language = 'uk_UA'
myst_heading_anchors = 2
# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinxawesome_theme'
html_static_path = ['_static']
html_css_files = ['custom.css']
html_theme_options = {
    "show_prev_next": False,  # Прибрати кнопки "Наступна/Попередня сторінка"
    "show_breadcrumbs": True,  # Відображати навігаційний шлях
}
