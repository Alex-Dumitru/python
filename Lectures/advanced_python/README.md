# Comprehension

Comprehension is a feature, that allows you to build a sequence from another sequence.

There are 3 types:
## List Comprehension:
List comprehensions provide a short and concise way to create lists. Common applications are to make new lists where each element is the result of some operations applied to each member of another sequence or iterable, or to create a subsequence of those elements that satisfy a certain condition. It consists of square brackets containing an expression followed by a `for` clause, then zero or more `for` or `if` clauses. The expressions can be anything, meaning you can put in all kinds of objects in lists. The result would be a new list made after the evaluation of the expression in context of the `if` and `for` clauses.

Syntax:

```python
variable = [expression for element in iterable]
variable = [expression for element in iterable if condition]
```

Use case - generating a list of squared numbers from a range or an existing list:


```python
squares = []
for elem in range(10):
    squares.append(elem**2)
print(squares)
```
Output:
```python
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```
- one side effect is that variable **x** is created, overwritten, and kept into memory

Another way, without any side effects would be:
```python
squares = list(map(lambda elem: elem **2, range(10)))
```

>NOTE: We will look at lambda and map later in the course!

And finally:
```python
squares = [elem**2 for elem in range(10)]
```
Which is more concise and readable.

Another example: 
- combining elements of 2 distinct lists, if they are not equal
```python
[(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]
```
Output:
```python
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```
- this replaces a nested `for` loop

[Documentaion](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)

## Dictionary Comprehension
They work in similar way, but the input and output is a dictionary.

Syntax:

```python
variable = {expression for element in iterable}
variable = {expression for element in iterable if condition}
variable = {key:value for (key,value) in dict.items()}
```

Example:
- creating a dictionary with frequency of letters used, regardless of their case
```python
case_dict = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
case_freq = {k.lower(): case_dict.get(k.lower(), 0) + case_dict.get(k.upper(), 0) for k in case_dict.keys()}
print(case_freq)
```
Output:
```python
{'a': 17, 'b': 34, 'z': 3}
```

## Set Comprehension
Similar to the other 2 cases, but we generate a **set**. We also use curly braces to define a set, but the difference is in the elements we generate.

Syntax:
```python
variable = {expression for element in iterable}
variable = {expression for element in iterable if condition}
```

Example:
- going back to our *squares* 
```python
squares = {x**2 for x in [1,1,2,4,6,9,6]}
print(squares)
```
Output:
```python
{1, 4, 36, 16, 81}
```

For more on **sets**, please see official [Documentation](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset).


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


# Generators

Generators are a simple and powerful tool for creating *iterators*. They are written like regular functions but use the `yield` statement whenever they want to return data. Each time `next()` is called on it, the generator resumes where it left off (it remembers all the data values and which statement was last executed). 

Compared to Iterators, Generators are more compact, because methods `__iter__()` and `__next__()` are created automatically. Also the local variables like `self.index` and `self.data` and execution state are automatically saved between calls and `StopIteration` is automatically raised.

Example:

```python
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse("gnirts ym"):
    print(char)
```
Output:
```python
m
y

s
t
r
i
n
g
```

Advantages:
- perfect for reading a large number of large files, since they yield out data a single chunk at a time, irrespective of the size of the input stream.
- they are syntactic sugar for writing objects that support the iterator protocol
- they abstract much of the boilerplate code needed when writing class-based iterators

Disadvantages:
- can [run slower](https://stackoverflow.com/questions/11964130/list-comprehension-vs-generator-expressions-weird-timeit-results/11964478#11964478) than list comprehension (unless you run out of memory, of course)
- have a specific number of iterations (which cannot be reset) !!!!!



## Generator Expression

A simple generator can also be coded as an expression using syntax similar to list comprehensions, adding yet another layer of syntactic sugar.
The difference is that we use parentheses instead of square brackets. This method is more compact, but less versatile than full generator definitions, and, compared to list comprehensions, they tend to be more memory efficient, because they don't store the entire array in memory.

There are 2 small caveats though:
- raising `StopIteration` exceptions after control flow leaves the generator function by any means other than a yield statement, means it cannot be reused (rethink your implementation with generator functions or class-based iterators)
- cannot be defined with input parameters

Example:
```python
// list comprehension
multiples_lc = [num * num for num in range(10)]

// generator
multiples_gen = (num * num for num in range(10))

print("list comprehension: ", multiples_lc)
print("generator: ", multiples_gen)

// iterate over them

for num in multiples_lc:
    print(num)

for num in multiples_gen:
    print(num)
```

Output:
```python
list comprehension:  [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
generator:  <generator object <genexpr> at 0x000001F2EA1CC048>

0   
1   
4   
9   
16  
25  
36  
49  
64  
81  

0
1
4
9
16
25
36
49
64
81
```
You can also access the values produced by a generator with the `next()` function
```python
multiples_gen = (num * num for num in range(10))
next(multiples_gen)
next(multiples_gen)
next(multiples_gen)

// this goes on until you get StopIteration
next(multiples_gen)
next(multiples_gen)
next(multiples_gen)
next(multiples_gen)
next(multiples_gen)
next(multiples_gen)
next(multiples_gen)
next(multiples_gen)
```

Output:
```python
0
1
4
9
16
25
36
49
64
81
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```


# Coroutines ?
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
Examples:
```python
# You could have:
def add(x, y):
    return x + y
add(5, 3)                   # Output: 8

# Which is equivalent of:

add = lambda x, y: x + y
add(5, 3)                   # Output: 8

# OR even:

(lambda x, y: x + y)(5, 3)  # Output: 8
```

> NOTE: Functions created with lambda expressions cannot contain statements or annotations (not even a `return` statement).

Executing a lambda function evaluates its expression and then automatically returns its result. So there's always an *implicit* `return` statement.

Use cases:

Technically, any time you’re expected to supply a function object you can use a lambda expression. And because a lambda expression can be anonymous, you don’t even need to assign it to a name.

- writing short and concise *key funcs* for sorting iterables by an alternate key

```python
sorted(range(-5,6), key=lambda x: x ** 2)
```
Output:
```python
[0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5]
```

- provide on-the-fly functions, where a function object is expected (see [Map](#map), [Filter](#filter))

# Overview of useful functions
## Map
## Filter
## Reduce
## Zip
## Enumerate
# Parsing *args and **kwarg
# Ternary Operators (conditional expressions)

Ternary operators are more commonly known as conditional expressions in Python. These operators evaluate something based on a condition being true or not.

Syntax:
```python
condition_if_true if condition else condition_if_false
```

Example:
```python
is_nice = True
state = "nice" if is_nice else "not nice"

# as opposed to

if is_nice:
    state = "nice"
else:
    state = "not nice"
```

This feature allows us to quickly test a condition of a multiline `if` statement. Often times it can be immensely helpful and can make your code compact but still maintainable. 

Another example involves tuples:

```python
(if_test_is_false, if_test_is_true)[test]
```

Example:
```python
nice = True
personality = ("mean", "nice")[nice]
print("The cat is", personality)
```
Output:
```python
"The can is nice"
```
>NOTE: the trick behind this is that **True == 1** and **False == 0**, so in fact, we are leveraging this to state which index from the tuple we want to use. This is also somewhat regarded as not pythonic, because it can create confusion if you don't remember where to put the *true* and *false* values.



# Decorators

In the most simplest words, a decorator is a function which modifies the functionality of other functions. 

## How to write a decorator

First of all let’s review the functions in Python:

```python
# we define a function that says "Hi" to a name. If we don't specify the "name", the name will default to "Alex"

def hello(name="Alex"):
    return "Hi " + name

print(hi())
# output: 'Hi Alex'

# We can even assign a function to a variable like
greet = hello
# We are not using parentheses here because we are not calling the function hello
# instead we are just putting it into the greet variable. Let's try to run this

print(greet())
# output: 'hello Alex'

# Let's see what happens if we delete the old "hello" function!
del hello
print(hello())
#outputs: NameError

print(greet())
#outputs: 'hello Alex'
```

Let's take it one step further, and define other functions inside our function

```python
def hello(name="Alex"):
    print("now you are inside the hello() function")

    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    print(greet())
    print(welcome())
    print("now you are back in the hello() function")

hello()
#output:now you are inside the hello() function
#       now you are in the greet() function
#       now you are in the welcome() function
#       now you are back in the hello() function

# This shows that whenever you call hello(), greet() and welcome()
# are also called. However the greet() and welcome() functions
# are not available outside the hello() function e.g:

greet()
#outputs: NameError: name 'greet' is not defined
```




---

possible material [here](http://book.pythontips.com/en/latest/index.html)




