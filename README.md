=====================================
Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13...19 inclusive -- then that value counts as 0, except 15 and 16 do not count as a teen. The input is passed as command line arguments and output is to be printed on screen
=====================================


STEPS to run code on local
==========================


RUNNING CODE
=============

.. code-block:: python

    >>> python app.py 1 2 3
    6

    >>> python app.py 1 13 2
    3

    >>> python app.py 2 1 14
    3

    >>> python app.py 1 2
    Exactly 3 numbers are required

    >>> python app.py 1 2 a
    All inputs must be numeric

RUN UNIT TEST
=============

.. code-block:: python

    >>> python -m unittest