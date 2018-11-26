Lesson 1
========

> Code that can't be tested won't be tested.

In this lesson, you'll learn about some untestable `code smells`_.
There are more than we have time to cover here, so we'll focus on some
of the most common ones.

Untestable Code
---------------

What is untestable code? Very simply, it's code that's difficult or
impossible to test. Learning to detect untestable code early, and
learning to avoid writing untestable code in the first place, will save
you a lot of time.

Heavy-Duty Constructors
~~~~~~~~~~~~~~~~~~~~~~~

A constuctor is an ``__init__`` method on a class. If an object's
constuctor does a lot of work, it will be very difficult to recreate
that object in a test fixture. This can be especially bad if one of the
things your constructor does is construct other hard-to-construct
objects.

Related to this is writing functions or methods that take a large
number of parameters as input. Creating all the objects that you need
in order to even get your code into a testable state is challenging.

Side Effects
~~~~~~~~~~~~

A side effect is when a piece of code modifies some state outside of
it's local scope. This could be setting attributes on a class,
changing a global variable, etc. Side effects make code difficult to
use because they're generally not well-communicated to the user or
require the user to call different parts of the code in a specific
order. They make code difficult to test for the same reasons.

Lots of If Statements
~~~~~~~~~~~~~~~~~~~~~

The more ``if`` statements you have, the greater the number of possible
execution paths that you'll need to test for. This is made even worse
if you have a lot of nested ``if`` statements.  
One thing you can do if you find yourself in this situation is to try
to express your conditionals more concisely: instead of adding an ``if``
for every condition you can think of, look to see which conditions
follow the same code path or return the same result and group them into
a single ``if`` statement.

.. _code smells: https://blog.codinghorror.com/code-smells/
