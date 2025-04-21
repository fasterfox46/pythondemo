import math
import numpy as np
# Class Definition
class Person:
 def __init__(self, name, age):
  self.name = name
  self.age = age
  
# function Definition
def sum(x, y):
 return x + y
def fact(x):
 if x == 0:
   return 1
 else:
   return x * fact(x - 1)
pi = math.pi

# Creating a matrix from a string
matrix_str = np.matrix('1 2 1; 3 5 2')
print("Matrix from string:\n", matrix_str)

a = np.array([[1, 2], [3, 5]])
b = np.array([1, 2])
x = np.linalg.solve(a, b)
print("equation:",x)
print("pi",pi)
print("fact 5:", fact(5))
p1 = Person("Ivan", 60)
print ("name:", p1.name)
print ("age:", p1.age)
print ("hello world")
a = 1
b = 5 
if a > 1:
 print ("if if")
else:
 print ("else else")
while a < b:
 print(a)
 a = a + 1
print ("end while")
a = 1
for a in range(b):
 print("a", a)
print("end for")
print ("suma:",sum(4,7))


# Define matrix A (coefficients)
A = np.array([[2 + 3j, 4 - 1j],
              [1 - 1j, 3 + 2j]])

# Define vector b (right-hand side)
b = np.array([5 + 2j, 4 - 3j])

# Solve for x
x = np.linalg.solve(A, b)

print("Solution:", x)

