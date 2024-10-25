U = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
a = {1, 2, 3, 4, 5}
b = {1, 3, 5, 7, 9}
c = {3, 4, 8, 9}
d = {2, 4, 6, 8}
e = {3, 5}

#p 
#answer before python: false
print ('A subset of C = ', a.issubset(c))

#q
#answer before python: false 
print ('A subset of E = ', a.issubset(e))

#r
#answer before python: false
print ('B subset of E = ', b.issubset(e))

#s 
#answer before python: false 
print ('U subset of A = ', U.issubset(a))

#supersets

#t
#answer before python; true 
print ('U superset of A = ', U.issuperset(a))

#u
#answer before python; false 
print ('B superset of C = ', b.issuperset(c))

#v
#answer before python; true 
print ('E superset of A', e.issuperset(a))
