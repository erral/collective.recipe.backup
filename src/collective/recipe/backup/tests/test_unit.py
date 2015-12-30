# -*- coding: utf-8 -*-
import unittest


class UtilsTestCase(unittest.TestCase):

    def test_to_bool(self):
        from collective.recipe.backup import to_bool
        self.assertTrue(to_bool(True))
        self.assertFalse(to_bool(False))
        self.assertFalse(to_bool(None))
        self.assertTrue(to_bool('True'))
        self.assertTrue(to_bool('true'))
        self.assertTrue(to_bool('on'))
        self.assertFalse(to_bool('False'))
        self.assertFalse(to_bool('false'))
        self.assertFalse(to_bool(''))
        self.assertFalse(to_bool('unknown'))
        self.assertFalse(to_bool('0'))
        self.assertTrue(to_bool('1'))
        self.assertFalse(to_bool('10'))
        self.assertFalse(to_bool(0))
        self.assertTrue(to_bool(-1))
        self.assertTrue(to_bool(42))

    def test_check_for_true(self):
        from collective.recipe.backup import check_for_true
        # check_for_true changes the input in place.
        self.assertEqual(check_for_true({}, []), None)
        options = {}
        check_for_true(options, [])
        self.assertEqual(options, {})
        options = {
            'a': 'True',
            'b': 'true',
            'c': 'yes',
            'd': 'on',
            'e': 'False',
            'f': 'false',
            'g': '',
            'h': 'unknown',
            }
        orig_options = options.copy()
        # The result should be a unified capitalized True/False string.
        sanitised_options = {
            'a': 'True',
            'b': 'True',
            'c': 'True',
            'd': 'True',
            'e': 'False',
            'f': 'False',
            'g': 'False',
            'h': 'False',
            }
        # Without keys, nothing is changed.
        check_for_true(options, [])
        self.assertEqual(options, orig_options)
        # With some keys, some is changed.
        check_for_true(options, ['a', 'c'])
        self.assertNotEqual(options, orig_options)
        self.assertNotEqual(options, sanitised_options)
        self.assertEqual(options['a'], 'True')
        self.assertEqual(options['c'], 'True')
        # Without all keys, everything is changed.
        check_for_true(options, options.keys())
        self.assertEqual(options, sanitised_options)
