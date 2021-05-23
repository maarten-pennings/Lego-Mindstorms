#!/usr/bin/python

print("study3 - indefinite iterator (by self)")

# This class is an container of _all_ Fibonacci numbers.
# It doesn't store them, but it can be iterated.
# The object is iterable; it is its own iterator.
class Fibonacci :
    def __init__(self) :
        pass

    def __iter__(self) :
        self.a = 0
        self.b = 1
        return self

    def __next__(self) :
        val = self.a
        self.a , self.b = self.b , self.a+self.b
        return val
        
iterable = Fibonacci()

# Getting the iterator from the iterable: for-in
print("  study3 - for-in")
for element in iterable :
    print( "   ", element )
    if element==13 :
        break # Emergency break

# study3 - indefinite iterator (by self)
#   study3 - for-in
#     0
#     1
#     1
#     2
#     3
#     5
#     8
#     13
