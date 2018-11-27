Lesson 0
========

In this lesson we'll sketch out a possible testing workflow for
reproducible science.

Testing Stochastic Programs
---------------------------

Unit testing doesn't translate well to stochastic programs. Unit testing
assumes that you have a concrete expectation that you can test for,
which isn't the case with stochastic programs.

That being said, there are a couple of things we can do to test
stochastic programs.

Testing Distributions
~~~~~~~~~~~~~~~~~~~~~

If you have an expectation about the distribution of your outputs, you
can run your program a bunch of times, collect the outputs, and then
test that they're distributed the way you expect. Of course, these tests
will fail sometimes. This doesn't necessarily mean that there's anythong
wrong with your program (and thus, this is not a "pure" unit test), but
it can prompt you to look at the actual results and make a call as to
whether they look reasonable or not.

Testing Setup
~~~~~~~~~~~~~

In many stochastic programs, there's a lot of setup that needs to happen
before entropy enters your program, and we can test all of that setup.
This is a good idea, because as you iterate on your model you want to
be able to isolate changes in your results to changes in your input data
or changes in your model, not to some unexpected behavior in the setup.

Testing Workflow for Reproducible Science
-----------------------------------------

#. **Begin by prototyping your code in a Jupyter notebook.** This code
   will include your actual model, as well as any setup. Don't worry
   about testing at this stage if it slows you down. Focus on getting an
   idea of how you need to set up your model and what your model's
   outputs should look like.
#. Once you have a good sense of your model's outputs, **add tests for
   the distribution of outputs.** These tests should be *outside* of
   your notebook because they need to execute your notebook several
   times and collect the results of each run. `nbconvert`_ allows you to
   execute Jupyter notebooks from the command line and from Python. See
   `Executing notebooks using the Python API interface <nbconvert>`_ for
   details on how to run Jupyter notebooks from Python. It's important
   to have these tests in place *before* we move to the following steps
   so that we can safely factor our setup code out of our notebook and
   into a package.  #. Factor any setup code into a reusable package,
   and add tests.
#. **Replace setup code in your notebook with imports from your
   package.**
#. **Run distribution tests to determine that steps 3 and 4 didn't
   dramatically change your results.**

At this point, you should be in pretty good shape. Moving forward, you
should do the following:

* **When you update your package, try to write tests for the change
  you're making *before* making the change.** This will force you to
  think about the change you're making and the consequences that it will
  have, which can reveal logical errors. This will be difficult or
  impossible if you're very new to unit testing, and that's okay. It
  takes practice to be able to think of tests before writing the code
  you need to test.
* **When you update your package, you should run the package's tests as
  well as the distribution tests.** You can use a `continuous
  integration`_ tool like `Travis CI`_ to ensure that your package tests
  are run every time you open a Pull Request. It's good to get in the
  practice of running your tests yourself, but it's also good to have CI
  in place in case you forget. You'll need to be diligent about
  remembering to run your dristribution tests since there's no easy way
  to integrate them into your CI.
* **When you upgrade dependencies, you should run your package's tests
  as well as your distribution tests.** If either your package or your
  notebook breaks, you can either roll back the dependency to the
  previous version, or update your package and/or notebook (making sure
  to run all your tests after doing so).
* **Periodically, you should run the distribution tests to ensure that
  your model is still producing results that match your expectations.**

.. _nbconvert: https://nbconvert.readthedocs.io/en/latest/execute_api.html#executing-notebooks-using-the-python-api-interface
.. _continuous integration: https://www.thoughtworks.com/continuous-integration
.. _Travis CI: https://travis-ci.org
