# Iterator study

This directory contains some python projects with the aim to understand iterators.
Iterators form the basis for generators, which I wanted to use for cooperative multitasking in Lego Mindstorms 4 Robot inventor.
However, this study is Python (on a PC) only.

## Introduction

In software, a _container_ is a data-structure that stores a multitude of elements.
Prime examples are a list of integers, or a tree of identifiers.
One operation that is typically required from a container it to loop over all elements.
Such a container is than called _iterable_.

In python, if an object `iterable` (a container) is iterable we can ask it for an _iterator_ by calling `iter(iterable)`.
```python
  iterator = iter(iterable)
```
This returns a (new) object `iterator` that allows iterating over all elements in `iterable`.

Internally, the iterator maintains a "cursor". 
Initially, when the iterator is created, the cursor points to the first element of `iterable`.
By calling `next(iterator)`, the element that the cursor points to is returned, and the cursor moves to the next element.
When `next()` is called and there is no (more) element the exception `StopIteration` is raised.

That is all.

Well, maybe one more thing: Python's for-in does all of this behind the scenes. So you can just type
```python
for element in iterable :
    print( element )
```
and the for loop takes care of calling `iter()` on the `iterable`, calling `next()` on the returned iterator,
and stopping on `StopIteration`.

Let's look into the details.

## Setup

To follow the study, you need Python on you machine. 
I got mine at [python.org](https://www.python.org/downloads/).
If Python is not in your search `PATH`, edit the line that defines `PYTHONDIR` in `setup.bat`.

I use a standard setup with a virtual environment.
If you download this directory `iteratorstudy`, open command prompt and run `setup`.
This script creates a directory `env` with a copy of the python interpreter, pip and all modules needed.
At any moment you can delete `env` again because `setup` can recreate it. 
That's why this repo does not have the `env` directory.

After you have run `setup` it has changed that `cmd` instantiation. 
The most important part is that the path to Python has changed to the `env` virtual environment.
To make that visible, also the prompt has changed; it has `(env)` prepended, see the last line

```cmd
C:\Repos\Lego-Mindstorms\ms4\multitask\iteratorstudy>setup
Found correct version of Python; creating virtual env
Requirement already satisfied: pip in c:\repos\lego-mindstorms\ms4\multitask\iteratorstudy\env\lib\site-packages (21.1.1)
Collecting pip
  Downloading pip-21.1.2-py3-none-any.whl (1.5 MB)
     |████████████████████████████████| 1.5 MB 6.4 MB/s
Requirement already satisfied: setuptools in c:\repos\lego-mindstorms\ms4\multitask\iteratorstudy\env\lib\site-packages (57.0.0)
Requirement already satisfied: wheel in c:\repos\lego-mindstorms\ms4\multitask\iteratorstudy\env\lib\site-packages (0.36.2)
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 21.1.1
    Uninstalling pip-21.1.1:
      Successfully uninstalled pip-21.1.1
Successfully installed pip-21.1.2
'setup' done, now 'run'

(env) C:\Repos\Lego-Mindstorms\ms4\multitask\iteratorstudy>
```

Why would you want to have a virtual environment? Because it allows installing the modules 
needed for a project, only with that project (with the versions needed by that project).

By the way, the modules needed for a project are found in `requirements.txt`, for this study, that file is empty.

Next step is to run `run.bat`. It just runs the python file, after checking that the virtual environment has been activated.

## Study 1 basic iterator (by self)

Let's implement our own container and make it iterable.

### Study1 - source

In [study 1](study1.py) we make a simple container `Perm`.
An object `Perm(n)` will contain a random permutation of all numbers from (including) 0 to (excluding) n.
For example, `Perm(5)` might be 0,1,2,3,4, but that is unlikely because there are 119 other permutations, e.g. 0,3,1,4,2.

```python
import random

# This class creates a random permutation (of size `num`).
class Perm :
    def __init__(self,num) :
        self.nums= list(range(num))
        # make a permutation
        for i1 in range(num) :
            i2 = random.randrange(i1,num)
            self.nums[i1],self.nums[i2] = self.nums[i2],self.nums[i1]
```

The object is a container (of the elements in the permutation - see `self.nums`), and we want it to be iterable.

This means we want to call `iter()`. 
What you should know is that `iter(obj)` calls `obj.__iter__()`, so that is what we need to add to our class.

A common approach (in Python) is that an iterable (`Perm`) implements its own iterator. Let's give that a try.
We add the `__iter__()` method to our `Perm` class, and set the cursor `iter_index` to 0.

```python    # Having __iter__ makes an object iterable.
    # Having __iter__ makes an object iterable.
    # In this case we return ourselves (self). 
    # A cursor is created (iter_index) and reset to 0, the first element.
    def __iter__(self) :
        self.iter_index = 0
        return self
```

The `__iter__()` returns an object, which must be an iterator. That means, the object must have a "next".
Since the `__iter__()` returns the `Perm` object itself, the `Perm` class must have the "next" method.
Similarly to `iter`, `next(obj)` calls `obj.__next__()`, so that is what we need to add to our `Perm` class.

```python
    # The __iter__() function shall return an object that has a __next__().
    # Since the object is its own iterator, it must have __next__().
    # __next__() must return all elements, one per call, and end by raising StopIteration
    def __next__(self) :
        if self.iter_index == len(self.nums ) :
            raise StopIteration
        val = self.nums[ self.iter_index ]
        self.iter_index += 1
        return val
```

That is all. 

### Study 1 - low level

See the complete source of [study1](study1.py) for details.
Let's see it in action.

First we call the methods we implemented, just to check they are working

```python
print("  study1 - low-level")
iterable = Perm(4)
iterator1 = iterable.__iter__()
print( "   ", iterator1.__next__() )
print( "   ", iterator1.__next__() )
print( "   ", iterator1.__next__() )
print( "   ", iterator1.__next__() )
#print("   ", iterator1.__next__() ) # Raises exception
```

This produces

```text
  study1 - low-level
    0
    1
    3
    2
```

If the last line was not commented out, the `StopIterator` would kick in.

```text
Traceback (most recent call last):
  File "C:\Repos\Lego-Mindstorms\ms4\multitask\iteratorstudy\study1.py", line 45, in <module>
    print("   ", iterator1.__next__() ) # Raises exception
  File "C:\Repos\Lego-Mindstorms\ms4\multitask\iteratorstudy\study1.py", line 31, in __next__
    raise StopIteration
StopIteration
```

### Study 1 - Python way

Instead of calling the low level methods `__iter__()` and `__next__()` 
we should call the Python wrappers `iter()` and `next()`.

```python
print("  study1 - python-way")
iterable = Perm(4)
iterator2 = iter(iterable)
print( "   ", next(iterator2) )
print( "   ", next(iterator2) )
print( "   ", next(iterator2) )
print( "   ", next(iterator2) )
#print("   ", next(iterator2) ) # Raises exception
```

This produces the same output

```text
  study1 - python-way
    0
    1
    3
    2
```

(and the same exception if the last line was not commented out).

### Study 1 - for-in

The real Pythonic way to do this is to use a for-in loop on an iterable.
The for-in first gets the iterator (`iter()`), and then uses it (`next()`).

```python
# Looping using an iterable: for-in
iterable = Perm(4)
print("  study1 - for-in (iterable)")
for element in iterable :
    print( "   ", element )
```

this produces the same output

```text
  study1 - for-in (iterable)
    0
    1
    3
    2
```

and even handles the `StopIteration`. 
A definite improvement.

Note that in general a for-in operates on an _iterable_, not on an _iterator_.
But in study 1, that happens to be one and the same object.

### Study 1 - two iterators

So, is everything fine? No.

Since the object is its own iterator (`__iter__()` returns `self`), every `Perm` object has exactly one cursor.
Suppose that we want to print a table of all element combinations.
We might expect the following to work.

```python
print("study1 - two iterators: does NOT work")
iterable = Perm(4)
for elm1 in iterable :
    for elm2 in iterable :
        print( "   ",elm1,elm2)
```

But it doesn't, we get this as output.

```text
  study1 - two iterators: does NOT work
    0 0
    0 1
    0 3
    0 2
```

The reason is that the iterators in the two for-in loops are _aliases_, so when the second loop ends
(after iterating 0, 1, 3, 2), also the first loops ends (it's an alias).

In study 2 we will fix this.


## Study 2 stand-alone iterator

In study 1 we implemented an iterator without creating a second class. 
The iterable _is_ its own iterator.
Since the iterable had only one cursor (`iter_index`), we can not have two iterators active at one time.

In this [study 2](study2.py) we fix that: `__iter__()` creates a fresh iterator, 
which is an object of a new class `PermIterator`.

### Study 2 - the iterable

We have the same iterable as before `Perm`.
This time, its `__iter__()` method returns a new fresh iterable `PermIterator`.
That also means, the `Perm` class no longer needs `__next__()` (it moves to the `PermIterator` class).

```python
import random

# This class creates a random permutation (of size `num`).
# The object is iterable; it has a stand-alone iterator.
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
```

Note that a `PermIterator` is created, and that it has a reference to the iterable:
the iterator must know which permutation to iterate.

### Study 2 - the iterator

The iterable `Perm` has a "friend" class `PermIterator` that knows (and touches) the
private parts of `Perm`.

```python
# An "internal" class, implementing an iterator of the Perm class
class PermIterator :
    def __init__(self,perm) :
        self.perm = perm # ref to iterable
        self.index = 0 # the "cursor" of the iterator

    # Since this is an iterator, it must have __next__().
    # __next__() must return all elements of the iterable, 
    # one per call, and end by raising StopIteration
    # We know the internal structure of Perm (e.g. that it has a `nums`).
    def __next__(self) :
        if self.index == len(self.perm.nums ) :
            raise StopIteration
        val = self.perm.nums[ self.index ]
        self.index += 1
        return val
```

### Study 2 - for-in

Let's test if this is still working.

```python
print("  study2 - for-in")
for element in iterable :
    print( "   ", element )
```

Yes it is

```text
  study2 - for-in
    0
    2
    3
    1
```

### Study 2 - two iterators

In study 1 two iterators did not work.
Does it now?

```python
print("  study2 - two iterators: does now work")
for elm1 in iterable :
    for elm2 in iterable :
        print( "   ",elm1,elm2)
```

Yes. The iterators are no longer aliases, they run independently.

```text
  study2 - two iterators: does now work
    0 0
    0 2
    0 3
    0 1
    2 0
    2 2
    2 3
    2 1
    3 0
    3 2
    3 3
    3 1
    1 0
    1 2
    1 3
    1 1
```       

## Study 3 indefinite iterator

One of the tricks we can do is to make an iterable with an indefinite amount of elements.
That is possible if we can _compute_ the elements instead of actually _storing_ them.

In [study 3](study3.py) we give an example using the Fibonacci sequence.

To keep the source short, we fall back on an iterable that has itself as iterator 
(with the know downside we can not have two iterators active).

```python
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
```

If we run it, it runs forever. Therefore, we added an emergency break.

```python
iterable = Fibonacci()

print("  study3 - for-in")
for element in iterable :
    print( "   ", element )
    if element==13 :
        break # Emergency break
```

So we get this as result

``` text
  study3 - for-in
    0
    1
    1
    2
    3
    5
    8
    13
```

## Study 4 special iterator: generator

In study 3 we give an example of an iterator that computes the elements on the fly.
This is such a common pattern that Python has syntactic sugar for that.

There are special functions - still defined with `def`, but they have `yield` somewhere in their body. 
When you call them, they are not executed.
Instead, some magic Python code is run, and that converts the function body into an iterator.
That iterator is returned.

Sounds complex, [study 4](study4.py) shows an example, using the Fibonacci sequence we also studied in study 3.

### Study 4 - generator function

This below function is a _generator_ of all Fibonacci numbers.
The function body has the keyword `yield`, a trigger for the Python interpreter that this is a special function.

A function that contains a `yield` statement is called a "generator function", see [PEP 0255](https://www.python.org/dev/peps/pep-0255/).
A generator function is an ordinary function object in all respects, 
but when a generator function is called, no code in the body of the function is executed. 

Instead a generator-iterator is returned.
The generator-iterator object conforms to the iterator protocol, i.e. it has a `next()`.
The value returned by `next()` is the expression passed to `yield`.

The generator function may have multiple `yield` statements, each `next()` runs until `yield` 
(and starts where the previous `yield` stopped).
If the function returns (with an explicit `return` statement, or implicitly at the end of the function), 
the iterator stops.

```python
def fib() :
    a = 0
    b = 1
    while True:
      yield a
      a,b = b,a+b
```

As we see, this [study 4](study4.py) code is shorter than the `Fibonacci` in [study 3](study3.py).

### Study 4 - for-in

We can now call the function `fib()`. It returns an iterator, so it can be used in a for-in loop.
The iterator never stops by itself, so again we have an emergency break.

```python        
for element in fib() :
    print( "   ", element )
    if element==13 :
        break # Emergency break
```

with the expected result

```text
  study4 - for-in
    0
    1
    1
    2
    3
    5
    8
    13
```

### Study 4 - life-cycle

I was wondering about the life-cycle of the generator. What is what and when :-).

I made this generator-function; it yields 1 and 2, but prints A, B and C around those yields.

```python
def lifecycle():
    print("    A")
    yield 1
    print("    B")
    yield 2
    print("    C")
```

Let's first check the types.

```python
print( "   ", lifecycle )
lc = lifecycle();
print( "   ", lc )
it = iter(lc)
print( "   ", it )
```

The first output is not really a surprise, `lifecycle` is a _function_.
Then we call that function, and store the result in `lc`.
The next print, of `lc`, matches the Python documentation. The `lifecycle` body is not run, 
which is confirmed by not getting any output, not even "A". Instead, what is returned
is a _generator_.

Then comes a bit of a surprise. The generator is an _iterable_. 
This follows form the fact that we are able to call `iter()` on `lc`. 

```text    
    <function lifecycle at 0x000001687714E310>
    <generator object lifecycle at 0x000001687713F9E0>
    <generator object lifecycle at 0x000001687713F9E0>
```

This is a bit contradicting the documentation, which says 

> When a generator function is called [...] no code in the body of the function is executed. 
> Instead a generator-iterator object is returned

So it clearly says an _iterator_ is returned.
What we see is that an iterable is returned, because it allows `iter()`.
Note however that the returned iterator is the _same_ object as the iterable (same address).
So the iterable is its own iterator - just as we had in study 1.
Since a for-in loop needs an iterable, it is very convenient that the returned generator object is both.

Let's now use the generator: three discrete steps to get a `next()` value - trapping `StopIteration`.

```python
print("    --------")
try :
    print( "   ", next(lc) )
except StopIteration:
    print( "    StopIteration" )
print("    --------")
try :
    print( "   ", next(lc) )
except StopIteration:
    print( "    StopIteration" )
print("    --------")
try :
    print( "   ", next(lc) )
except StopIteration:
    print( "    StopIteration" )
print("    --------")
```

We see that only now the first "A" comes out. So the generator body is only run once we call
the first `next()`; it prints "A" and yields 1. 
The "B" prints in the second `next()` which yields 2.
The third next prints "C", does not yield, but instead raises `StopIteration`.

```text    
    --------
    A
    1
    --------
    B
    2
    --------
    C
    StopIteration
    --------
```


### Study 4 - observations

Iterators and general and generators specifically have a prominent role in Python.

For example, they exist in generator comprehensions

```python
>>> g = (i*i for i in [1,2,3,4,5])
>>> print(g)
<generator object <genexpr> at 0x0000022FF2829510>
>>> print( list(g) )
[1, 4, 9, 16, 25]
```

They have even special syntax features (drop parenthesis) for iterator eating functions

```python
>>> sum( (i*i for i in [1,2,3,4,5]) )
55
>>> sum( i*i for i in [1,2,3,4,5] )
55
```

They also seem to be the basis of the `range` function.
That is a bit harder to proof because that object is a specialty anyhow

```python
>>> r = range(6)
>>> print(r)
range(0, 6)
>>> type(r)
<class 'range'>
```

but its implementation size does not grow with the range it spans.

```python
>>> sys.getsizeof(range(1))
48
>>> sys.getsizeof(range(1000))
48
>>> sys.getsizeof([1])
64
>>> sys.getsizeof([1,2,3,4,5,6,7,8,9,10])
152
```


## Study 5 nested generators

In [study 5](study5.py) we push generators to the limit.

A container can contain, say, two sub containers. 
Is it possible that a generator contains two sub generators?

Of course the iterator of the container would iterate the first sub container, and then the second.
Likewise, the generator would first generate the first sub generator, and then the second.

And yes, Python supports this.

### Study 5 - power

Let's start slowly.
We have a generator `pow(base)` that generates the first five powers of `base`.

```python
def pow(base) :
    for exp in range(5) :
        yield base ** exp
```

If we call that for base 10,

```text
print("  study5 - pow")
for element in pow(10) :
    print( "   ", element )
```

it generates the first 5 powers of 10.

```text
  study5 - pow
    1
    10
    100
    1000
    10000
```

### Study 5 - nested yield

Let's now make a generator that contains two sub generators, each of `pow` but with a different base.

```python
print("  study5 - nested yield")
def dualpow1(base1,base2) :
    for elm in pow(base1) :
      yield elm
    for elm in pow(base2) :
      yield elm

for element in dualpow1(2,3) :
    print( "   ", element )
```

This works fine

```text
  study5 - nested yield
    1
    2
    4
    8
    16
    1
    3
    9
    27
    81
```

### Study 5 - nested yield-from

But the above has a more Pythonic way: yield-from.

```python
print("  study5 - nested yield-from")
def dualpow2(base1,base2) :
    yield from pow(base1)
    yield from pow(base2)
        
for element in dualpow2(2,3) :
    print( "   ", element )
```

which gives the same results:

```text
  study5 - nested yield-from
    1
    2
    4
    8
    16
    1
    3
    9
    27
    81
```

I agree that `yield from xxx` is a bit shorter than `for elm in xxx: yield elm`, but not that much shorter.
Why does Python have this new construct?

As [PEP380](https://www.python.org/dev/peps/pep-0380/) explains

> However, if the subgenerator is to interact properly with the caller in the case of calls to 
> send(), throw() and close(), things become considerably more difficult. 
> As will be seen later, the necessary code is very complicated, and it is tricky to handle all the corner cases correctly.

We did not yet study `send()`, and we won't for now. But in a nutshell
- `next(gen)` returns val, assuming `gen` hits the statement `yield val`.
- `gen.send(val)` makes `x=yield` in `gen` assign `val` to `x`.
- If `gen` has `x=yield y`, the value of `y` is yielded by `next` and a value `send` is assigned to `x`.

Let's forget about `send()`.

### Study 5 - recursion

Just to stretch the limits.
A generator is a function (that returns an iterator).
Functions can be recursive. Can generators also be recursive?

Yes they can.

The below generator `recursive(base)` iterates over `pow(1)` up to `pow(base)`.
Note the last line in the generator body: a recursive call.

```python
def recursive(base) :
    if base>0 :
        yield from pow(base)
        yield from recursive(base-1)
```

This works as expected. The loop
	
```python
for element in recursive(5) :
    print( "   ", element )
```

returns 25 elements

```text
  study5 - recursive
    1
    5
    25
    125
    625
    1
    4
    16
    64
    256
    1
    3
    9
    27
    81
    1
    2
    4
    8
    16
    1
    1
    1
    1
    1
```


## Study 6 generator types

[Study 6](study6.py) is the last study. We look at the _types_ yielded by generators.

### Study 6 - multiple types

Syntactically, a generator looks like a function, with `return expr` replaced by `yield expr`.
For each `next()` the generator yields the computed `expr`.
Python is dynamically typed: a generator body may contain multiple `yield`s, 
each `yield` has its own expression, and each of those can potentially have a different type.

Is that allowed? yes. Is that useful? probably not.

Let's go for the extreme,

```python
def gentypes() :
    yield 1
    yield "two"
    yield True
    yield None
    yield
    yield 6
```

and see what this yields

```python
for element in gentypes() :
    print( "   ", element, "-", type(element).__name__ )
```

Actually, no surprises with Python's dynamic typing.

```text
  study6 - multiple types
    1 - int
    two - str
    True - bool
    None - NoneType
    None - NoneType
    6 - int
```

Note that like `return` the expression of `yield` may be absent, this means that `None` is yielded, as shown in the test above.

### Study 6 - side effect

Is it useful that a (plain) function has no `return` statement, or only "empty" ones?
Maybe no, because the function does not compute any value.
But yes, it is useful if the function has _side effects_.
In the good old days of the Pascal language, 
functions returning a value were declared as _function_ and functions returning nothing/None/void as  _procedues_.

The same usefulness considerations hold for generators.
The `yield` may be without an expression, but then the generator should have a side-effect.

```python
# Generator that only has side effects
def sideeffect(n) :
    for i in range(n) :
        print( "   ", i, "!" )
        yield
```

We can now loop over the elements, but all elements are `None`. So we have an empty body.

```python        
for element in sideeffect(6) :
    print( "   ", element)
```

Twelve lines are printed, 6 in the for-in and 6 as side effect.
```text
  study6 - side effect
    0
    None
    1
    None
    2
    None
    3
    None
    4
    None
    5
    None
```

Maybe this for-in loop is more appropriate
```python
for element in sideeffect(6) :
    pass
```

## Conclusion

- We have studied _iterables_, data structures that have an `__iter__()` member function, which returns an _iterator_.
- An _iterator_ has a member function `__next__()`, which returns the next value (or raises `StopIteration`) from the iterable.
- The iterable can be its own iterator, but that blocks using two iterators at the same time.
- An iterator can exist without iterable (container), if it _computes_ the elements instead of producing the one from the container.
- A generator is a function with `yield` in the body; it is a compact way to write a computing iterator.
- Generators may yield `None` in which case the generator needs to have a side effect.

The last conclusion is the basis for cooperative multitasking. See the next [study](../tasksstudy/readme.md) for details.

(end)
