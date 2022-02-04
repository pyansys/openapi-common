from ansys.openapi import common
import os
import sys

# -- Project information -----------------------------------------------------

project = "ansys.openapi.common"
copyright = "(c) 2021 ANSYS, Inc. All rights reserved"
author = "ANSYS Inc."
html_title = f"OpenAPI Common {__version__}"

sys.path.insert(0, os.path.abspath("../src"))

# The short X.Y version
release = version = common.__version__

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx_autodoc_typehints",
    "numpydoc",
    "sphinx.ext.doctest",
    "sphinx.ext.autosummary",
    "notfound.extension",
    "sphinx.ext.intersphinx",
    "sphinx_copybutton",
    "sphinx.ext.extlinks",
    "sphinx.ext.coverage",
]

add_module_names = False
typehints_fully_qualified = True
typehints_document_rtype = False

intersphinx_mapping = {
    "python": ("https://docs.python.org/dev", None),
    "requests": ("https://docs.python-requests.org/en/master/", None),
}

# numpydoc configuration
numpydoc_show_class_members = False
numpydoc_xref_param_type = True

# Consider enabling numpydoc validation. See:
# https://numpydoc.readthedocs.io/en/latest/validation.html#
numpydoc_validate = True
numpydoc_validation_checks = {
    "GL06",  # Found unknown section
    "GL07",  # Sections are in the wrong order.
    "GL08",  # The object does not have a docstring
    "GL09",  # Deprecation warning should precede extended summary
    "GL10",  # reST directives {directives} must be followed by two colons
    "SS01",  # No summary found
    "SS02",  # Summary does not start with a capital letter
    # "SS03", # Summary does not end with a period
    "SS04",  # Summary contains heading whitespaces
    # "SS05", # Summary must start with infinitive verb, not third person
    "RT02",  # The first line of the Returns section should contain only the
    # type, unless multiple values are being returned"
}

# static path
html_static_path = ["_static"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
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
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# Copy button customization ---------------------------------------------------
# exclude traditional Python prompts from the copied code
copybutton_prompt_text = r">>> ?|\.\.\. "
copybutton_prompt_is_regexp = True


# -- Options for HTML output -------------------------------------------------
html_theme = "pyansys_sphinx_theme"
html_logo = "./_static/pyansys-logo-black-cropped.png"
html_theme_options = {
    "github_url": "https://github.com/pyansys/openapi-common",
    "show_prev_next": False,
    "show_breadcrumbs": True,
    "additional_breadcrumbs": [
        ("PyAnsys Documentation", "https://docs.pyansys.com"),
        ("Shared Components", "https://shared.docs.pyansys.com")
    ]
}

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "openapicommondoc"


# -- Options for LaTeX output ------------------------------------------------
latex_elements = {}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        "ansys_openapi_common.tex",
        "ansys.openapi.common Documentation",
        author,
        "manual",
    ),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (
        master_doc,
        "ansys.openapi.common",
        "ansys.openapi.common Documentation",
        [author],
        1,
    )
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "ansys.openapi.common",
        "ansys.openapi.common Documentation",
        author,
        "ansys.openapi.common",
        "Common authentication components for pyAnsys REST clients",
        "Engineering Software",
    ),
]
latex_engine = "xelatex"

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
