# Списки, словари и множества - изменяемые!
from copy import deepcopy


l = [1, 2, 3, [4, 5, 6]]
ll = deepcopy(l)

ll.insert(0, 0)
ll[-1].append(7)
print(l)
print(ll)

# Кортежи, frozenset - нет

tuple()
t = (1, 2, 3, 4, 5)
print(t[0])

s = {1, 2, 3}
