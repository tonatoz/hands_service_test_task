from src.task2 import distinct, distinct_with_order

input = [1, 4, 7, 6, 6, 2, 8, 12, 4]
expected = [1, 4, 7, 6, 2, 8, 12]


def test_simple_uniq():
    assert set(distinct(input)) == set(expected)


def test_order_uniq():
    assert distinct_with_order(input) == expected
