# nelta.py
# Licensed under the MIT license.

# CONSTRAINT: must use at least 4 list comprehensions
# CONSTRAINT: may not use `pandas`, `numpy`; must use `csv`

class LabeledList:
    
    def __init__(self, data = None, index = None):
        if index is None:
            index = list(range(len(data)))
            
        self.values = data
        self.index = index

    def __str__(self):
        s = ''
        max_len = max([len(str(label)) for label in self.index])
        vals_max_len = max([len(str(v)) for v in self.values])
        format_spec = f'>{max_len}'
        
        for index, data in zip(self.index, self.values):
            s += f'{index:{format_spec}} {str(data):>{vals_max_len}}\n'
        
        return s

    def __repr__(self):
        return self.__str__()

    def __getitem__(self, key_list):
        if isinstance(key_list, LabeledList):
            key_list = key_list.values

        if not isinstance(key_list, list):
            key_list = [key_list]
        
        if len([v for v in key_list if type(v) is bool]) == len(key_list):
            return self.__filter(key_list) 
        else:
            index = []
            data = []
            
            for key in key_list:
                for label, val in self.__find(key):
                    index.append(label)
                    data.append(val)
            
            return data[0] if len(data) == 1 else LabeledList(data, index)

    def __filter(self, filter_list):
        index = []
        data = []
        
        if len(filter_list) != len(self.index):
            raise IndexError('Length of indexes does not match length of boolean list')
        
        for i, include in enumerate(filter_list):
            if include:
                index.append(self.index[i])
                data.append(self.values[i])
                
        return LabeledList(data, index)
    
    def __find(self, k):
        index, data = [], []
        matches = [
            (label, self.values[i]) for i, label in enumerate(self.index) 
                if k == label
        ]
        
        if len(matches) == 0:
            raise KeyError(f'Index label not found {k}')
        
        return matches
    
    def __iter__(self):
        return iter(self.values)
    
    def __eq__(self, scalar):
        return LabeledList(
            [ i is not None and i == scalar for i in self.values ], self.index)
        
    def __ne__(self, scalar):
        return LabeledList(
            [ i is not None and i != scalar for i in self.values ], self.index)
     
    def __gt__(self, scalar):
        return LabeledList(
            [ i is not None and i > scalar for i in self.values ], self.index)
    
    def __lt__(self, scalar):
        return LabeledList(
            [ i is not None and i < scalar for i in self.values ], self.index)
    
    def map(self, f):
        return LabeledList([ f(i) for i in self.values ], self.index)
    
class Table:
    pass


if __name__ == '__main__':
    def squared(n):
        return n ** 2
    
    print(LabeledList([5, 6, 7]).map(squared))
    