# test_nelta.py
# Licensed under the MIT license.

from unittest import TestCase, main

from nelta import LabeledList, Table, read_csv

class TestNelta(TestCase):
    def test_read_csv1(self):
        t = read_csv('data/fruitarians.csv')
        x = """first                last weekly_fruits_eaten           fav_color
0                 abe               apple                 0.0                 red
1                 bob              banana                 4.0              yellow
2               carol             coconut               100.0               white
"""
        self.assertEqual(str(t.head(3)), x)
        
    def test_read_csv2(self):
        t = read_csv('data/fruitarians.csv')

        self.assertEqual(t[t['last'] == 'apple'].shape()[0], 2)
        
    def test_read_csv3(self):
        t = read_csv('data/fruitarians.csv')
        x = """first weekly_fruits_eaten
2               carol               100.0
4                 eve                20.0
6                 ann                23.0
"""
        y = t[t['weekly_fruits_eaten'] > 10][[ 'first', 'weekly_fruits_eaten' ]]
        
        self.assertEqual(y, x)
        
    def test_read_csv4(self):
        t = read_csv('data/fruitarians.csv')
        
        def lengthLessThan(n):
            def isLengthLessThanN(s):
                return len(s) < n
            return isLengthLessThanN
        
        shortFirstName = t[t['first'].map(lengthLessThan(4))]
        shortFirstName[shortFirstName['weekly_fruits_eaten'] < 10]

class TestLabeledList(TestCase):
    def test_init1(self):
        l = LabeledList([ 'foo', 'bar', 'baz' ])
        x = """0 foo
1 bar
2 baz
"""
        self.assertEqual(str(l), x)
        self.assertEqual(l.index, [ 0, 1, 2 ])
    
    def test_init2(self):
        l = LabeledList([ 1, 2, 3, 4, 5 ], [ 'A', 'BB', 'BB', 'CCC', 'D' ])
        x = """  A 1
 BB 2
 BB 3
CCC 4
  D 5
"""
        self.assertEqual(str(l), x)
    
    def test_str(self):
        l = LabeledList([ 1, 2, 3, 4, 5 ], [ 'A', 'BB', 'BB', 'CCC', 'D' ])
        x = """  A 1
 BB 2
 BB 3
CCC 4
  D 5
"""
        self.assertEqual(str(l), x)
        
    def test_getitem1(self):
        l = LabeledList([ 1, 2, 3, 4, 5 ], [ 'A', 'BB', 'BB', 'CCC', 'D' ])
        x = """ A 1
BB 2
BB 3
"""
        y = l[LabeledList([ 'A', 'BB' ])]
        
        self.assertEqual(type(y), LabeledList)
        self.assertEqual(str(y), x)
        
    def test_getitem2(self):
        l = LabeledList([ 1, 2, 3, 4, 5 ], [ 'A', 'BB', 'BB', 'CCC', 'D' ])
        x = """ A 1
BB 2
BB 3
"""
        y = l[[ 'A', 'BB' ]]
        
        self.assertEqual(type(y), LabeledList)
        self.assertEqual(str(y), x)
        
    def test_getitem3(self):
        l = LabeledList([ 1, 2, 3, 4, 5 ], [ 'A', 'BB', 'BB', 'CCC', 'D' ])
        x = """CCC 4
  D 5
"""
        y = l[[ False, False, False, True, True ]]
        
        self.assertEqual(type(y), LabeledList)
        self.assertEqual(str(y), x)
    
    def test_getitem4(self):
        l = LabeledList([ 1, 2, 3, 4, 5 ], [ 'A', 'BB', 'BB', 'CCC', 'D' ])
        y = l['A']
        
        self.assertEqual(type(y), int)
        self.assertEqual(y, 1)
        
    def test_getitem5(self):
        l = LabeledList([ 1, 2, 3, 4, 5 ], [ 'A', 'BB', 'BB', 'CCC', 'D' ])
        x = """BB 2
BB 3
"""
        y = l['BB']
        
        self.assertEqual(type(y), LabeledList)
        self.assertEqual(str(y), x)
        
    def test_iter(self):
        l = LabeledList([ 1, 2, 3, 4, 5 ], [ 'A', 'BB', 'BB', 'CCC', 'D' ])
        y = ""
        
        for value in l:
            y += str(value) + "\n"
            
        x = """1
2
3
4
5
"""
        self.assertEqual(y, x)
    
    def test_gt1(self):
        y = LabeledList([ 0, 1, 2, 3, 4 ]) > 2
        x = """0 False
1 False
2 False
3  True
4  True
"""
        self.assertEqual(type(y), LabeledList)
        self.assertEqual(str(y), x)
        
    def test_gt2(self):
        y = LabeledList([None, 0, 2]) > 1
        x = """0 False
1 False
2  True
"""
        self.assertEqual(type(y), LabeledList)
        self.assertEqual(str(y), x)

    def test_eq1(self):
        y = LabeledList([ 1, 2 ], [ 'x', 'y' ]) == 1
        x = """x  True
y False
"""
        self.assertEqual(type(y), LabeledList)
        self.assertEqual(str(y), x)

    def test_eq2(self):
        y = LabeledList([ 'a', 'b', 'c', 'b', 'b' ]) == 'b'
        x = """0 False
1  True
2 False
3  True
4  True
"""
        self.assertEqual(type(y), LabeledList)
        self.assertEqual(str(y), x)
        
    def test_map(self):
        def squared(n):
            return n ** 2
        
        y = LabeledList([ 5, 6, 7 ]).map(squared)
        x = """0 25
1 36
2 49
"""
        self.assertEqual(type(y), LabeledList)
        self.assertEqual(str(y), x)

class TestTable(TestCase):
    def test_init1(self):
        t = Table([[ 'foo', 'bar', 'baz' ], [ 'qux', 'quxx', 'corge' ]])
        x = """    0    1     2
0  foo  bar   baz
1  qux quxx corge
"""
        self.assertEqual(str(t), x)
        
    def test_init2(self):    
        d = [
            [ 1000, 10, 100, 1, 1.0 ],
            [ 200, 2, 2.0, 2000, 20 ],
            [ 3, 300, 3000, 3.0, 30 ],
            [ 40, 4000, 4.0, 400, 4 ],
            [ 7, 8, 6, 3, 41 ]
        ]
        t = Table(
            d, 
            [ 'foo', 'bar', 'bazzy', 'qux', 'quxx' ], 
            [ 'a', 'b', 'c', 'd', 'e' ])
        x = """         a    b    c    d   e
  foo  1000   10  100    1 1.0
  bar   200    2  2.0 2000  20
bazzy     3  300 3000  3.0  30
  qux    40 4000  4.0  400   4
 quxx     7    8    6    3  41
"""
        self.assertEqual(str(t), x)
        
    def test_str(self):
        t = Table([ [ 'foo', 'bar', 'baz' ], [ 'qux', 'quxx', 'corge' ] ])
        x = """    0    1     2
0  foo  bar   baz
1  qux quxx corge
"""
        self.assertEqual(str(t), x)
        
    def test_getitem1(self):
        d = [
            [ 1000, 10, 100, 1, 1.0 ],
            [ 200, 2, 2.0, 2000, 20 ],
            [ 3, 300, 3000, 3.0, 30 ],
            [ 40, 4000, 4.0, 400, 4 ],
            [ 7, 8, 6, 3, 41 ]
        ]
        t = Table(
            d, 
            [ 'foo', 'bar', 'bazzy', 'qux', 'quxx' ], 
            [ 'a', 'b', 'c', 'd', 'e' ])
        y = t[LabeledList([ 'a', 'b' ])]
        x = """a    b
  foo 1000   10
  bar  200    2
bazzy    3  300
  qux   40 4000
 quxx    7    8
"""
        self.assertEqual(type(y), Table)
        self.assertEqual(str(y), x)
        
    def test_getitem2(self):
        columns = [ 'x', 'y', 'z' ]
        t = Table([ [ 15, 17, 19 ], [ 14, 16, 18 ] ], columns = columns)
        y = t[[ 'x', 'x', 'y' ]]
        x = """   x  x  y
0 15 15 17
1 14 14 16
"""        
        self.assertEqual(type(y), Table)
        self.assertEqual(str(y), x)
        
    def test_getitem3(self):
        columns = [ 'x', 'y', 'z' ]
        t = Table([[1, 2, 3], [4, 5, 6], [7, 8 , 9]], columns = columns)
        y = t[[ True, False, True ]]
        x = """  x y z
0  1 2 3
2  7 8 9
"""
        self.assertEqual(type(y), Table)
        self.assertEqual(str(y), x)

    def test_getitem4(self):
        t = Table([ [ 1, 2, 3 ], [ 4, 5, 6 ] ], columns = [ 'a', 'b', 'a' ])
        y = t['b']
        x = """0 2
1 5
"""
        self.assertEqual(type(y), LabeledList)
        self.assertEqual(str(y), x)
    
    def test_getitem5(self):
        t = Table([ [ 1, 2, 3 ], [ 4, 5, 6 ] ], columns = [ 'a', 'b', 'a' ])
        y = t['a']
        x = """  a a
0  1 3
1  4 6"""
        self.assertEqual(type(y), Table)
        self.assertEqual(str(y), x)
        
if __name__ == '__main__':
    main()
