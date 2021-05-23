#!/usr/bin/python

print("study5 - nested generators")


# Generator function for 5 powers of `base`
print("  study5 - pow")
def pow(base) :
    for exp in range(5) :
        yield base ** exp

# Getting the iterator from the generator: for-in
for element in pow(10) :
    print( "   ", element )


# Generator function that contains two generators: pow(base1) and pow(base2) and both are iterated        
print("  study5 - nested yield")
def dualpow1(base1,base2) :
    for elm in pow(base1) :
      yield elm
    for elm in pow(base2) :
      yield elm

# Getting the iterator from the generator: for-in
for element in dualpow1(2,3) :
    print( "   ", element )


# Generator function that contains two generators: pow(base1) and pow(base2) and both are iterated        
print("  study5 - nested yield-from")
def dualpow2(base1,base2) :
    yield from pow(base1)
    yield from pow(base2)
        
# Getting the iterator from the generator: for-in
for element in dualpow2(2,3) :
    print( "   ", element )


# Generator function that contains all pow(x) for x<=base.
# Is recursive, just for the fun of it.
print("  study5 - recursive")
def recursive(base) :
    if base>0 :
        yield from pow(base)
        yield from recursive(base-1)
        
# Getting the iterator from the generator: for-in
for element in recursive(5) :
    print( "   ", element )

# study5 - nested generators
#   study5 - pow
#     1
#     10
#     100
#     1000
#     10000
#   study5 - nested yield
#     1
#     2
#     4
#     8
#     16
#     1
#     3
#     9
#     27
#     81
#   study5 - nested yield-from
#     1
#     2
#     4
#     8
#     16
#     1
#     3
#     9
#     27
#     81
#   study5 - recursive
#     1
#     5
#     25
#     125
#     625
#     1
#     4
#     16
#     64
#     256
#     1
#     3
#     9
#     27
#     81
#     1
#     2
#     4
#     8
#     16
#     1
#     1
#     1
#     1
#     1
