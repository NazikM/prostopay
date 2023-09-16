import pytest
from task1 import HashMap  # Assuming your HashMap class is in a separate file called 'hashmap.py'


def test_put_and_get():
    hashmap = HashMap()
    hashmap.put("name", "Nazar")
    assert hashmap.get("name") == "Nazar"


def test_overwrite():
    hashmap = HashMap()
    hashmap.put("name", "Nazar")
    hashmap.put("name", "Oksana")
    assert hashmap.get("name") == "Oksana"


def test_non_existent_key():
    hashmap = HashMap()
    assert hashmap.get("age") is None


def test_collision():
    hashmap = HashMap()
    hashmap.put("age", 21)
    hashmap.put("phone", "38099190xxxx")
    assert hashmap.get("age") == 21
    assert hashmap.get("phone") == "38099190xxxx"


def test_resizing():
    hashmap = HashMap()
    for i in range(10, 35):
        hashmap.put(f"key{i}", f"value{i}")
    assert hashmap.get("key30") == "value30"
    assert hashmap.get("key32") == "value32"


if __name__ == "__main__":
    pytest.main()
