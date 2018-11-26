Lesson 2
========

In this lesson, you’ll see how to write and run unit tests and how to
read unit test results.

Unit Test Example
-----------------

.. note::
   All of the examples in this repository use Python’s built-in
   ```unittest```_ library. This is not the only library that you can
   use to write unit tests in Python. I prefer ``unittest`` to other libraries and frameworks for a couple of reasons, but it’s less
   important which library or framework you use *as long as you’re
   writing tests*. If you want to use ```pytest```_ instead of
   ``unittest`` you have my blessing!

Below is a test case with four test methods: ``test_is_even``,
``test_is_odd``, ``test_is_composite``, and ``test_is_prime``. Each of
these test methods is a unit test. We know this because, in
``unittest``, any method on a ``TestCase`` class whose name begins with
``test_`` is considered a test.

.. literalinclude:: examples/test_numbers.py

Anatomy of a Unit Test
----------------------

Every unit test, whether you’re using ``unittest`` or ``pytest`` or some
other testing library or framework, has two basic steps:

1. The code under test is invoked
2. An assertion is made

Assertions
~~~~~~~~~~

In ``unittest``, assertions are made using ``assert*`` methods on the
test case. You can read about the available assertion methods `here`_.
In ``pytest``, assertions are made using the bare ``assert`` keyword.
For example, our ``test_is_prime`` unit test would look like this in
``pytest``:

.. code:: python

   def test_is_prime():
       assert is_prime(3)
       assert not is_prime(4)

In either framework, if the assertion fails, an ``AssertionError`` will
be raised, and the test will fail. If an exception other than
``AssertionError`` is raised, the test will error. Finally, if no
exceptions are raised, the test will pass.

.. note::
   Errors are not the same as failures; an error indicates that the
   test didn’t execute properly, while a failure indicates that the
   test *did* execute properly but the assertion condition didn’t hold.

Anatomy of a Unit Test Result
-----------------------------
Let's run our tests and look at the results:

.. code::

   python test_numbers.py
   E..E
   ======================================================================
   ERROR: test_is_composite (__main__.NumbersTestCase)
   ----------------------------------------------------------------------
   Traceback (most recent call last):
     File "examples/test_numbers.py", line 16, in test_is_composite
       self.assertFalse(numbers.is_composite(3))
     File "unit-0/examples/numbers.py", line 20, in is_composite
       if n % i != 0:
   ZeroDivisionError: integer division or modulo by zero

   ======================================================================
   ERROR: test_is_prime (__main__.NumbersTestCase)
   ----------------------------------------------------------------------
   Traceback (most recent call last):
     File "examples/test_numbers.py", line 20, in test_is_prime
       self.assertTrue(numbers.is_prime(3))
     File "unit-0/examples/numbers.py", line 28, in is_prime
       if n % i == 0:
   ZeroDivisionError: integer division or modulo by zero

   ----------------------------------------------------------------------
   Ran 4 tests in 0.001s

   FAILED (errors=2)

So what happened?

.. _here: https://docs.python.org/3/library/unittest.html#test-cases
