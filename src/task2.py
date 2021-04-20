from collections import OrderedDict


def distinct(seq: list) -> list:
    """Simple distinct"""
    return list(set(seq))


def distinct_with_order(seq: list) -> list:
    """Distinc with saving original order"""
    return list(OrderedDict.fromkeys(seq))
