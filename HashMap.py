class HashMap:

    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None for num in range(self.array_size)]

    def hash(self, key, collisions=0):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code + collisions

    def compressor(self, hashcode):
        return hashcode % self.array_size

    def assign(self, key, value):
        index = self.compressor(self.hash(key))
        current_value = self.array[index]
        if (current_value is None) or (current_value[1] == value):
            self.array[index] = [key, value]
        elif current_value != key:
            collisions = 1
            while current_value != key:
                new_index = self.compressor(self.hash(key, collisions))
                current_value = self.array[new_index]
                if (current_value is None) or (current_value[1] == value):
                    self.array[new_index] = [key, value]
                    return
                else:
                    collisions += 1
        return

    def retrieve(self, key):
        current_value = self.array[self.compressor(self.hash(key))]
        if current_value is None:
            return None
        elif current_value[0] == key:
            return current_value[1]
        elif current_value[0] != key:
            collisions = 1
            while current_value[0] != key:
                current_value = self.array[self.compressor(self.hash(key, collisions))]
                if current_value is None:
                    return None
                elif current_value[0] == current_value:
                    return current_value[1]
                else:
                    collisions += 1
