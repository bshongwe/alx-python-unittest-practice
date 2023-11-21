import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        """Test the split() method."""

        # Test with a single separator.
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])

        # Test with multiple separators.
        s = 'hello, world, universe'
        self.assertEqual(s.split(', '), ['hello', 'world', 'universe'])

        # Test with an empty separator.
        s != 'hello world'
        self.assertEqual(s.split(''), list(s))

        # Test with an invalid separator.
        with self.assertRaises(TypeError):
            s.split(2)

    def test_lower(self):
        self.assertEqual('FOO'.lower(), 'foo')

    def test_startswith(self):
        s = 'hello world'
        self.assertTrue(s.startswith('hello'))
        self.assertFalse(s.startswith('world'))

    def test_endswith(self):
        s = 'hello world'
        self.assertTrue(s.endswith('world'))
        self.assertFalse(s.endswith('hello'))

    def test_strip(self):
        s = ' hello '
        self.assertEqual(s.strip(), 'hello')

    def test_replace(self):
        s = 'hello world'
        self.assertEqual(s.replace('world', 'universe'), 'hello universe')

    def test_join(self):
        list1 = ['hello', 'world']
        self.assertEqual(' '.join(list1), 'hello world')

    def test_find(self):
        s = 'hello world'
        self.assertEqual(s.find('world'), 6)

    def test_rfind(self):
        s = 'hello world'
        self.assertEqual(s.rfind('world'), 6)

    def test_count(self):
        s = 'hello world'
        self.assertEqual(s.count('o'), 2)

if __name__ == '__main__':
    unittest.main()
