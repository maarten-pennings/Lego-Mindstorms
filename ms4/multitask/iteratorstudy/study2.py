#!/usr/bin/python
import random

print("study2 - stand-alone iterator")

# This class creates a random permutation (of size `num`).
# The object is iterable; it has a stand-alone iterator.
# Advantage: can have two iterators at the same time, disadvantage: extra class
class Perm :
    def __init__(self,num) :
        self.nums= list(range(num))
        # make a permutation
        for i1 in range(num) :
            i2 = random.randrange(i1,num)
            self.nums[i1],self.nums[i2] = self.nums[i2],self.nums[i1]

    # Having __iter__ makes an object iterable.
    # The __iter__() function shall return an object that has a __next__().
    # Here we create a fresh iterator (it must know what to iterate)
    def __iter__(self) :
        return PermIterator(self)

# An "internal" class, implementing an iterator of the Perm class
class PermIterator :
    def __init__(self,perm) :
        self.perm = perm # ref to iterable
        self.index = 0 # the "cursor" of the iterator

    # Since this is an iterator, it must have __next__().
    # __next__() must return all elements of the iterable, 
    # one per call, and end by raising StopIteration
    def __next__(self) :
        if self.index == len(self.perm.nums ) :
            raise StopIteration
        val = self.perm.nums[ self.index ]
        self.index += 1
        return val
        
iterable = Perm(4)

# Getting the iterator from the iterable: for-in
print("  study2 - for-in")
for element in iterable :
    print( "   ", element )

# Does now work: create all combinations using two separate iterators
print("  study2 - two iterators: does now work")
for elm1 in iterable :
    for elm2 in iterable :
        print( "   ",elm1,elm2)

# study2 - stand-alone iterator
#   study2 - for-in
#     0
#     2
#     3
#     1
#   study2 - two iterators: does now work
#     0 0
#     0 2
#     0 3
#     0 1
#     2 0
#     2 2
#     2 3
#     2 1
#     3 0
#     3 2
#     3 3
#     3 1
#     1 0
#     1 2
#     1 3
#     1 1
