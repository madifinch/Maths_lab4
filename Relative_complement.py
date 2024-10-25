U = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
a = {1, 2, 3, 4, 5}
b = {1, 3, 5, 7, 9}
c = {3, 4, 8, 9}
d = {2, 4, 6, 8}
e = {3, 5}

#i 
#answer before python: 8, 6
print ('D = ', d)
print ('A = ', a)
print ('D \ A = ', d.difference(a))

#j 
#answer before python: 4, 8
print ('C \ B = ', c.difference(b))

#k
#answer before python: 1, 2, 5
print ('A \ C = ', a.difference(c))

#l
#answer before python: 2, 4, 6, 8, 10 
print ('U \ B = ', U.difference(b))