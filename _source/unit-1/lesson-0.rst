Lesson 0
========

In this lesson, we'll dig deeper into how to write unit tests.

Unit Testing Libraries
----------------------

As we mentioned in Unit 0, there are several different unit testing
libraries and frameworks for Python. To name a few:
* :mod:`unittest`
* `pytest`_
* `marbles`_
* `nose`_
* :mod:`doctest`

:mod:`unittest` is Python's built-in unit testing library.
:mod:`unittest` organizes tests into :mod:`~unittest.TestCase` classes
where tests are methods beginning with ``test_``. This can be
alienating, especially to users who aren't very familiar with Python
classes, but it's easy to get the hang of.

`pytest`_ is one of if not the most popular Python testing library. One
of the things that `pytest`_ users like is that there's less
boilerplate than :mod:`unittest` because you don't have to write
classes.

In the interest of full transparency, I am the co -creator and
-maintainer of `marbles`_. `marbles`_ extends the :mod:`unittest`
framework to provide more information-rich failure messages, and writing
`marbles`_ tests is basically the same as writing :mod:`unittest` tests.

`nose`_ is no longer being maintained and you shouldn't use it. I
included it in this list because you might come across it at some point,
and it's useful to know about it. My first unit tests were written in
nose primarily becase tests are very easy to write in nose.

:mod:`doctest` isn't really a unit testing library, but it's worth
knowing about. :mod:`doctest` looks for pieces of text that look like
interactive Python sessions in your docstrings, and then executes them
to make sure that they work the way they're shown in the docstring.
:mod:`doctest` is very useful for ensuring that code examples in
docstrings work as documented.

Again, it doesn't matter which library you use to write your tests
(except really don't use nose) as long as you're writing tests!

Testing Jupyter Notebooks
-------------------------

To be perfectly honest, if you want to test your code, you should get
it out of a Jupyter notebook and into a package that you then import
into your Jupyter notebooks when you need it. The reason for this is
that we want our tests to be isolated from one another and we want them
to be reproducible, and this is difficult in Jupyter notebooks where
it's easy to get your notebook into a weird state by running cells out
of order, deleting cells without deleting the objects defining those
cells, etc.

But, refactoring notebooks into packages takes time, and we can make
some progress toward testing our notebooks, even if it's not perfect.

Executing Your Notebooks
~~~~~~~~~~~~~~~~~~~~~~~~

One simple way to test that your notebooks are working is to execute
all the cells and ensure that none of them raise an execption. This
obviously doesn't guarantee that your notebook is doing what you think
it's doing, but it does guarantee that you can still run your notebook.

You can see an example of this `here`_.

Adding Tests to Your Notebooks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can also add unit tests directly in cells inside your notebook. For
example, if you define some functions at the top of your notebook, you
can add a cell afterward that defines tests for those functions. You
can then execute your tests in the following cell with:

.. code-block:: python

   unittest.main(argv=['first-arg-is-ignored'], exit=False)

.. note::
   This is a bit different from how we executed our tests from the
   command line. Recall that we added the following to the bottom of
   our test file:

   .. code-block:: python

      if __name__ == '__main__':
         unittest.main()

   Calling :func:`unittest.main` like this won't work in Jupyter for two
   reasons:

   #. :func:`unittest.main` looks at ``sys.argv`` by default, and the
      first argument will be whatever started Jupyter instead of what
      :mod:`unittest` was expecting`. We can make :func:`unittest.main`
      ignore ``sys.argv`` by passing a list to ``argv`` ourselves.
   #. :mod:`unittest` will try to shut down the process after it runs
      your tests, which you don't want it to do because we want our
      kernel to keep running after we've run our tests.

You have to be diligent about cleaning up after yourself in between each
test run. In Jupyter, the results of all evaluations are stored in
global variables unless they're explicitly deleted. This means that even
if you delete or rename a test, the old test will still be found unless
you explicitly delete it with the ``del`` command.

If possible, you can restart your notebook in between test runs. If this
won't work for you, I recommend looking at how `ipytest`_ cleans up in
between tests `here <clean_tests>`__. We'll cover `ipytest`_ below.

nbval
~~~~~

`nbval`_ is a `pytest`_ plugin that validates Jupyter notebooks by
executing every cell that contains code and compares the output with
the outputs the most recently stored outputs. Basically, it uses the
saved notebook as the test criteria.

This can be a good way of ensuring that your notebook is doing what it
was doing last week, but it won't work well if your notebook's outputs
are stochastic.

ipytest
~~~~~~~

Finally, there's `ipytest`_. `ipytest`_ allows you to run `pytest`_ unit
tests inside Jupyter notebooks.

`ipytest`_ provides a way of cleaning up tests that may be lingering
around in your global state. See `clean tests`_ for more information on
how this works and how you should use it.

.. note::
   `ipytest`_ used to support :mod:`unittest` tests but has deprecated
   support for :mod:`unittest`.

Testing Packages
----------------

Let's say we have a Python package ``my_package`` with two modules,
``foo`` and ``bar``. This package might have a structure like this:

.. code::

   ├── my_package
   │   ├── __init__.py
   │   ├── foo.py
   │   └── bar.py
   ├── README.md
   ├── requirements.txt
   └── setup.py

We want to test the code in foo.py and bar.py.

Structuring Your Project
~~~~~~~~~~~~~~~~~~~~~~~~

The first question is: where should our tests go? There are a couple of
places they could go:

#. Inside foo.py and bar.py
#. In separate files next to foo.py and bar.py
#. In a separate test directory

Tests in Source Code
""""""""""""""""""""

In general it's not a good idea to put tests in the same file as the
code that they're testing. The reason we don't want to do this is that
we'd then have to find a way of communicating to whoever is using our
module which things are tests and which things are actually provided by
the module for them to use.

Tests Next to Source Code
"""""""""""""""""""""""""

Okay so we don't want to put our tests right inside our modules. What
about next to them like this? This gets them out of the modules, but
we still have the problem of communicating to the user which modules
they should import and use and which modules they shouldn't import.

.. code::

   ├── my_package
   │   ├── __init__.py
   │   ├── foo.py
   │   ├── test_foo.py
   │   ├── foo.py
   │   └── test_bar.py
   ├── README.md
   ├── requirements.txt
   └── setup.py

Tests in a Test Directory
"""""""""""""""""""""""""

Finally, you can create a separate test directory whose directory
structure mirrors the structure of your package:

.. code::

   ├── my_package
   │   ├── __init__.py
   │   ├── foo.py
   │   └── bar.py
   ├── tests
   │   ├── __init__.py
   │   ├── test_foo.py
   │   └── test_bar.py
   ├── README.md
   ├── requirements.txt
   └── setup.py

One disadvantage of putting tests in a separate directory is that you
miss out on the visual signal that 

Running Tests
~~~~~~~~~~~~~

Test Discovery
""""""""""""""

:mod:`unittest` can find and run all of your tests as long as all of
your test files are modules or packages that can be imported from the
top-level of your package and they all start with ``test_``.

.. code:: bash

   $ cd my_package
   $ python -m unittest discover

If you want to run some specific tests you can do that too:

.. code:: bash

   $ # run all the tests in test_foo
   $ python -m unittest tests.test_foo
   $ # run all the tests defined in FooTestCase
   $ python -m unittest tests.test_foo.FooTestCase
   $ # run only test_foo_does_this
   $ python -m unittest tests.test_foo.FooTestCase.test_foo_does_this

You can read more about test discovery
`here <https://docs.python.org/3/library/unittest.html#test-discovery>`__.

Interpreter
"""""""""""

You can also run your tests directly with ``python -m
tests/test_foo.py`` as long as you have the following at the bottom of
your test file:

.. code:: python

   if __name__ == '__main__':
      unittest.main()

Setup and Teardown
~~~~~~~~~~~~~~~~~~

At a certain point you'll probably have quite a few tests on your hands,
and setting them up can get repetetive. If you find yourself in this
situation, you can factor out your test setup code into the
:meth:`unittest.TestCase.setUp` method. :mod:`unittest` will
automatically call this method before it runs every test.

There's a counterpart method that runs after every test (unless an
exception is raised): :meth:`unittest.TestCase.tearDown`. The
environment created in between :meth:`~unittest.TestCase.setUp` and
:meth:`~unittest.TestCase.tearDown` is known as a *test fixture*.

Organizing Your Test Code
~~~~~~~~~~~~~~~~~~~~~~~~~

In :mod:`unittest`, tests are grouped together into test cases. A good
rule of thumb is to group tests according to the features that they
test. For smaller projects, it's likely that you'll have only one test
file with one case per module, and that's fine. For bigger projects,
you'll probably find it easier to split your tests into separate test
cases, perhaps even separate test files.

At the end of the day, you should organize your test code in whatever
way is easiest for you to understand and is most efficient for you to
write.

.. _pytest: https://docs.pytest.org
.. _marbles: https://marbles.readthedocs.io/en/latest/
.. _nose: https://nose.readthedocs.io/en/latest/
.. _here: https://blog.thedataincubator.com/2016/06/testing-jupyter-notebooks/
.. _nbval: https://nbval.readthedocs.io/en/latest/
.. _ipytest: https://github.com/chmp/ipytest
.. _clean tests: https://github.com/chmp/ipytest#ipytestclean_tests
.. _clean_tests: https://github.com/chmp/ipytest/blob/master/ipytest/_util.py
