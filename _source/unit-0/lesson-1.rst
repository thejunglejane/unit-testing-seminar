Lesson 1
========

In this lesson, we’ll define what a unit test is.

What is a unit test?
--------------------

So what is a unit test? Let’s break it down.

The “unit” in “unit test” refers to the code under test. It’s called a
“unit” because a unit is considered indivisible. Why is this important?
We want our unit tests to be isolated from one another. We need this
isolation so that unit test failures are localized to the code under
test and aren’t confused by errors elsewhere. One way of achieving this
isolation is to test each individual part of our code separately, and we
do that by breaking the code down into indivisible units and testing
each one separately.

The “test” in “unit test” is the verification of the unit under test
against a set of formal requirements. Note that there’s nothing about
verifying that the code under test is *correct*, which is a common
misconception.

So, a unit test is a separate piece of code that verifies that a unit of
code meets a formal set of requirements.

Automated v. Manual Testing
---------------------------

In general, “unit testing” refers to automated testing where tests are
run by a machine (as opposed to manual testing where a human tests the
code by running it “by hand” to try to find errors).

You *can* manually test that a unit of code meets a formal set of
requirements, but having a machine run the tests for you has several
advantages:

#. Automated tests are faster
#. Automated tests are more consistent
#. You can test more things
#. Automated tests are easier to maintain
