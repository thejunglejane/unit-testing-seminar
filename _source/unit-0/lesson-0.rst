Lesson 0
========

In this lesson, we'll ask the motivating question behind unit testing:
“how do you know that your code is doing what you think it’s doing?”

Consider the following code:

.. code:: python

   def is_even(n):
       '''Return True if ``n`` is an even number, otherwise return False.'''
       if n % 2 == 0:
           return True
       return False


   def is_odd(n):
       '''Return True if ``n`` is an odd number, otherwise return False.'''
       if n % 2 != 0:
           return True
       return False


   def is_composite(n):
       '''Return True if ``n`` is a composite number, otherwise return
       False.
       '''
       for i in range(n):
           if n % i == 0:
               return True
       return False


   def is_prime(n):
       '''Return True if ``n`` is a prime number, otherwise return False.'''
       for i in range(n):
           if n % i == 0:
               return False
       return True


How can you determine whether each of these functions is working, i.e.,
that each function is doing what you think it’s doing?

One approach is to come up with a set of known inputs and outputs, call
our function(s) with each input, and ensure that we get the expected
output. This is, essentially, unit testing.
