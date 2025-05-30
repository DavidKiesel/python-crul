#   -*- coding: utf-8 -*-

##############################################################################
# copyrights and license
#
# Copyright (c) 2025 David Harris Kiesel
#
# Licensed under the MIT License. See LICENSE in the project root for license
# information.
##############################################################################

##############################################################################
# build.py documentation:
#
# PyBuilder usage documentation at https://pybuilder.io/documentation/manual.

##############################################################################
# Imports.

from pybuilder.core import (
    Author,
    before,
    init,
    task,
    use_bldsup,
    use_plugin,
)

# bldsup
# https://pybuilder.io/documentation/plugins#additional-project-structure
use_bldsup(
    build_support_dir='bldsup'
)
import build_util

##############################################################################
# Plugins.
#
# https://pybuilder.io/documentation/plugins

use_plugin('python.core')
use_plugin('python.install_dependencies')
use_plugin('python.flake8')
use_plugin('python.unittest')
#use_plugin('python.integrationtest')
use_plugin('python.coverage')
use_plugin('python.distutils')
# Sphinx plugin created API documentation for `python.dhk.crul`
# instead of `dhk.crul` so not using it.
# https://www.sphinx-doc.org/en/master/
# use_plugin('python.sphinx')

##############################################################################
# Project attributes set as global variables.
#
# Note that, while the PyBuilder documentation indicates that project
# attributes can be set as global variables or as `project` instance attributes
# within an initializer function, the naming of the Python package distribution
# files does not work correctly by default as of PyBuilder version 0.13.15
# unless `name` and `version` are set as global variables.  See
# https://github.com/pybuilder/pybuilder/issues/646.

# Sets setup.py `name` variable.
name = 'dhk.crul'

# Sets setup.py `version` variable.
# https://packaging.python.org/guides/distributing-packages-using-setuptools/#choosing-a-versioning-scheme
# https://www.python.org/dev/peps/pep-0440/
version = '1.0.0.dev'

##############################################################################
# Functions.

@init
def initialize(project):
    """
    Initialize the project.

    Project attributes can be set as global variables or as attributes of the
    `project` object.
    """

    # A `str` or `list[str]`.
    project.default_task = \
        (
            'clean',
            'publish',
        )

    # Sets setup.py variable description.
    project.summary = \
        'A dumb cURL impostor to illustrate Python development.' 

    # Sets setup.py variable long_description.
    project.description = """
    A dumb cURL impostor to illustrate Python development.
    """

    # Sets setup.py variable author and author_email.
    project.authors = \
        (
            Author(
                'David Harris Kiesel',
                'david.sw@suddenthought.net'
            ),
        )

    # Sets setup.py variable maintainer and maintainer_email.
    project.maintainers = \
        (
            Author(
                'David Harris Kiesel',
                'david.sw@suddenthought.net'
            ),
        )

    # Sets setup.py variable license.
    # See:
    # * https://choosealicense.com/
    # * https://spdx.org/licenses/
    project.license = 'MIT'

    # Sets setup.py variable url.
    project.url = 'https://github.com/DavidKiesel/python-crul'

    # Sets setup.py variable project_urls.
    project.urls = \
        {
            'Homepage': 'https://github.com/DavidKiesel/python-crul',
        }

    # Sets setup.py variable namespace_packages.
    # project.explicit_namespaces = \
    #     (
    #         'EXPLICIT_NAMESPACES_1',
    #         'EXPLICIT_NAMESPACES_2',
    #     )

    # Sets setup.py variable python_requires.
    project.requires_python = '>=3.8'

    # Sets setup.py variable obsoletes.
    # project.obsoletes = \
    #     (
    #         'OBSOLETES_1',
    #         'OBSOLETES_2',
    #     )

@init
def set_properties(
    project
):
    ##########################################################################
    # install_dependencies plugin properties
    #
    # https://pybuilder.io/documentation/plugins

    project.depends_on_requirements(
        'requirements.txt'
    )

    project.depends_on_requirements(
        'requirements-dev.txt'
    )

    ##########################################################################
    # flake8 plugin properties
    #
    # https://pybuilder.io/documentation/plugins

    project.set_property(
        'flake8_include_test_sources',
        True
    )

    ##########################################################################
    # coverage plugin properties
    #
    # https://pybuilder.io/documentation/plugins

    # project.set_property(
    #     'coverage_break_build',
    #     False
    # )

    ##########################################################################
    # distutils plugin properties
    #
    # https://pybuilder.io/documentation/plugins

    # sets setup.py variable classifiers
    # https://pypi.org/classifiers/
    project.set_property(
        'distutils_classifiers',
        (
            'Development Status :: 3 - Alpha',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
            'Programming Language :: Python :: 3.11',
            'Programming Language :: Python :: 3.12',
            'Programming Language :: Python :: 3.13',
        )
    )

# https://pybuilder.io/documentation/writing-plugins
@task(
    description='Example of a custom task.'
)
def some_task(
    project,
    logger
):
    build_util.execute_some_build_function(
        project,
        logger,
        'Hello, build.'
    )

    build_util.execute_some_build_function(
        project,
        logger,
        ", ".join([author.name for author in project.authors])
    )

    build_util.execute_some_build_function(
        project,
        logger,
        project.get_property('sphinx_doc_author')
    )

    build_util.execute_some_build_function(
        project,
        logger,
        project.get_property('sphinx_project_name')
    )

    build_util.execute_some_build_function(
        project,
        logger,
        project.expand_path("$dir_source_main_python")
    )
