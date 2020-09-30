import unittest
from user import User


class TestUser(unittest.TestCase):
    def test_convert_data(self):
        self.assertEqual(User.convert_data('1-1-1'), '0001-01-01')
        self.assertEqual(User.convert_data('2020-12-12'), '2020-12-12')
        self.assertEqual(User.convert_data('0020-01-3'), '0020-01-03')
        self.assertEqual(User.convert_data('202-1-03'), '0202-01-03')
        self.assertEqual(User.convert_data('80-12-1'), '0080-12-01')
        self.assertEqual(User.convert_data('0-2-01'), '0000-02-01')
        self.assertEqual(User.convert_data('080-12-1'), '0080-12-01')
        self.assertEqual(User.convert_data('080-2-1'), '0080-02-01')
        self.assertEqual(User.convert_data('80-2-1'), '0080-02-01')
        self.assertEqual(User.convert_data('12-12-3'), '0012-12-03')

    def test_find(self):
        self.assertEqual(User.convert_find([('022-1-24', 'do C++', '1'), ('022-1-24', 'do Golang', '1'),
                                            ('022-1-24', 'do SQL', '1')]), ['do C++', 'do Golang', 'do SQL'])
        inp = [('2010-11-4', 'do python and do washing up', '1'), ('2010-11-4', 'just do it, ok?', '1'), ('2010-11-4', 'buy bicycle', '1')]
        out = ['do python and do washing up', 'just do it, ok?', 'buy bicycle']
        self.assertEqual(User.convert_find(inp), sorted(out))
        inp = [('1-1-1', 'kek', '1'), ('1-1-1', 'lol', '1'), ('1-1-1', '-_-', '1')]
        out = ['kek', 'lol', '-_-']
        self.assertEqual(User.convert_find(inp), sorted(out))
        inp = [('12-12-1', 'c', '1'), ('12-12-1', 'a', '1'), ('12-12-1', 'b', '1')]
        out = ['a', 'b', 'c']
        self.assertEqual(User.convert_find(inp), out)
        inp = [('131', 'c', '1')]
        out = ['c']
        self.assertEqual(User.convert_find(inp), out)
        inp = [('date', 'c', '1'), ('date', '0', '1'), ('date', 'a', '1')]
        out = ['0', 'a', 'c']
        self.assertEqual(User.convert_find(inp), out)
        inp = [('date', 'cz', '1'), ('date', 'c', '1'), ('date', '0', '1'), ('date', 'a', '1')]
        out = ['0', 'a', 'c', 'cz']
        self.assertEqual(User.convert_find(inp), out)

    def test_format_all(self):
        inp = [('1', 'b'), ('3', 'z'), ('2', 'a')]
        out = {'1': ['b'], '3': ['z'], '2': ['a']}
        self.assertEqual(User.format_all(inp), out)
        inp = [('1', 'b'), ('1', 'a'), ('2', 'a')]
        out = {'1': ['a', 'b'], '2': ['a']}
        self.assertEqual(User.format_all(inp), out)
        inp = [('1', 'b'), ('1', 'a'), ('2', 'a'), ('1', 'c')]
        out = {'1': ['a', 'b', 'c'], '2': ['a']}
        self.assertEqual(User.format_all(inp), out)
        inp = [('1', 'b'), ('1', 'a'), ('2', 'a'), ('1', 'c'), ('2', '1')]
        out = {'1': ['a', 'b', 'c'], '2': ['1', 'a']}
        self.assertEqual(User.format_all(inp), out)
        inp = [('1', 'b'), ('5', 'a'), ('2', 'a'), ('1', 'c'), ('2', '1')]
        out = {'1': ['b', 'c'], '2': ['1', 'a'], '5': ['a']}
        self.assertEqual(User.format_all(inp), out)
        inp = [('1', 'b1234 wdc'), ('5', 'a'), ('2', 'a'), ('1', 'c'), ('2', '1')]
        out = {'1': ['b1234 wdc', 'c'], '2': ['1', 'a'], '5': ['a']}
        self.assertEqual(User.format_all(inp), out)
        inp = [('1', 'b1234 wdc'), ('5', 'a'), ('2', 'a'), ('1', 'c'), ('2', '1'), ('5', '0')]
        out = {'1': ['b1234 wdc', 'c'], '2': ['1', 'a'], '5': ['0', 'a']}
        self.assertEqual(User.format_all(inp), out)
        inp = [('1', 'b')]
        out = {'1': ['b']}
        self.assertEqual(User.format_all(inp), out)


if __name__ == '__main__':
    unittest.main()