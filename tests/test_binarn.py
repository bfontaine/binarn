import binarn


def test_find_one_atom_value():
    for value in (42, -10, None, True, False, 1.2, object(), "foo", b"bar", lambda: 2):
        assert binarn.find_one(value, value=value) == ((), value)


def test_find_one_atom_value_mismatch():
    assert binarn.find_one(object(), value=object()) is None


def test_find_one_atom_key():
    for value in (42, -10, None, True, False, 1.2, object(), "foo", b"bar", lambda: 2):
        assert binarn.find_one(value, key=value) is None


def test_find_one_dict():
    assert binarn.find_one({}, key=42) is None
    assert binarn.find_one({}, value=42) is None
    assert binarn.find_one({41: 41}, key=42) is None
    assert binarn.find_one({41: 41}, value=42) is None
    assert binarn.find_one({41: "a"}, key=41) == ((41,), "a")
    assert binarn.find_one({"a": 41}, value=41) == (("a",), 41)
