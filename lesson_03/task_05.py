list_a = [1, 2, 3]
list_a.append('four')
print(list_a)
list_a[1] = 'two'
print(list_a)
list_a.append({5, 6})
print(list_a)
list_a[4].add(7)
print(list_a)
list_a[2] = (2.5, 2.6)
print(list_a)