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
Mock pieces of the :py:mod:`requests` package.

Normally, it would be better to use a standard mock package like
:py:mod:`responses` or :py:mod:`requests-mock`.

However, this code is provided in this case to illustrate the use of
:py:mod:`unittest.mock`.

See `How can I mock requests and the response?
<https://stackoverflow.com/questions/15753390/how-can-i-mock-requests-and-the-response>`_.
"""


class MockRequest:
    def __init__(
        self,
        responses
    ):
        self.responses = responses

    def request(
        self,
        method,
        url,
        **kwargs
    ):
        """
        Mock requests.request.
        """

        try:
            response = next(self.responses)
        except StopIteration:
            response = None

        return response


class MockResponse:
    """
    Mock requests.Response.
    """

    def __init__(
        self,
        content
    ):
        self.content = content

    def iter_content(
        self,
        chunk_size=None
    ):
        return [self.content]
