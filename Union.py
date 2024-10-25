U = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
a = {1, 2, 3, 4, 5}
b = {1, 3, 5, 7, 9}
c = {3, 4, 8, 9}
d = {2, 4, 6, 8}
e = {3, 5}

#e
#answer before python: 1, 2, 3, 4, 5, 7, 9
print ('A = ', a)
print ('B = ', b)
print ('AUB = ', a.union(b))

#f
#answer before python: 1, 2, 3, 4, 5, 8, 9
print ('A = ', a)
print ('C = ', c)
print ('AUC = ', a.union(c))

#g
#answer before python: 1, 3, 4, 5, 7, 8, 9
print ('B = ', b)
print ('C = ', c)
print ('BUC = ', b.union(c))

#h
#answer before python: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
print ('U = ', U)
print ('A = ', a)
print ('UUA = ', U.union(a))