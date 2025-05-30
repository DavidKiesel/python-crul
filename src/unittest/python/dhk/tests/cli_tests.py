#   -*- coding: utf-8 -*-

##############################################################################
# copyrights and license
#
# Copyright (c) 2025 David Harris Kiesel
#
# Licensed under the MIT License. See LICENSE in the project root for license
# information.
##############################################################################

from io import \
    BufferedWriter, \
    BytesIO
from string import \
    Template
import unittest
from unittest import \
    TestCase
from unittest.mock import \
    patch

# local
from dhk.crul import cli
from .requests_mock import \
    MockRequest, \
    MockResponse


class Test(TestCase):
    def test_get_parser__normal(self):
        ######################################################################
        # prepare

        argvs = \
            [
                [
                    'https://example.com'
                ],
                [
                    '--output',
                    'target/test_get_parser__normal-example.com.html',
                    '--headers',
                    '{"key1": "value1"}',
                    'https://example.com/index.html'
                ]
            ]

        expected_results = \
            [
                [
                    BufferedWriter,
                    '<stdout>',
                    {},
                    'https://example.com'
                ],
                [
                    BufferedWriter,
                    'target/test_get_parser__normal-example.com.html',
                    {
                        'key1': 'value1'
                    },
                    'https://example.com/index.html'
                ]
            ]

        ######################################################################
        # test and assert

        for i in range(0, len(argvs)):
            with self.subTest(
                i=i
            ):
                parser = \
                    cli.get_parser().parse_args(
                        argvs[i]
                    )

                self.assertIsInstance(
                    parser.output,
                    expected_results[i][0]
                )

                self.assertEqual(
                    parser.output.name,
                    expected_results[i][1]
                )

                self.assertDictEqual(
                    parser.headers,
                    expected_results[i][2]
                )

                self.assertEqual(
                    parser.url,
                    expected_results[i][3]
                )

    def test_get_parser__no_such_option(self):
        ######################################################################
        # prepare

        argvs = \
            [
                [],
                ['--no_such_option']
            ]

        expected_results = \
            [
                SystemExit,
                SystemExit
            ]

        ######################################################################
        # test and assert

        for i in range(0, len(argvs)):
            with self.subTest(
                i=i
            ):
                with self.assertRaises(expected_results[i]):
                    cli.get_parser().parse_args(
                        argvs[i]
                    )

    @patch('dhk.crul.requester.requests')
    def test_main(
        self,
        mock_requests
    ):
        ######################################################################
        # prepare

        paramss = \
            [
                {
                    'url': 'http://example.com',
                    'headers': {
                        'key1': 'value1',
                        'key2': 'value2'
                    }
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

                url = params['url']

                headers = params['headers']

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

                with BytesIO() as output:
                    cli.main(
                        url,
                        headers=headers,
                        output=output
                    )

                    self.assertSequenceEqual(
                        output.getvalue(),
                        content,
                        seq_type=bytes
                    )


if __name__ == '__main__':
    unittest.main()
