#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 1, part 1."""

def listdivide(numbers, divide=2):
    """
    Args:
        numbers (list): List of Numbers to divide on.
        divide (int): Interger used to divide numbers list.
        divisible (list): List of divisible numbers.
    Returns:
        divisible (list): A list of divisible numbers.
    Examples:
        >>> test = testListDivide([1,2,3,4,5])
        >>> print test
        >>> [2, 4]
    """
    divisible = []
    for values in numbers:
        if values % divide == False:
            divisible.append(values)
    return divisible

class ListDivideException(Exception):
    """
    Attributes:
        None
    """
    pass

def testlistdivide():
    """
    Args:
        None
    Returns:
        None
    Examples:
        >>> testListDivide()
        >>>
    """
    try:
        listdivide([1, 2, 3, 4, 5])
        listdivide([2, 4, 6, 8, 10])
        listdivide([30, 54, 63, 98, 100], divide=10)
        listdivide([0])
        listdivide([1, 2, 3, 4, 5], 1)
    except:
        raise ListDivideException()

    if __name__ == '__main__':
        testlistdivide()
