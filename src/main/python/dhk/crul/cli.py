#   -*- coding: utf-8 -*-

##############################################################################
# copyrights and license
#
# Copyright (c) 2025 David Harris Kiesel
#
# Licensed under the MIT License. See LICENSE in the project root for license
# information.
##############################################################################

"""
A module for handling command-line interface functionality.
"""

import argparse
import io
import json
import sys

# from this distribution package
from dhk.crul.requester import RequesterClient


def get_binary_writer(
    file_path
):
    # docstring conventions;
    # https://www.python.org/dev/peps/pep-0257/
    # https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#the-python-domain
    """
    Get binary writer.

    Create instance of :py:class:`argparse.FileType` with parameter ``mode``
    set to ``'wb'``.

    Get ``writer`` by calling instance of ``argparse.FileType`` with parameter
    ``file_path``.

    If ``writer`` is instance of :py:class:`io.TextIOWrapper` (``'-'``
    sys.stdout case), then return ``writer.buffer``, which will be an instance
    of :py:class:`io.BufferedWriter`.

    Otherwise, return ``writer``, which will be an instance of
    :py:class:`io.BufferedWriter`.

    :param str file_path: File path.

    :return: A binary writer.
    :rtype: io.BufferedWriter
    """
    writer = \
        argparse.FileType(
            mode='wb'
        )(
            file_path
        )

    if isinstance(
        writer,
        io.TextIOWrapper
    ):
        writer = \
            writer.buffer

    return writer


def get_parser():
    # docstring conventions;
    # https://www.python.org/dev/peps/pep-0257/
    # https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#the-python-domain
    """
    Get parser.

    :return: A parser.
    :rtype: argparse.ArgumentParser
    """

    parser = \
        argparse.ArgumentParser(
            prog='crul',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description="""
A dumb cURL impostor.
""",
            add_help=True,
            epilog="""
Examples:

    %(prog)s 'https://example.com'

    %(prog)s \\
        --output OUTPUT \\
        --headers '{"KEY": "VALUE"}' \\
        'https://example.com'
"""
        )

    # type=argparse.FileType(mode='wb')
    # works for ordinary files but use get_binary_writer
    # to also be able to handle '-' sys.stdout case
    parser.add_argument(
        '--output',
        '-o',
        metavar='OUTPUT',
        type=get_binary_writer,
        default='-',
        help="""
output; default: '-' (standard output)
"""
    )

    parser.add_argument(
        '--headers',
        '-H',
        metavar='HEADERS',
        type=json.loads,
        default='{}',
        help="""
headers in JSON format; default: '{}'
"""
    )

    parser.add_argument(
        'url',
        metavar='URL',
        help="""
URL
"""
    )

    return parser


def main(
    url,
    headers={},
    output=sys.stdout.buffer
):
    # docstring conventions;
    # https://www.python.org/dev/peps/pep-0257/
    # https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#the-python-domain
    """
    Create instance of :class:`.RequesterClient`.

    Send HTTP request using method ``method`` and URL ``url``.

    Write response contents to ``output``.

    :param str url: URL.
    :param dict headers: Headers.
    :param io.BufferedWriter output: Output.
    """

    requester_client = \
        RequesterClient(
            headers=headers
        )

    requester_client.request_and_write(
        'GET',
        url,
        output
    )
