"""
print("Switch the value of a to b or b to a.")
x = int(input("x: "))
y = int(input("y: "))

print('Before swapping: x = %s, y = %s' % (x, y))

swapper = lambda x, y : ((x ^ x ^ y), (x ^ y ^ y))

print('After swapping: x = %s, y = %s ' % swapper(x, y))
"""

print("Switch the value of a to b or b to a.")
x = input("a: ")
y = input("b: ")

z = x
x = y
y = z

print("a = " + x)
print("b = " + y)