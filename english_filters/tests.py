# -*- coding: utf-8 -*-
# (c) 2015 Bright Interactive Limited. All rights reserved.
# http://www.bright-interactive.com | info@bright-interactive.com
from django.utils.unittest import TestCase
from english_filters.templatetags.english_filters import join_or, join_and


class JoinTests(TestCase):
    def test_join_or_empty_list(self):
        self.assertEqual(u'',
                         join_or([]))

    def test_join_or_one_number(self):
        self.assertEqual(u'123',
                         join_or([123]))

    def test_join_or_2_numbers(self):
        self.assertEqual(u'123 or 456',
                         join_or([123, 456]))

    def test_join_or_3_numbers(self):
        self.assertEqual(u'123, 456 or 7',
                         join_or([123, 456, 7]))

    def test_join_or_4_numbers(self):
        self.assertEqual(u'123, 456, 42 or 321',
                         join_or([123, 456, 42, 321]))

    def test_join_or_3_strings(self):
        self.assertEqual(u'Peter, Jane or Mary',
                         join_or(['Peter', 'Jane', 'Mary']))

    def test_join_or_escapes_when_autoescape_true(self):
        self.assertEqual('&lt; or &gt;',
                         join_or(['<', '>'], autoescape=True))

    def test_join_and_escapes_when_autoescape_true(self):
        self.assertEqual('&lt; and &gt;',
                         join_and(['<', '>'], autoescape=True))

    def test_join_and_3_strings(self):
        self.assertEqual(u'Peter, Jane and Mary',
                         join_and(['Peter', 'Jane', 'Mary']))
