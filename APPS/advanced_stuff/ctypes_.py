'''

C + Python = fun (and mayhem)

Ctypes are a means of using C code within a Python program.
They allow you to do things which may not have been included in Python, or which require special modules/libraries
They are tricksy beasts, and require a bit of setup


Calling conventions in C

C primarily uses two calling conventions on x86 platforms: cdecl and stdcall
In Windows C, stdcall is called WINAPI and cdecl is called WINAPIV

stdcall - used for functions which always take the same number of arguments
    def boo(a,b,c)

cdecl   - used for functions which take a variable number of arguments
    def bar(a,....)

DLL's

A DLL (Dymanically Linked Library) is used to gain access to functions from other code.
They're similar to Python modules, but require a bit more legwork.
You can use DLL's to access the various ctype functions.

Major DLL's

kernel32.dll - exports memory management, I/O, and process/thread functions
user32.dll   - makes GUI's possible. This is what is implemented to make the OS user friendly
msvcrt.dll   - allows programmers to use Linux-C style code without making major source code changes

Pointers in Ctypes

A pointer is a memory address. Python doesn't generally use these.
Pseudo-code ex:

int a = 0;     in C this is how you create an integer
int *b = &a;   this is how you create a pointer ('b') to the value 'a'

After creating the variables, you can access the value by using either the original, or by dereferencing the pointer

a = 1;
*b = 1;  the star accesses the value pointed to by 'b'

Why to use a pointer ?
The answer lies in the difference netween passing by reference or passing by value

C passes by reference   - you pass the address of the data, rather than copying it all over
                        - any changes you make to the addressed data will show for any functions which access that data
Python passes by value  - any time you pass a variable to a function, the called function copies the entire contents of
                        that variable
                        - you can do whatever you like to the data you receive, the original won't be altered

https://docs.python.org/3/library/ctypes.html
'''

from ctypes import *


# Assigning C data types

c_int(1)
string =c_char_p('test'.encode('utf-8'))
print(string)
c_char_p(2154388753856)
print(string.value)
b'test'
string.value='hello world!'.encode('utf-8')
print(string.value)
b'hello world!'

# Calling Ctype functions

type(cdll) # is a Library Loader

message = b"blah blah"
cdll.msvcrt.printf(b"%s", message) # not working :( .. should work in python 2.7. Didn't figure it out yet....

'''
!!! Works only in console prompt !!!

NOTE FROM DOC: Note that printf prints to the real standard output channel, not to sys.stdout, so these examples will 
only work at the console prompt, not from within IDLE or PythonWin:


Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from ctypes import *
>>> libc = cdll.msvcrt
>>> printf = libc.printf
>>> printf(b"hello, %s\n", b"world!")
hello, world!
14
>>>
'''
cdll.user32.MessageBoxA # to create a message box in windows
cdll.user32.MessageBoxA(0, b'click yes or no', b'title', 4)
windll.user32.MessageBoxA(0, b'click yes', b'title', 4)  # don't know the difference...not really important now

# you can use the return code, and based on this, do some action following the user response
