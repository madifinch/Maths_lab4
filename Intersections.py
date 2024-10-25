U = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
a = {1, 2, 3, 4, 5}
b = {1, 3, 5, 7, 9}
c = {3, 4, 8, 9}
d = {2, 4, 6, 8}
e = {3, 5}

#intersection 
#A
#answer before python: 1 , 3, 5
print ('A = ', a)
print ('B = ', b)
print ('AnB = ', a.intersection(b))

#b 
#answer before python: 3, 9
print ('B = ', b)
print ('C = ', c)
print ('BnC = ', b.intersection(c))

#c 
#answer before python: N/A
print ('B = ', b)
print ('D = ', d)
print ('BnD = ', b.intersection(d))

#d 
#answer before python: 3, 4, 8, 9
print ('U = ', U)
print ('C = ', c)
print ('UnC = ', U.intersection(c))

