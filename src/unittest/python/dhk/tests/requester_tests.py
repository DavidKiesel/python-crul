#   -*- coding: utf-8 -*-

##############################################################################
# copyrights and license
#
# Copyright (c) 2025 David Harris Kiesel
#
# Licensed under the MIT License. See LICENSE in the project root for license
# information.
##############################################################################

from string import \
    Template
import unittest
from unittest import \
    TestCase
from unittest.mock import \
    patch

# local
from dhk.crul.requester import \
    RequesterClient
from .requests_mock import \
    MockRequest, \
    MockResponse


class Test(TestCase):
    """
    """

    @patch('dhk.crul.requester.requests')
    def test_static_request(
        self,
        mock_requests
    ):
        ######################################################################
        # prepare

        paramss = \
            [
                {
                    'method': 'GET',
                    'url': 'http://example.com'
                }
            ]

        content_template = \
            Template(
                '''<html>
            <body>
                <p>Response for ${url}.<p>
            </body>
        </html>'''
            )

        ######################################################################
        # test and assert

        for subtest_number in range(0, len(paramss)):
            with self.subTest(
                i=subtest_number
            ):
                params = paramss[subtest_number]

                method = params['method']

                url = params['url']

                content = \
                    content_template.substitute(
                        {
                            'url': url
                        }
                    ).encode()

                mock_responses = \
                    [
                        MockResponse(
                            content
                        )
                    ]

                mock_requests.request = \
                    MockRequest(
                        iter(mock_responses)
                    ).request

                response = \
                    RequesterClient.static_request(
                        method,
                        url,
                    )

                self.assertSequenceEqual(
                    response.content,
                    content,
                    seq_type=bytes
                )


if __name__ == '__main__':
    unittest.main()
