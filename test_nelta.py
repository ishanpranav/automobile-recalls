# test_nelta.py
# Licensed under the MIT license.

from unittest import TestCase, main

from nelta import LabeledList, read_csv

class TestLabeledList(TestCase):
    def test_composite_1(self):
        t = read_csv('data/fruitarians.csv')
        x = """first                last weekly_fruits_eaten           fav_color
0                 abe               apple                 0.0                 red
1                 bob              banana                 4.0              yellow
2               carol             coconut               100.0               white"""
        
        self.assertEqual(str(t.head(3)), x)
        
    def test_composite_2(self):
        t = read_csv('data/fruitarians.csv')

        self.assertEqual(t[t['last'] == 'apple'].shape()[0], 2)
        
    def test_composite_3(self):
        t = read_csv('data/fruitarians.csv')
        x = """first weekly_fruits_eaten
2               carol               100.0
4                 eve                20.0
6                 ann                23.0"""
        y = t[t['weekly_fruits_eaten'] > 10][['first', 'weekly_fruits_eaten']]
        
        self.assertEqual(y, x)
        
    def test_composite_4(self):
        t = read_csv('data/fruitarians.csv')
        
        def lengthLessThan(n):
            def isLengthLessThanN(s):
                return len(s) < n
            return isLengthLessThanN
        
        shortFirstName = t[t['first'].map(lengthLessThan(4))]
        shortFirstName[shortFirstName['weekly_fruits_eaten'] < 10]

if __name__ == '__main__':
    main()
