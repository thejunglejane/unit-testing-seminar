# Unit Testing for Reproducible Science

## Overview

This seminar teaches the basics of unit testing and how to use unit testing for
reproducible research.

### Seminar Topic

A unit test is a separate piece of code that exercises your code to determine if
it's functioning as expected. With unit tests in place, it's possible to isolate
changes in your results to changes to your input data or changes to your model.
Without unit tests in place, it's hard to determine if changes in your results
are a side effect of the code not doing what you expect it to do rather than a
"legitimate" result.

Beyond it's role in reproducible research, unit testing helps you write better
code by forcing you to think through edge cases, factor your code into
easily-testable units, and ensure that code changes don't break existing
functionality.

In this seminar, you will learn what unit testing is, why it's important, and
how to write (and run!) unit tests for your code.

### Audience

The seminar is intended for researchers and scientists, and it assumes that most
of your code is developed in Jupyter notebooks. If that's not you, feel free to
skip the lesson on testing Jupyter notebooks.

## What's Inside

The seminar is divided into four units, each of which contains several lessons.
Each lesson contains the following:

1. Written lecture
1. Jupyter notebook containing examples
1. Practice exercises

## How to use this repository

First, create a fork of this repository on GitHub
[here](https://github.com/thejunglejane/unit-testing-seminar/fork) and then
clone your fork locally with:

```bash
git clone git@github.com:{username}/unit-testing-seminar.git
```

To run the Jupyter notebooks and examples included in this seminar, you need
`python3.7` and `jupyter`. Create a [virtual
environment](https://docs.python.org/3/tutorial/venv.html) and install the
required dependencies into it.

If you have [`pipenv`](https://pipenv.readthedocs.io/en/latest/) installed, you
can run:

```bash
cd unit-testing-seminar
pipenv install
pipenv shell
```

If you don't have `pipenv`, you can install the dependencies into any other
virtualenv by running:

```bash
cd unit-testing-seminar
pip install -r requirements.txt
```

Either of these will install all of the dependencies for you. Now, you can
launch Jupyter and run all the notebooks.
