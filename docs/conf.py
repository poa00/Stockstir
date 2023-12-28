project = 'Stockstir'
copyright = '2023, PatzEdi'
author = 'PatzEdi'

release = '1.0.1'
version = '1.0.1'

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']



html_theme = 'classic'


epub_show_urls = 'footnote'