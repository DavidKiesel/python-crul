#   -*- coding: utf-8 -*-

##############################################################################
# copyrights and license
#
# Copyright (c) 2025 David Harris Kiesel
#
# Licensed under the MIT License. See LICENSE in the project root for license
# information.
##############################################################################

# docstring conventions;
# https://www.python.org/dev/peps/pep-0257/
# https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#the-python-domain
"""
A module for composing and sending HTTP requests and handling responses.
"""

# https://pypi.org/project/requests/
# https://requests.readthedocs.io/
# https://github.com/psf/requests
import requests


class RequesterClient:
    # docstring conventions;
    # https://www.python.org/dev/peps/pep-0257/
    # https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#the-python-domain
    """
    Requester client.
    """

    @staticmethod
    def static_request(
        method,
        url
    ):
        # docstring conventions;
        # https://www.python.org/dev/peps/pep-0257/
        # https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#the-python-domain
        """
        Send HTTP request using method ``method`` and URL ``url``.

        :param str method: Method.
        :param str url: URL.

        :return: An HTTP response.
        :rtype: requests.Response
        """

        requester = \
            RequesterClient()

        response = \
            requester.request(
                method,
                url
            )

        return response

    def __init__(
        self,
        headers={}
    ):
        # docstring conventions;
        # https://www.python.org/dev/peps/pep-0257/
        # https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#the-python-domain
        """
        Constructor.

        :param headers: Headers; a ``dict`` of ``str`` key-value pairs; defaults to ``{}``.
        :type headers: dict, optional
        """

        self.headers = headers

    def request(
        self,
        method,
        url
    ):
        # docstring conventions;
        # https://www.python.org/dev/peps/pep-0257/
        # https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#the-python-domain
        """
        Send HTTP request using method ``method`` and URL ``url``.

        :param str method: Method.
        :param str url: URL.

        :return: An HTTP response.
        :rtype: requests.Response
        """

        response = \
            requests.request(
                method,
                url
            )

        return response

    def request_and_write(
        self,
        method,
        url,
        output
    ):
        # docstring conventions;
        # https://www.python.org/dev/peps/pep-0257/
        # https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#the-python-domain
        """
        Send HTTP request using method ``method`` and URL ``url``.

        Write response contents to ``output``.

        :param str method: Method.
        :param str url: URL.
        :param io.BufferedWriter output: Output.
        """

        response = \
            self.request(
                method,
                url
            )

        for chunk in response.iter_content(chunk_size=128):
            output.write(chunk)
