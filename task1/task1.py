"""
Implementation notes:
    1) I created python dict-lin hashmap.
    2) You can choose capacity of hashmap, however it will auto increase if it'll e filled up to 70% of capacity.
    It's similar to python default dict behavior.
    3) I'm filling list with None values because it's consumes less memory at the start compare to list. But it will decrease
    speed, because we need to check if element filled. And it's doubles our time to put elements.
    4) Lists in python has O(1) time-complexity. So our HashMap is efficient.
"""


class HashMap:
    def __init__(self, capacity=10):
        self.max_size = int(capacity * 0.7)
        self.hash_map = [None] * capacity
        self.capacity = capacity
        self.size = 0

    def _hash(self, key):
        return hash(key) % self.capacity

    def increase_max_size(self):
        new_capacity = self.capacity * 2
        print(f"Increased max_size to {new_capacity}")
        new_table = [None] * new_capacity

        for bucket in self.hash_map:
            if bucket is not None:
                for key, value in bucket:
                    index = hash(key) % new_capacity
                    if new_table[index] is None:
                        new_table[index] = []
                    new_table[index].append((key, value))

        self.capacity = new_capacity
        self.max_size = int(new_capacity * 0.7)
        self.hash_map = new_table

    def put(self, key, value):
        """
        Add a key-value pair to the HashMap.
        """

        if self.size >= self.max_size:
            self.increase_max_size()

        index = self._hash(key)
        if not self.hash_map[index]:
            self.hash_map[index] = []

        bucket = self.hash_map[index]
        for i, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self.size += 1

        # for pair in self.hash_map[index]:
        #     if pair[0] == key:
        #         pair[1] = value  # Update value if key already exists
        #         return
        # self.hash_map[index].append([key, value])

    def get(self, key):
        index = self._hash(key)
        if self.hash_map[index] is None:
            return None
        bucket = self.hash_map[index]
        for existing_key, value in bucket:
            if existing_key == key:
                return value
        return None


# Test Cases
def test_hashmap():
    hashmap = HashMap()

    # Test put and get
    hashmap.put("name", "Nazar")
    assert hashmap.get("name") == "Nazar"

    # Test overwrite
    hashmap.put("name", "Oksana")
    assert hashmap.get("name") == "Oksana"

    # Test non-existent key
    assert hashmap.get("age") is None

    # Test collision
    hashmap.put("age", 21)
    hashmap.put("phone", "38099190xxxx")
    assert hashmap.get("age") == 21
    assert hashmap.get("phone") == "38099190xxxx"

    # Test resizing
    for i in range(20, 70):
        hashmap.put(f"key{i}", f"value{i}")
    assert hashmap.get("key30") == "value30"
    assert hashmap.get("key32") == "value32"


if __name__ == "__main__":
    test_hashmap()
    print("All tests passed.")