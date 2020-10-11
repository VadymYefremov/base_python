""" Sort data by 'List' """
a = ['a', 'b', 'c', 'd', 'e']
b = ['a', 2, 'c', [0, 10, [4, 'z']]]
c = ['a', 'b', 'c', 'd', 'e']
d = [1, 2, 3, 4, 5, 6, 7, 8]


a.append(str('r'))
b.insert(1, 9)
c.reverse()
d.extend(c)
d.insert(2, 3)
a.remove('b')
ind_b = c.index('b')
count_c = c.count('b')

print(a)
print(b)
print(c)
print(d)
print(ind_b)
print(count_c)
