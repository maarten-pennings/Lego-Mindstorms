#!/usr/bin/python
import random

print("study1 - basic iterator (by self)")

# This class creates a random permutation (of size `num`).
# The object is iterable.
# Note, the object is its _own_ iterator.
# Advantage: no extra class, disadvantage: can not have two iterators at the same time
class Perm :
    def __init__(self,num) :
        self.nums= list(range(num))
        # make a permutation
        for i1 in range(num) :
            i2 = random.randrange(i1,num)
            self.nums[i1],self.nums[i2] = self.nums[i2],self.nums[i1]

    # Having __iter__ makes an object iterable.
    # In this case we return ourselves (self). 
    # A cursor is created (iter_index) and reset to 0, the first element.
    # Note, object is its _own_ iterator; disadvantage: can not have two iterators at the same time
    def __iter__(self) :
        self.iter_index = 0
        return self

    # The __iter__() function shall return an object that has a __next__().
    # Since the object is its own iterator, it must have __next__().
    # __next__() must return all elements, one per call, and end by raising StopIteration
    def __next__(self) :
        if self.iter_index == len(self.nums ) :
            raise StopIteration
        val = self.nums[ self.iter_index ]
        self.iter_index += 1
        return val
        
iterable = Perm(4)

# Getting the iterator from the iterable: low-level
print("  study1 - low-level")
iterator1 = iterable.__iter__()
print( "   ", iterator1.__next__() )
print( "   ", iterator1.__next__() )
print( "   ", iterator1.__next__() )
print( "   ", iterator1.__next__() )
#print("   ", iterator1.__next__() ) # Raises exception

# Getting the iterator from the iterable: python-way: use wrappers iter() and next()
print("  study1 - python-way")
iterator2 = iter(iterable)
print( "   ", next(iterator2) )
print( "   ", next(iterator2) )
print( "   ", next(iterator2) )
print( "   ", next(iterator2) )
#print("   ", next(iterator2) ) # Raises exception

# Looping using an iterable: for-in
print("  study1 - for-in")
for element in iterable :
    print( "   ", element )

# Does not work: create all combinations
# (Doesn't work because the object is its own iterator, so the iterators are aliases of each other)
print("  study1 - two iterators: does NOT work")
for elm1 in iterable :
    for elm2 in iterable :
        print( "   ",elm1,elm2)

# study1 - basic iterator (by self)
#   study1 - low-level
#     2
#     0
#     1
#     3
#   study1 - python-way
#     2
#     0
#     1
#     3
#   study1 - for-in
#     2
#     0
#     1
#     3
#   study1 - two iterators: does NOT work
#     2 2
#     2 0
#     2 1
#     2 3

