Lesson 0
========

In this lesson we'll learn some good unit-test patterns and some
anti-patterns to avoid.

Unit Test Patterns
------------------

At this point you've seen some example unit tests and have hopefully
tried writing a couple of them yourself. Now, we're going to cover some
unit test best practices.

Isolation
~~~~~~~~~

The first best practice is that your unit tests should be isolated,
from each other but also from external services or libraries. By
isolating our tests in this way, we localize test failures to the code
that's actually under test, meaning that test failures are much easier
to debug, and we'll be incentivized to factor our code into loosely
coupled components.

One of the ways you isolate your tests is by writing separate test
methods (rather than one big test method with a bunch of code calls
and assertions in it). Behind the scenes, :mod:`unittest` calls the
:meth:`~unittest.TestCase.setUp` and :meth:`~unittest.TestCase.tearDown`
methods before and after each individual test method is run to help
ensure that each test is running with a "clean slate". You should make
sure that your :meth:`~unittest.TestCase.tearDown` methods clean up
after each of your tests so they don't leak into the next test that's
run.

Mocking
"""""""
The best way to isolate your tests from external services or libraries
is to mock those external services/libraries. The way this works is you
create a mock of the external service/library that exhibits the same
behavior as the real service/library, and use the mock in your test
instead of the real object. You can make assertions about how your code
interacted with the mock without actually relying on the real object
being mocked.

The :mod:`unittest.mock` module provides resources for creating mocks
for your unit tests.

It is possible to over-mock your unit tests, which is an anti-pattern
that we call out below.

Single-Purpose
~~~~~~~~~~~~~~

This applies to tests just as much as it applies to code. In general,
we want each of our unit tests to test for just one thing. That doesn't
mean that each test method should only make one assertion; rather, it
means that each test should be focused on testing one condition and one
expectation. Another way of putting this is that a test should fail for
one reason: that the unit under test failed to meet expectation X under
condition Y.

Explicit
~~~~~~~~

Each unit test should be explicit about what it's testing. In other
words, it should be easy to tell from reading the code what the test is
doing. This is a general principle of code, but it is uniquely
important when it comes to testing. The more convoluted your code
becomes, the less certain you can be that it's working correctly. If
you feel like you have to write unit tests for your unit tests to
ensure that they're working, then you need to make your tests simpler
and more explicit.

Easy Set-Up
~~~~~~~~~~~

This is related to the principle above, and to the principle below. It
should be easy (and quick) to set up and tear down your tests. If your
tests require really complicated setup, you may consider creating
separate test cases, each with their own
:meth:`~unittest.TestCase.setUp`. This can bring down the complexity of
your setup. If you can't simplify the set up by creating separate test
cases, you may be testing code that takes too many inputs. In this case,
you should try to break your code into smaller pieces that each take
fewer inputs.

Fast
~~~~

Finally, your unit tests should be fast -- they should execute in a
matter of milliseconds, ideally. The reason for this is that, if your
tests take a long time to run, you'll run them less frequently, and
tests are only effective if they're being run.

Sometimes, you'll wind up with tests that take a while to run, and
there's nothing you can do about it; you need those tests. What you can
do in this scenario is put your long-running tests in a separate file
or folder. This allows you to keep frequently running your fast tests
and run your slow tests less frequently.

Reproducible
~~~~~~~~~~~~

This might seem obvious, but running the same test multiple times in a
row should yield the same results. If not, there's a problem somewhere
in your :meth:`~unittest.TestCase.setUp` or
:meth:`~unittest.TestCase.tearDown` (are you generating a random number
in your set up?), or you've got a `race condition`_ in your code.


Unit Test Anti-Patterns
-----------------------

There are several anti-patterns that you should try to avoid. Remember
that these aren't strict rules, and there are always exceptions. Use
your head.

You can find a great catalog of unit testing anit-patterns on
StackOverflow `here`_. I'll call out a few of them here:

* The Mockery
* The Hidden Dependency
* The Local Hero
* The Inspector
* The Happy Path
* The Butterfly

.. _here: https://stackoverflow.com/questions/333682/unit-testing-anti-patterns-catalogue
.. _race condition: https://dwheeler.com/secure-programs/Secure-Programs-HOWTO/avoid-race.html
