import numpy as np

B= np.arange(1, 11)**2
C= np.arange(11,21)**2
D= np.arange(21,31)**2
E= np.arange(31,41)**2
F= np.arange(41,51)**2
G= np.arange(51,61)**2
H= np.arange(61,71)**2
I= np.arange(71,81)**2
J= np.arange(81,91)**2
K= np.arange(91,101)**2
A= np.vstack ((B,C,D,E,F,G,H,I,J,K))
print (A)

print ("Elements that are divisible by 3: ")

X= A[A%3==0]
print (X)

