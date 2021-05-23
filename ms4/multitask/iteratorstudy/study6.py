#!/usr/bin/python

print("study6 - generator types")


print("  study6 - multiple types")

# Generator that yields multiple types
def gentypes() :
    yield 1
    yield "two"
    yield True
    yield None
    yield
    yield 6
        
for element in gentypes() :
    print( "   ", element, "-", type(element).__name__ )

    
print("  study6 - side effect")

# Generator that only has side effects
def sideeffect(n) :
    for i in range(n) :
        print( "   ", i)
        yield
        
for element in sideeffect(6) :
    print( "   ", element)

# study6 - generator types
#   study6 - multiple types
#     1 - int
#     two - str
#     True - bool
#     None - NoneType
#     None - NoneType
#     6 - int
#   study6 - side effect
#     0
#     None
#     1
#     None
#     2
#     None
#     3
#     None
#     4
#     None
#     5
#     None
