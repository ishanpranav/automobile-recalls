# test_nelta.py
# Licensed under the MIT license.

from unittest import TestCase, main

from nelta import LabeledList, read_csv

class TestLabeledList(TestCase):
    def test_composite1(self):
        t = read_csv('data/fruitarians.csv')
        x = """first                last weekly_fruits_eaten           fav_color
0                 abe               apple                 0.0                 red
1                 bob              banana                 4.0              yellow
2               carol             coconut               100.0               white
"""
        self.assertEqual(str(t.head(3)), x)
        
    def test_composite2(self):
        t = read_csv('data/fruitarians.csv')

        self.assertEqual(t[t['last'] == 'apple'].shape()[0], 2)
        
    def test_composite3(self):
        t = read_csv('data/fruitarians.csv')
        x = """first weekly_fruits_eaten
2               carol               100.0
4                 eve                20.0
6                 ann                23.0
"""
        y = t[t['weekly_fruits_eaten'] > 10][[ 'first', 'weekly_fruits_eaten' ]]
        
        self.assertEqual(y, x)
        
    def test_composite4(self):
        t = read_csv('data/fruitarians.csv')
        
        def lengthLessThan(n):
            def isLengthLessThanN(s):
                return len(s) < n
            return isLengthLessThanN
        
        shortFirstName = t[t['first'].map(lengthLessThan(4))]
        shortFirstName[shortFirstName['weekly_fruits_eaten'] < 10]

    def test_labeledListInit1(self):
        l = LabeledList([ 'foo', 'bar', 'baz' ])
        x = """0 foo
1 bar
2 baz
"""
        self.assertEqual(str(l), x)
        self.assertEqual(l.index, [ 0, 1, 2 ])
    
    def test_labeledListInit2(self):
        l = LabeledList([ 1, 2, 3, 4, 5 ], [ 'A', 'BB', 'BB', 'CCC', 'D' ])
        x = """  A 1
 BB 2
 BB 3
CCC 4
  D 5
"""
        self.assertEqual(str(l), x)
    
    def test_labeledListStr(self):
        l = LabeledList([ 1, 2, 3, 4, 5 ], [ 'A', 'BB', 'BB', 'CCC', 'D' ])
        x = """  A 1
 BB 2
 BB 3
CCC 4
  D 5
"""
        self.assertEqual(str(l), x)
        
    def test_labeledListGetItem1(self):
        l = LabeledList([ 1, 2, 3, 4, 5 ], [ 'A', 'BB', 'BB', 'CCC', 'D' ])
        x = """ A 1
BB 2
BB 3
"""
        y = l[LabeledList([ 'A', 'BB' ])]
        
        self.assertEqual(type(y), LabeledList)
        self.assertEqual(str(y), x)
        
    def test_labeledListGetItem2(self):
        l = LabeledList([ 1, 2, 3, 4, 5 ], [ 'A', 'BB', 'BB', 'CCC', 'D' ])
        x = """ A 1
BB 2
BB 3
"""
        y = l[[ 'A', 'BB' ]]
        
        self.assertEqual(type(y), LabeledList)
        self.assertEqual(str(y), x)
        
    def test_labeledListGetItem3(self):
        l = LabeledList([ 1, 2, 3, 4, 5 ], [ 'A', 'BB', 'BB', 'CCC', 'D' ])
        x = """CCC 4
  D 5
"""
        y = l[[ False, False, False, True, True ]]
        
        self.assertEqual(type(y), LabeledList)
        self.assertEqual(str(y), x)
    
    def test_labeledListGetItem4(self):
        l = LabeledList([ 1, 2, 3, 4, 5 ], [ 'A', 'BB', 'BB', 'CCC', 'D' ])
        y = l['A']
        
        self.assertEqual(type(y), int)
        self.assertEqual(y, 1)
        
    def test_labeledListGetItem5(self):
        l = LabeledList([ 1, 2, 3, 4, 5 ], [ 'A', 'BB', 'BB', 'CCC', 'D' ])
        x = """BB 2
BB 3
"""
        y = l['BB']
        
        self.assertEqual(type(y), LabeledList)
        self.assertEqual(str(y), x)
        
    def test_labeledListIter(self):
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
    
    def test_labeledListGt1(self):
        y = LabeledList([ 0, 1, 2, 3, 4 ]) > 2
        x = """0 False
1 False
2 False
3  True
4  True
"""
        self.assertEqual(type(y), LabeledList)
        self.assertEqual(str(y), x)
        
    def test_labeledListGt2(self):
        y = LabeledList([None, 0, 2]) > 1
        x = """0 False
1 False
2  True
"""
        self.assertEqual(type(y), LabeledList)
        self.assertEqual(str(y), x)

    def test_labeledListEq1(self):
        y = LabeledList([ 1, 2 ], [ 'x', 'y' ]) == 1
        x = """x  True
y False
"""
        self.assertEqual(type(y), LabeledList)
        self.assertEqual(str(y), x)

    def test_labeledListEq2(self):
        y = LabeledList(['a', 'b', 'c', 'b', 'b']) == 'b'
        x = """0 False
1  True
2 False
3  True
4  True
"""
        self.assertEqual(type(y), LabeledList)
        self.assertEqual(str(y), x)
        
    def test_labeledListMap(self):
        def squared(n):
            return n ** 2
        
        y = LabeledList([5, 6, 7]).map(squared)
        x = """0 25
1 36
2 49
"""
        self.assertEqual(type(y), LabeledList)
        self.assertEqual(str(y), x)

if __name__ == '__main__':
    main()
