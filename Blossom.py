from BlossomLib import flower_definitions
from LinkedList import LinkedList
from Node import Node

class HashMap:

    def __init__(self, size):
        self.array_size = size
        self.array = [LinkedList() for item in range(self.array_size)]

    def hash(self, key):
        return sum(key.encode())

    def compress(self, hash_code):
        return hash_code % self.array_size

    def assign(self, key, value):
        index = self.compress(self.hash(key))
        payload = Node([key, value])
        list_at_index = self.array[index]
        for node in list_at_index:
            if (node is not None) and (node.get_value()[0] == key):
                node.value = value
                return
        list_at_index.insert_beginning(payload)

    def retrieve(self, key):
        index = self.compress(self.hash(key))
        list_at_index = self.array[index]
        for node in list_at_index:
            if node.get_value()[0] == key:
                return node.get_value()[1]
        return None


blossom = HashMap(len(flower_definitions))
for flower in flower_definitions:
    blossom.assign(flower[0], flower[1])
print(blossom.retrieve("wisteria"))
