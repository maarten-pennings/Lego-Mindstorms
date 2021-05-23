# Cooperative multi tasking study

This directory contains some python projects with the aim to develop cooperative multi tasking in Lego Mindstorms 4 Robot inventor.
However, this study is Python (on a PC) only.

The core of the mechanism is _generators_.

To understand those, see the precursory [study](../iteratorstudy) for details.


## Introduction

The crux of a generator is that it runs from `yield` to `yield` on every call to `next()`.

So we can write a function with all kinds of "normal processing" (a sequence of statements, even with `if`s or `while`s)
and intersperse a `yield` now and then. Each time `next()` is called the function progresses to the next `yield`.
The `yield`s themselves have no expression, so the only thing that matters are the side-effects between the `yield`s.

Now we take a mental context switch.

Consider a multi tasking environment.
Multiple _tasks_ are running in parallel.
Each task has its own _task function_ - the function that is run for that task.
Typically that function is a never ending loop.

In a _preemptive_ system, the tasks (their task functions) run in parallel and can be stopped and continued by the kernel
at more or less arbitrary moments. Exceptions as critical sections made with e.g. mutexes.

However, also _cooperative_ multi tasking systems exist.
Here, the tasks must voluntarily give up the cpu and allow another task to become computable.
There is an api of the kernel that contains functions to (may) cause a task switch.

The down side of cooperative kernels is that a run-away task "kills" the system.
If a task never gives up the cpu, others will never run. bad.
On the up side, it is much easier to write a program for a cooperative kernel, since there is task switching at arbitrary moments.
Every sequence of statements is a non-preemptable section ("critial section") until an explicit "switch task" call.

Another down side of preemptive kernels is that they are harder to implement.
Lego Mindstorms 4 Robot Inventor does not yet support it.
The underlying micro python does support this at [experimental level](https://docs.micropython.org/en/latest/library/_thread.html).

> This module is highly experimental and its API is not yet fully settled and not yet described in this documentation.

Now take a mental step.

Think of generators again. Sequence of statements running from yield to yield. 
Thinks of those yields as the "give up cpu" call to the kernel.
And we have our free cooperative multi tasking system.

This is very close to a main loop calling fragments of code.
But generators is better, because a long fragment of code (taking 5x the time it is deemed good for responsiveness or deadline)
does not need to be cut in fragments; we can just keep the one big fragment and have yields at appropriate places.

## Setup

To replicate the study, open a command shell (`cmd`) and run first `setup.bat`, then `run.bat`.
For details see the [iterator study](../iteratorstudy/readme.md#Setup)


## Program 1 - tick tock

Let's begin very simple.

[Program 1](prog1.py) has a task function that prints a counter that is repeatedly stepped.
The task function has two start-up parameters: its name and the initial value of the counter.

Note that this task function is a generator function; it has a `yield` between each steps.

```python
def task_main(lbl="label",start=0) :
    counter = start
    while True:
        print( f"  {lbl} {counter}")
        step += 1
        yield 
```

Next, we create two tasks.

```python
task_a = task_main("tick",0)
task_b = task_main("tock",100)
```

And then we start the cooperative kernel.
This could run indefinitely, so we force stop after 5 cycles.

```python
for _ in range(5):
    next(task_a)
    next(task_b)
```

This is the output.

```text
prog1 - tick tock
  tick 0
  tock 100
  tick 1
  tock 101
  tick 2
  tock 102
  tick 3
  tock 103
  tick 4
  tock 104
```

## Program 2 - writer reader

The previous program is named after Intels tick/tock strategy.
The first task makes one step (tick) then the other task makes one (tock), 
and so on (tick, tock, tick, ...).

The next example, [program 2](prog2.py) is a bit more realistic.
We have one task (writer) that adds numbers to a global queue, 
and another task (reader) that removes those numbers from the queue.

```python
queue = []
```

In the real world, the writer is maybe handling incoming bytes of the serial port.
To make it somewhat realistic, the writer in this example acts randomly, 
it has a 1 in 100 change to write numbers, the count of bytes being written is random 
between 1 and 5.

For debugging the writer `print`s how many bytes were added to the `queue`.

```python
def task_writer() :
    val = 100
    while True:
        arrive = random.randrange(100)<1
        if arrive :
            count = random.randrange(1,6)
            yield
            print( f"  w: {count}" )
            for _ in range(count) :
                queue.append(val)
                val += 1
        yield 
```

Note that the writer has two `yield`s (more are possible).
But an important choice made, is that the append loop does not contain a `yield`.
This means that writing the `count` numbers is an atomic action: no task switch is possible in between.

If we look at the reader we see a similar aspect.
If the `queue` is filled, it is emptied in one `while`, no `yield` in between.

```python
def task_reader() :
    while True:
        while len(queue)>0 :
            elem = queue.pop(0)
            print( f"  r: {elem}" )
        yield 
```

This completes the task functions.
We create the two tasks, a writer and a reader, and start the kernel.
The kernel is limited to run 1000 cycles, we should expect 10 writes.

```python
# Create the two tasks (with label and start value).
task_w = task_writer()
task_r = task_reader()

# Start the "kernel", let it run for 100 units.
for _ in range(1000):
    next(task_w)
    next(task_r)
```

My run happens to be shorter: only 6 writes.
But we see that if _n_ bytes are written, the reader takes all _n_ in one go.

```text
prog2 - writer reader
  w: 3
  r: 100
  r: 101
  r: 102
  w: 1
  r: 103
  w: 1
  r: 104
  w: 5
  r: 105
  r: 106
  r: 107
  r: 108
  r: 109
  w: 4
  r: 110
  r: 111
  r: 112
  r: 113
  w: 2
  r: 114
  r: 115
```

## Program 3 - time

Most embedded programs use time heavily.

In [program 3](prog3.py), we have two tasks that each control a LED, 
one with a 2 sec toggle period, the other with a 3 second toggle period.

To make timing easier, we have defined a `Timer` class.

```python
class Timer():
    def __init__(self):
        """Creates a Timer and resets it."""
        self.reset()
    def now(self):
        """Returns the time in seconds since the timer was last reset."""
        return time.time() - self.sec0
    def reset(self,target=0):
        """Resets the timer (to `target` seconds)."""
        self.sec0 = time.time()+target
```

Each timer that is created has its own reset moment.

So we can use that have a `clock` that is reset at program startup, and from then one we can use 
`clock.now()` to check how long our program has run. We use this for time stamping log messages.

```python
# Seconds since startup - used for logging
clock = Timer()
```

Both tasks have their own `t=Timer()` to control their LED. Each time the LED toggles,
the timer is reset. Both tasks use the same task function. Upon task creation we pass
which LED to toggle (`lbl` parameter) and how fast (`sec` parameter).

```python
def inc_main(lbl="label",sec=1) :
    t = Timer()
    t.reset(-sec) # Fire now
    n = 0
    while True:
        if t.now() >= sec :
            t.reset()
            print( f"  {int(clock.now())}: {lbl}={n}" )
            n += 1
        yield
```

For logging purposes, the logging moments are counted (`n`).
Also note the trick commented `Fire now`: the timer is set back to force an immediate "fire".

We create a task for LED "a" with a period of 2 and a task for LED "b" with a period of 3 seconds.
```python
task_a = inc_main("a",2)
task_b = inc_main("b",3)
```

We start the kernel and limit it to 500 million cycles.

```python
for _ in range(500_000_00):
    next(task_a)
    next(task_b)
```

Note that each task only does one check `t.now() >= sec`, then yields.
On my PC, python can do that ~20 million times in 1 second.
So, 500 million cycles gives a runtime of ~25 seconds.

``` text
prog3 - time
  0: a=0
  0: b=0
  2: a=1
  3: b=1
  4: a=2
  6: b=2
  6: a=3
  8: a=4
  9: b=3
  10: a=5
  12: b=4
  12: a=6
  14: a=7
  15: b=5
  16: a=8
  18: b=6
  18: a=9
  20: a=10
  21: b=7
  22: a=11
```

Observer that indeed "a" is toggled every 2 seconds (at 0, 2, 4, 6, ...)
and "b" is toggled every 3 seconds (at 0, 3, 6, 9, ...).

## Program 4 - no break up

Remember the promise from the introduction?

> But generators is better, because a long fragment of code 
> does not need to be cut in fragments; 
> we can just keep the one big fragment and have yields at appropriate places.

But what we actually see in program 2 is that we did break up the program.
The while loop has a timer, and each time the timer triggers we take one small action.

In [program 3](prog3.py), we will investigate not breaking up the program.
We have one task that controls LED "a" to switch on for 2 and off for 5.

We do not want "time event handlers":

```python
if t.now() >= onsec  : 
    led_off()
    t.reset()
  
if t.now() >= offsec : 
    led_on()
    t.reset()
```

Rather, we want one simple sequential program

```python
while True:
    led_on()
	wait(onsec)
    led_off()
	wait(offsec)
```

We have the same `Timer` class (and `clock`) as before, but we make a `wait` generator.

```python
def wait(sec):
    t = Timer()
    while t.now() < sec :
        yield
```

This generator keeps on yielding until `sec` has elapsed. That is the side effect.

The task that controls the LED can now indeed be written without breaking up.
The crux here is the `yield` delegation to `wait()`.
Every cycle (every `next()` to `led_main()`) that `wait()` yields (instead of raising `StopIteration`) is yielded by `led_main()`.
As soon as `wait(0` raises `StopIteration`, the `yield from` terminates, and `led_main()` continues with the next `print()`.

```python
# Implements an infinite loop, which switches on LED `lbl` for `onsec` seconds, 
# then switches it off for `offsec` seconds.
# This propagates the yields from the sub-generator `wait()` to the main loop.
def led_main(lbl, onsec, offsec) :
    while True:
        print( f"  {int(clock.now())}: {lbl} on" )
        yield from wait(onsec)
        print( f"  {int(clock.now())}: {lbl} off" )
        yield from wait(offsec)
```

For fun, we create two tasks: "a" 2 on 5 off, and "b" 5 on and 7 off.
We run the kernel for ~25 seconds (see previous section).

```python
task_a = led_main("a",2,5)
task_b = led_main("b",5,7)

for _ in range(500_000_00):
    next(task_a)
    next(task_b)
```

The log is as expected.

```text
prog4 - no break up
  0: a on
  0: b on
  2: a off
  5: b off
  7: a on
  9: a off
  12: b on
  14: a on
  16: a off
  17: b off
  21: a on
  23: a off
  24: b on
```

## Program 5 - globals

[Program 5](prog5.py) is similar to program 4.
It is closer to real embedded software; the LED is now a global variable.

```python
led_a = 0  
def led_a_main(onsec, offsec) :
    global led_a
    while True:
        led_a = 1
        yield from wait(onsec)
        led_a = 0
        yield from wait(offsec)
```

and the same for `led_b`.

We have a helper task to print the LED status.

```python
def log_main():
    while True:
        print( f"  {clock.now():4.1f}: {led_a} {led_b}" )
        yield from wait(0.3)
```

We create two LED tasks and one log task and let them run for a while.

```python
task_a = led_a_main(2,5)
task_b = led_b_main(5,7)
task_c = log_main()

for _ in range(250_000_00):
    next(task_a)
    next(task_b)
    next(task_c)
```

This is the output

```text
prog5 - globals
   0.0: 1 1
   0.3: 1 1
   0.6: 1 1
   0.9: 1 1
   1.3: 1 1
   1.6: 1 1
   1.9: 1 1
   2.2: 0 1
   2.5: 0 1
   2.8: 0 1
   3.1: 0 1
   3.4: 0 1
   3.7: 0 1
   4.0: 0 1
   4.3: 0 1
   4.6: 0 1
   4.9: 0 1
   5.3: 0 0
   5.6: 0 0
   5.9: 0 0
   6.2: 0 0
   6.5: 0 0
   6.8: 0 0
   7.1: 1 0
   7.5: 1 0
   7.8: 1 0
   8.1: 1 0
   8.4: 1 0
   8.7: 1 0
   9.0: 1 0
   9.3: 0 0
   9.6: 0 0
   9.9: 0 0
  10.2: 0 0
  10.6: 0 0
  10.9: 0 0
  11.2: 0 0
  11.5: 0 0
  11.8: 0 0
  12.1: 0 1
  12.4: 0 1
  12.7: 0 1
  13.0: 0 1
  13.4: 0 1
  13.7: 0 1
  14.0: 0 1
  14.3: 1 1
  14.6: 1 1
  14.9: 1 1
  15.2: 1 1
  15.5: 1 1
  15.8: 1 1
  16.2: 0 1
  16.5: 0 1
  16.8: 0 1
  17.1: 0 0
  17.4: 0 0
  17.7: 0 0
  18.0: 0 0
```

## Conclusions

We have seen how
- to write "event" handlers.
- we can use `yield` to skip time.
- we can use `yield from` to delegate waiting to a sub generator `wait()`, allowing us to prevent "break up".

Time to switch to lego Mindstorms 4 Robot Inventor and try this out.

(end)
