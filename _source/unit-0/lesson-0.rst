Lesson 0
========

In this lesson, we'll ask the motivating question behind unit testing:
“how do you know that your code is doing what you think it’s doing?”

Consider the following code:

.. literalinclude:: examples/numbers.py

How can you determine whether each of these functions is working, i.e.,
that each function is doing what you think it’s doing?

One approach is to come up with a set of known inputs and outputs, call
our function(s) with each input, and ensure that we get the expected
output. This is, essentially, unit testing.
