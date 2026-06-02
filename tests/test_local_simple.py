def test_addition():
    assert 1 + 1 == 2

def test_string_concat():
    assert "hello" + " " + "world" == "hello world"

def test_list_ops():
    nums = [1, 2, 3]
    nums.append(4)
    assert nums == [1, 2, 3, 4]

def test_fail_example():
    assert True
