import sys
import ctypes
x,y,z=1,"Hello",True
print(x,y,z)
print(type(x))
print(type(y))
print(type(z))
y=1
z=1
print(id(x))
print(id(y))
print(id(z))

print(sys.getrefcount(x))
print(sys.getrefcount(y))
print(sys.getrefcount(z))   

address1=ctypes.addressof(ctypes.py_object(x))
print("Address 1 :",address1)

address2=ctypes.addressof(ctypes.py_object(y))
print("Address 2 :",address2)

address3=ctypes.addressof(ctypes.py_object(z))
print("Address 3 :",address3)

print(sys.getsizeof(x))