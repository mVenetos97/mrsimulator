# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config
# -- Path setup --------------------------------------------------------------
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import textwrap

sys.path.insert(0, os.path.abspath("../.."))
# sys.path.insert(0, os.path.dirname(os.path.abspath(".")))
# sys.path.insert(0, os.path.abspath("../.."))

# curr_dir = os.path.abspath(os.path.dirname(__file__))
# path_to_static = os.path.join(curr_dir, "_build", "_static")


# -- Project information -----------------------------------------------------

project = "mrsimulator"
copyright = "2019, Deepansh J. Srivastava"
author = "Deepansh J. Srivastava"

# The short X.Y version
version = "0.1"
# The full version, including alpha/beta/rc tags
release = "0.1.1a0"


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = "2.0"

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.coverage",
    "sphinx.ext.mathjax",
    "sphinx.ext.githubpages",
    "sphinx.ext.autosummary",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    # "autoapi.extension",
    "breathe",
    "exhale",
    "sphinxjp.themes.basicstrap",
]

# autodoc mock modules
autodoc_mock_imports = ["astropy", "matplotlib", "numba"]

# Setup the breathe extension
breathe_projects = {"My Project": "./doxyoutput/xml"}
breathe_default_project = "My Project"
breathe_domain_by_extension = {"h": "c", "py": "py"}
breathe_use_project_refids = True

# Setup the exhale extension
exhale_args = {
    # These arguments are required
    "containmentFolder": "./api_c",
    "rootFileName": "c_api.rst",
    "rootFileTitle": "C-API References",
    "afterTitleDescription": textwrap.dedent(
        """
       .. note::

           The following documentation presents the C-API.  The Python API
           generally mirrors the C-API, but some methods may not be available in
           Python or may perform different actions.
    """
    ),
    "doxygenStripFromPath": ".",
    # Suggested optional arguments
    "createTreeView": True,
    # TIP: if using the sphinx-bootstrap-theme, you need
    # "treeViewIsBootstrap": True,
    "exhaleExecutesDoxygen": True,
    "exhaleDoxygenStdin": "INPUT = ../mrsimulator/scr/include",
}

# Tell sphinx what the primary language being documented is.
primary_domain = "py"

# Tell sphinx what the pygments highlight language should be.
highlight_language = "c"

# autoapi_dirs = ["../mrsimulator/"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**.ipynb_checkpoints"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# Some html_theme options are 'alabaster', 'bootstrap', 'sphinx_rtd_theme',
# 'classic', 'basicstrap'
html_theme = "basicstrap"


# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    # Set the lang attribute of the html tag. Defaults to 'en'
    "lang": "en",
    # Disable showing the sidebar. Defaults to 'false'
    "nosidebar": False,
    # Show header searchbox. Defaults to false. works only "nosidebar=True",
    "header_searchbox": True,
    # Put the sidebar on the right side. Defaults to false.
    "rightsidebar": False,
    # Set the width of the sidebar. Defaults to 3
    "sidebar_span": 3,
    # Fix navbar to top of screen. Defaults to true
    "nav_fixed_top": True,
    # Fix the width of the sidebar. Defaults to false
    "nav_fixed": False,
    # Set the width of the sidebar. Defaults to '900px'
    "nav_width": "900px",
    # Fix the width of the content area. Defaults to false
    "content_fixed": False,
    # Set the width of the content area. Defaults to '900px'
    "content_width": "900px",
    # Fix the width of the row. Defaults to false
    "row_fixed": True,
    # Disable the responsive design. Defaults to false
    "noresponsive": False,
    # Disable the responsive footer relbar. Defaults to false
    "noresponsiverelbar": False,
    # Disable flat design. Defaults to false.
    # Works only "bootstrap_version = 3"
    "noflatdesign": False,
    # Enable Google Web Font. Defaults to false
    "googlewebfont": True,
    # Set the URL of Google Web Font's CSS.
    # Defaults to 'http://fonts.googleapis.com/css?family=Text+Me+One'
    # "googlewebfont_url": "http://fonts.googleapis.com/css?family=Lily+Script+One",  # NOQA
    # Set the Style of Google Web Font's CSS.
    # Defaults to "font-family: 'Text Me One', sans-serif;"
    "googlewebfont_style": u"font-family: 'Roboto' Regular 24;",
    # Set 'navbar-inverse' attribute to header navbar. Defaults to false.
    "header_inverse": True,
    # Set 'navbar-inverse' attribute to relbar navbar. Defaults to false.
    "relbar_inverse": True,
    # Enable inner theme by Bootswatch. Defaults to false
    "inner_theme": False,
    # Set the name of inner theme. Defaults to 'bootswatch-simplex'
    "inner_theme_name": "bootswatch-simplex",
    # Select Twitter bootstrap version 2 or 3. Defaults to '3'
    "bootstrap_version": "3",
    # Show "theme preview" button in header navbar. Defaults to false.
    "theme_preview": True,
    # Set the Size of Heading text. Defaults to None
    # "h1_size": "3.0em",
    # "h2_size": "2.6em",
    # "h3_size": "2.2em",
    # "h4_size": "1.8em",
    # "h5_size": "1.4em",
    # "h6_size": "1.1em",
}

# Theme options
html_logo = "_static/csdmpy.png"

html_context = {
    "display_github": True,
    "github_user": "DeepanshS",
    "github_repo": "mrsimulator",
    "github_version": "master/docs/",
    "css_files": [
        "_static/button.css",
        #     "_static/theme_overrides.css",  # override wide tables in RTD theme
        #     "_static/style.css",
        #     "_static/custom.css",
        #     "_static/bootstrap-toc.css",
    ],
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]


# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "MRSimulatordoc"


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    "papersize": "letterpaper",
    # The font size ('10pt', '11pt' or '12pt').
    #
    "pointsize": "10pt",
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    "figure_align": "htbp",
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        "mrsimulator.tex",
        "mrsimulator Documentation",
        "Deepansh J. Srivastava",
        "manual",
    )
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "mrsimulator", "mrsimulator Documentation", [author], 1)]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "mrsimulator",
        "mrsimulator Documentation",
        author,
        "mrsimulator",
        "Toolbox for simulating NMR spectrum.",
        "Miscellaneous",
    )
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ["search.html"]


# -- Extension configuration -------------------------------------------------


# def setup(app):
#     app.add_javascript("_static/copybutton.js")
#     app.add_javascript("_static/jquery.js")
