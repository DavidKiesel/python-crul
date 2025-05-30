#   -*- coding: utf-8 -*-

##############################################################################
# copyrights and license
#
# Copyright (c) 2020 David Harris Kiesel
#
# Licensed under the MIT License. See LICENSE in the project root for license
# information.
##############################################################################

##############################################################################
# file information
#
# https://pybuilder.io/documentation/plugins#additional-project-structure

def execute_some_build_function(
    project,
    logger,
    some_arg
):
    """
    An example of a function available through Pybuilder's bldsup feature.

    Positional arguments:

    project  -- PyBuilder project variable.
    logger   -- PyBuilder logger variable.
    some_arg -- Some argument.
    """

    logger.info(
        f'execute_some_build_function:project.name: {project.name}'
    )

    logger.info(
        f'execute_some_build_function:some_arg: {some_arg}'
    )
