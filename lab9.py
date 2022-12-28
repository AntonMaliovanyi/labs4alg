import random

class HashTable:
    def __init__(self):
        self.size = 31
        self.slots = [None] * self.size
        self.col_num = 0

    def put(self,key):
      hashvalue = self.hashfunction(key)

      if self.slots[hashvalue] == None:
        self.slots[hashvalue] = key
      else:
          self.col_num += 1
          nextslot = self.rehash(hashvalue, len(self.slots))
          
          while self.slots[nextslot] != None and self.slots[nextslot] != key:
            nextslot = self.rehash(nextslot, len(self.slots))

          if self.slots[nextslot] == None or self.slots[nextslot] == key:
            self.slots[nextslot] = key

    def hashfunction(self, key):
         return (key + 2003) % 3

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size



H=HashTable()
L = []

for i in range(30):
    L.append(random.randint(0, 1000))

print("Randomly generated elements")
print("Index  Element")
for i in L:
    print(L.index(i), "  |  ", i)

for i in range(len(L)):
    H.put(L[i])
 

print("  Hash table")
print("Index  Element")
for i in H.slots:
    print(H.slots.index(i), "  |  ", i)

print("col_num =", H.col_num)





