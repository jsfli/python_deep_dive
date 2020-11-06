import sys

a = [1,2,3]

print(id(a))

print(sys.getrefcount(a))

import ctypes

def ref_count(address: int):
    return ctypes.c_long.from_address(address).value

print(ref_count(id(a)))

b = a

print(id(b))

print(ref_count(id(b)))
 
