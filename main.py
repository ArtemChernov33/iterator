nested_list = [
   ['a', 'b', 'c'],
   ['d', 'e', 'f', 'h', False],
   [1, 2, None],
]

class FlatIterator(list):

    def __iter__(self):
        self.count1 = 0
        self.count2 = -1
        return self

    def __next__(self):

        if self.count1 is None:
                if self.count2 is None:
            #if self.count2 == 0:
                    raise StopIteration
        return self.count2


for item in FlatIterator(nested_list):
   print(item)