class HashTable:
    def __init__(self):
        self.max = 100
        self.arr = [[]] for i in range(self.max)]

    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.max
    
    #also __setitem__
    def add(self, key, val): 
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key,val)
                found = True
                break
        #if empty, add with the new one
        if not found:
            self.arr[h].append((key,val))
    
    #also __getitem__
    def get(self,key):
        h = self.get_hash(key)
        for element in self.array[h]
            if element[0] == key:
                return element[1]
        return self.arr[h]

    # also __delitem, deletes element
    def del(self, key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]

t = HashTable()
value = t.get_hash('march 6')
print(value)