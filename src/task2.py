from collections import OrderedDict


def distinct(seq: list) -> list:
    """Simple distinct"""
    return list(set(seq))


def distinct_with_order(seq: list) -> list:
    """Distinc with saving original order"""
    return list(OrderedDict.fromkeys(seq))


if __name__ == "__main__":
    print(distinct_with_order([1, 4, 7, 6, 6, 2, 8, 12, 4]))
