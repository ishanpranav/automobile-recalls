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
        result = ""
        maxLength = max(len(str(label)) for label in self.index)
        valuesMaxLength = max(len(str(value)) for value in self.values)
        formatting = f'>{maxLength}'
        
        for label, value in zip(self.index, self.values):
            result += f"{label:{formatting}} {str(value):>{valuesMaxLength}}\n"
        
        return result

    def __repr__(self):
        return self.__str__()

    def __getitem__(self, keys):
        def filter(includes):
            index = []
            data = []
            
            if len(includes) != len(self.index):
                raise IndexError(
                    "Length of indexes does not match length of boolean list")
            
            for i, include in enumerate(includes):
                if include:
                    index.append(self.index[i])
                    data.append(self.values[i])
                    
            return LabeledList(data, index)
        
        def find(k):
            matches = [
                (label, self.values[i]) for i, label in enumerate(self.index) 
                    if k == label
            ]
            
            if len(matches) == 0:
                raise KeyError(f'Index label not found {k}')
            
            return matches
        
        if isinstance(keys, LabeledList):
            keys = keys.values

        if not isinstance(keys, list):
            keys = [keys]
        
        if len([ v for v in keys if type(v) is bool ]) == len(keys):
            return filter(keys) 
        
        index = []
        data = []
        
        for key in keys:
            for label, value in find(key):
                index.append(label)
                data.append(value)
        
        return data[0] if len(data) == 1 else LabeledList(data, index)

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
    def __init__(self, data = None, index = None, columns = None):
        if index is None:
            index = list(range(len(data)))
            
        if columns is None:
            if len(data) == 0:
                columns = []
            else:    
                columns = list(range(len(data[0])))
       
        self.values = data
        self.index = index
        self.columns = columns

    def __str__(self):
        result = ""
        maxLength = max(len(str(label)) for label in self.index)
        formatting = f'>{maxLength}'
        values = self.values + [ self.columns ]
        columnMaxLengths = [
            max(len(str(value[i])) for value in values)
            for i in range(len(self.columns))
        ]
        
        result += " " * maxLength
        
        for column, columnMaxLength in zip(self.columns, columnMaxLengths):
            result += f" {str(column):>{columnMaxLength}}"
            
        result += "\n"
        
        for label, value in zip(self.index, self.values):
            result += f"{label:{formatting}} "
            
            for cell, columnMaxLength in zip(value, columnMaxLengths):
                result += f" {str(cell):>{columnMaxLength}}"
        
            result += "\n"
            
        return result
        
    def __repr__(self):
        return self.__str__()
    
    def __getitem__(self, keys):
        def filter(includes):
            index = []
            data = []
            count = len(includes)
            
            if count != len(self.index):
                raise IndexError(
                    "Length of indexes does not match length of boolean list")
            
            for i, include in enumerate(includes):
                if include:
                    index.append(self.index[i])
                    data.append(self.values[i])
            
            if count == 1:
                return LabeledList(data, index)
        
            return Table(data, index, self.columns)
        
        if isinstance(keys, LabeledList):
            keys = keys.values
            
        # if not isinstance(keys, list):
        #     keys = [keys]
        
        if len([ v for v in keys if type(v) is bool ]) == len(keys):
            return filter(keys)
        
        data = []
        columns = []
        
        for key in keys:
            for i, column in enumerate(self.columns):
                if column == key:
                    columns.append(column)
                    
        for value in self.values:
            row = []
            
            for key in keys:
                for i, column in enumerate(self.columns):
                    if column == key:
                        row.append(value[i])
            
            data.append(row)
            
        return Table(data, self.index, columns)
    
        # index = []
        # data = []
        
        # for key in keys:
        #     for label, value in find(key):
        #         index.append(label)
        #         data.append(value)
        
        # return data[0] if len(data) == 1 else LabeledList(data, index)

def read_csv(f):
    pass
