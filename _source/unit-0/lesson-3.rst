Lesson 3
========

In this lesson, you'll learn why it's important to write unit tests.

Why should you write unit tests?
--------------------------------

In the remaining lessons we're going to dig deeper into how to write
unit tests, but before we get there we need to understand why we're
writing unit tests in the first place. We already know that automated
unit tests have some advantages over manual tests of our code, but we
also know that unit tests can't prove that our code is correct. So, why
should we spend time writing unit tests?

Proper Functioning
~~~~~~~~~~~~~~~~~~

The first one we already know: unit tests ensure that our code works,
under a given set of conditions and for some definition of "works".
They don't guarantee that our code will work in all conditions, or that
it does everything correctly, and that's not the goal. The goal is to
try to test for a reasonably-complete set of conditions and criteria,
not an exhaustive set. We'll discuss how to pick which unit tests you
need in Unit 1 Lesson 1.

As we just saw in Lesson 2, having unit tests in place can help catch
all kinds of errors in code. In fact, a study published in USENIX
OSDI'14 concluded that 58% of catastrophic failures across 200
distributed systems could have been prevented with basic test coverage.
Just *basic* test coverage.

Detecting Regressions
~~~~~~~~~~~~~~~~~~~~~

A regression is when code that was working previously stops working.
Having unit tests in place is incredibly helpful for detecting
regressions, especially when you're refactoring (like we just did in
Lesson 2). Whenever you change code, you run the risk of breaking
something that used to be working, i.e., introducing a regression.
Sometimes, the code you broke is the code you just changed, but other
times the code that breaks as a result of your change is somewhere else
in your codebase. Even if you're diligent about manually testing the
code you're actually changing, it's really hard to track down all the
other parts of your codebase that may have been affected by your change
and ensuring that they still work. Having unit tests in place that you
can easily run can help detect these regressions across your codebase.

Another place where unit tests come in handy is when you need to
upgrade packages. The **only** safe way to upgrade a package (or
upgrade Python versions) is to start with a well-tested codebase. By
safe we mean "without breaking existing functionality".

Thinking Through Failure Modes and Edge Cases
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When we're writing code, we're often focused on how we expect our code
to work, and we're not so focused on how it's going to fail. But,
thinking through how our code is going to fail can help uncover logical
errors in our program and help identify edge cases that need to be
handled with special logic. For example, 0 and 1 are neither prime nor
composite numbers, so ``is_prime`` and ``is_composite`` should have
special handling for 0 and 1. After adding this special handling, it's
a good idea to add (and run!) tests for 0 and 1 specifically.

.. code:: python

    def test_0(self):
        self.assertFalse(numbs.is_composite(0))
        self.assertFalse(numbs.is_prime(0))

    def test_1(self):
        self.assertFalse(numbs.is_composite(1))
        self.assertFalse(numbs.is_prime(1))

Unit testing forces you to think through how your code could fail and
encourages you to write tests that ensure your code does the right
thing under those conditions. Thinking through this up front means
fewer headaches for you in the future when more people are using your
code in more ways.

Factoring Code
~~~~~~~~~~~~~~

It is a lot easier to test code that is factored into discrete units
that each do one thing and it is a lot easier to test code that is
loosely coupled, meaning it doesn't rely on the internals of some other
system and no other system relies on its internals.

Factoring and loose coupling are generally considered to be hallmarks
of good system design. Because well-factored, loosely coupled code is
easier to test, unit testing incentivizes us to write well-factored,
loosely coupled code. It's a really good instance of making the right
thing to do the easy thing to do. This is what people mean when they
say "unit testing helps you write better code".

Why should *data scientists* write unit tests?
----------------------------------------------

If you're a data scientist or researcher (like me), you've probably
heard someone, probably an engineer, bemoan the "fact" that data
scientists and researchers don't write unit tests or tell you that you
should really be writing unit tests. What are they actually trying to
say?

One of the reasons that many data scientists and researchers don't write
unit tests is that the code we write is stochastic: it doesn't produce
the exact same result every time we run it. Testing stochastic code is
difficult, and we'll get into how to test stochastic programs in
Unit 4 Lesson 0.

Another reason that many data scientists and researchers don't write
unit tests is that we're often working in Jupyter notebooks or in
standalone Python scripts, and we're usually the primary consumers of
our code. We don't really have users with requirements that we have to
satisfy.

So, why should we be writing unit tests, or why are all these engineers
telling us that we should be writing unit tests, if it's less
straightforward for us and is seemingly less important?

Safely Upgrading Packages
~~~~~~~~~~~~~~~~~~~~~~~~~

One big reason is that engineers are probably responsible for providing
you with a working development environment. At times, they may need to
upgrade packages to patch security holes, or upgrade everyone to Python3
because Python2 is end-of-lifed. The only way to safely upgrade versions
is to start with a well-tested codebase. You help them help you by
testing your code.

"It Worked on My Machine"
~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../_static/whale.jpg
   :align: center

Some data scientists and researchers build models that are eventually
handed over to engineers to deploy into a production environment. Tests
help engineers ensure that they didn't break anything during that
transition. No one is going to be happy if your model breaks on it's
first day in production, and no one is going to be happy if you learn
weeks or months down the line that your model has been failing silently
in it's new environment. Having tests in place helps engineers ensure
that your model is working the same way in production as it did in your
development environment.

Isolating Changes in Results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

So what's in it for you? The biggest thing is that unit tests help you
isolate changes in your results to changes to your input data or changes
to your model, rather than the code malfunctioning. Without unit tests
in place, it’s hard to determine if changes in your results are a side
effect of the code not doing what you expect it to do rather than a
“legitimate” result.

Reusing Your Code
~~~~~~~~~~~~~~~~~

Unit tests force you to break your code down into components that are
easy to test. Often, those components are also easy to reuse. If you
find yourself copying cells from Jupyter notebook to Jupyter notebook,
you're probably not excited about writing tests for each notebook
separately. This can incentivize you to factor the code in those cells
out into a package or library that you can import into all of your
Jupyter notebooks, and now you only have to test it in one place. Being
able to reuse your code saves you time but also makes you consistent,
which is an important part of research hygiene.
