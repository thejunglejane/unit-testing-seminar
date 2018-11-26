Lesson 1
========

In this lesson, we'll learn how to pick which unit tests to write. This
is one of the biggest hurdles for people that are new to testing.

Test Planning
-------------

Test planning is the process of determining what conditions and
functionality you're going to test for. When you sit down to actually
write your tests and implement your code, you may find that some tests
aren't needed or that you forgot to plan for some tests, and that's
okay. The goal of test planning is to think holistically about what
tests you need.

Depending on your experience, your group's processes, and the size or
complexity of the codebase you're testing, you may or may not write
your test plan down. You might show it to other people for feedback, or
you might keep it to yourself. As long as you're thinking about what
tests you need, you're test planning.

As you get more experience writing tests, your test plans, and your
tests in general, will probably start to look different. When you start
out, it's best to focus on making sure you're testing for the
conditions and functionality that you need to work as completely as
possible. Don't worry too much about repeating yourself in your tests;
you can worry about writing `DRY`_ tests later.


.. todo:: Don't test your dependencies

Bread & Butter
~~~~~~~~~~~~~~

These are the obvious things that just have to work. A good place to
look for these bread-and-butter tests is in the name and/or docstring
of the thing that you're testing, whether you're testing a function,
method, class, module, whatever. For example, it's easy for me to assume
that ``is_even`` should return True for even numbers and False for odd
numbers, which is just what the docstring says.

Another good place to look for bread-and-butter tests is in a
requirements spec or in the acceptance criteria, if applicable. These
are probably less common in research, where people are mostly writing
code for themselves rather than for others.

Edge Cases
~~~~~~~~~~

Are there any edge cases that require special handling? In our example,
0 and 1 require special handling because they're neither composite nor
prime. Conditional statements (i.e., ``if`` statements) are good places
to look for edge cases in your code that should be tested. If edge
cases aren't already being handled in your code, thinking through them
while you're test planning is a good opportunity to figure out what
special handling needs to be added.

.. note::
   Pro tip: if you think of an additional edge case that needs to be
   handled in your code, add a test for it *before* you handle it. Your
   test will start passing as soon as you finish implementing the
   special handling correctly and you'll know that you're done
   implementing!

Failure Modes
~~~~~~~~~~~~~

What inputs would break your code? For example, what would our code do
if someone provided a :py:class:`float` instead of an :py:class:`int`?
Let's add some logic to our code to make sure that the user passes an
:py:class:`int`:

.. code:: python

   def is_even(n):
       '''Return True if ``n`` is an even number, otherwise return False.'''
       if not isinstance(n, int):
         raise TypeError

       if n % 2 == 0:
           return True
       return False

To make sure that we're handling non-integers correctly, we can add a
test that passes a non-integer to our function and makes sure that a
``TypeError`` is raised. To do this, we'll use the ``assertRaises``
method:

.. code:: python

   def test_is_even_non_integer(self):
      self.assertRaises(TypeError, numbs.is_even(1.5))


Code can break for other reasons than bad inputs, too. For example, if
your code depends on a database connection, what would happen if that
database wasn't available? What about if your query returned 0 records?

There may be failure modes that you think up that don't become items in
your test plan. Some failure modes will become edge cases that will be
handled specifically (and have tests that ensure they're handled
correctly), while others will be documented without being handled
explicitly. Even if they don't make it into your test plan, it's
valuable to think through how your code will fail.

Test Coverage
-------------

Test coverage refers to what percentage of your codebase is exercised
by your tests. This metric is calculated by executing your tests and
determining which lines of code were executed while doing so. It's not
a perfect measure, because there's no guarantee that executing a line
of code within a test means you're testing that line well (or at all),
but it can help you identify areas of your codebase that aren't being
tested at all.

You can use the `coverage`_ package to calculate test coverage for your
Python programs.

.. code:: bash

   $ pip install coverage
   $ coverage run --omit test_numbs.py test_numbs.py
   $ coverage report
   Name       Stmts   Miss  Cover
   ------------------------------
   numbs.py      22      2    91%

We omit test_numbs.py because that's our test file and it doesn't really
make sense to calculate coverage for that because it will trivially be
100%.

Our tests cover 91% of numbs.py, but we're missing two statements. To
see what those statements are, we can generate an html report:

.. code:: bash

   $ coverage html
   $ (cd htmlcov; python -m http.server 8000)

Navigate to localhost:8000 in your browser and you'll see the same
coverage information, but in the browser we can click into individual
files and see which lines are uncovered by tests. It looks like our
tests don't cover the special handling of 0 and 1.

Let's add the following tests to test_numbs.py:

.. code:: python

    def test_0(self):
        self.assertFalse(numbs.is_composite(0))
        self.assertFalse(numbs.is_prime(0))

    def test_1(self):
        self.assertFalse(numbs.is_composite(1))
        self.assertFalse(numbs.is_prime(1))

and run our tests under coverage again:

.. code:: bash

   $ coverage run --omit test_numbs.py test_numbs.py 
   $ coverage report
   Name       Stmts   Miss  Cover
   ------------------------------
   numbs.py      22      0   100%

Adding those two tests brings our test coverage up to 100%!

It's natural to want to achieve 100% test coverage for all your code,
but this is a trap. It's possible to have 100% test coverage and not be
testing the important behaviors of your code at all, and spending time
testing every last line of code isn't necessarily adding a lot of value
beyond getting that coverage metric to 100%. You should put more stock
in your test plan than in your coverage metric, and use your coverage
metric to identify gaps in your test plan that you can triage.

.. _DRY: https://en.wikipedia.org/wiki/Don%27t_repeat_yourself
.. _coverage: https://coverage.readthedocs.io/en/v4.5.x/#
