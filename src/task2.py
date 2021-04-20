from collections import OrderedDict

x = [1, 4, 7, 6, 6, 2, 8, 12, 4]

# Simpel - using set
def distinct(x):
    return list(set(x))


# Saving order usign collections
def distinct_with_order(x):
    return list(OrderedDict.fromkeys(x))
