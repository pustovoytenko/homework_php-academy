class IteratorFromFile(object):
    def __init__(self, filename):
        self.fd = open(filename, 'r')

    def __iter__(self):
        return self

    def __next__(self):
        line = self.fd.readline()
        if line != '':
            line = line.rstrip('\n')
            self.line = line
            # if len(self.line) == 4:
            return self.line
        raise StopIteration


class IteratorFromList(object):

    def __init__(self, items):
        self.items = items
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        length = len(self.items)
        if self.i < length:
            self.item = self.items[self.i]
            self.i += 1
            return self.item
        raise StopIteration

file_data = IteratorFromFile("test.txt")

for item in file_data:
    print(file_data.line)

example_list = IteratorFromList([1, 2, 3, 4])

for item_list in example_list:
    print(example_list.item)
