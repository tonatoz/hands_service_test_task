from collections import OrderedDict

x = [1, 4, 7, 6, 6, 2, 8, 12, 4]

# Simpel - using set
uniq_x = list(set(x))

# Saving order usign collections
uniq_x2 = list(OrderedDict.fromkeys(x))

# Saving order with manualy caching visited items
def distinct(nums):
    visited = set()
    return [a for a in nums if a not in visited and not visited.add(a)]


uniq_x3 = distinct(x)


print(x)
print(uniq_x, uniq_x2, uniq_x3)
