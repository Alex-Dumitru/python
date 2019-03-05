# Iterators

Python supports the concept of iteration over containers. This is implemented using two distinct methods (`__iter__()` and `__next__()`); these are used to allow user-defined classes to support iteration. However, an iterator performs traversal and gives access to data elements in a container, but does not perform iteration. 

There are three parts, namely:

- Iterable
- Iterator
- Iteration

## Iterable

An **iterable** is any object in Python which has an `__iter__()` (tried 1st) or a `__getitem__()` (fallback) method defined which returns an iterator or can take indexes. In short an iterable is any object which can provide us with an iterator. 

## Iterator

An iterator is any object in Python which has a `next()` (Python2) or `__next__()` method defined. That’s it. That’s an iterator. 

## Iteration

In simple words it is the process of taking an item from something (e.g a list) and return it. When we use a loop to go over something, it is called iteration. It is the name given to the process itself. 

Documentation:

Module [itertools](https://docs.python.org/3/library/itertools.html) implements a number of iterator building blocks, standardizing a core set of fast, memory efficient tools that are useful by themselves or in combination.

Iterators [PEP234](https://www.python.org/dev/peps/pep-0234/)

Iterator types [official documentation](https://docs.python.org/3/library/stdtypes.html#iterator-types)

# Lambdas

Lambda expressions (sometimes called lambda forms) are used to create anonymous functions. You might want to use lambdas when you don’t want to use a function twice in a program, but keep in mind they have some restrictions.

Syntax:

```python
lambda parameters: expression
```

- this yields a function object.
- the unnamed object behaves like a function object defined with:

```python
def <lambda>(parameters):
    return expression
```

Note that functions created with lambda expressions cannot contain statements or annotations.

continue from https://dbader.org/blog/python-lambda-functions