'''
remember PEBCAK (problem exists between chair and keyboard)  - most of the times, when something is not working, it is
users fault :)


Processes and Threads

Processes:
- are full programs
- they have their own PID and their own PEB (process environment block)
- they can contain multiple threads (but not infinite)
- if one terminates, the associated threads do so as well

Threads:
- are separate execution paths within a process
- they don't have PID's, but they do each have a TEB (thread environment block)
- they can only be associated with one Process
- processes can continue after threads terminate (so long as there is at least one thread left)


|------------------------------------------------|
|  |--------|                 PROCESS            |
|  | PEB    |                                    |
|  |        |                                    |
|  |--------|                                    |
|                                                |
|  |-----------|  |-----------|  |-----------|   |
|  |  THREAD   |  |  THREAD   |  |  THREAD   |   |
|  |           |  |           |  |           |   |
|  | |-----|   |  | |-----|   |  | |-----|   |   |
|  | | TEB |   |  | | TEB |   |  | | TEB |   |   |
|  | |-----|   |  | |-----|   |  | |-----|   |   |
|  |           |  |           |  |           |   |
|  |-----------|  |-----------|  |-----------|   |
|------------------------------------------------|


Advantages:

Speed - more threads working on the same problem = increased speed (not applicable if step by step approach is needed)
Granularity - especially in network applications, having a thread for each client allows for more fine control over the
              connections
Robustness - if one thread crashes, you can continue the program and avoid a potential catastrophic termination

Desadvantages:

Debugging - it's harder to track down errors over multiple threads
Resource fights - if multiple threads are trying to access the same data, explosions will happen


Python's little problem

Multi-threading is problematic in Python because of a fundamental part of the standard Python interpreter; the Global
Interpreter Lock.
The GIL only allows a single Python instruction to be executed at a time, meaning parallelization is essentially
neutralized in Python Multi-threading. The speedup normally gained is nowhere to be found, because no matter how many
threads you have, they're bottlenecked by the GIL

This bottlenecking doesn't remove the benefit of multithreading for the sake of multiple network connections, or for
the sake of program robustness. Only the speed is affected.

The damage to the multi-threading speedup can also be neutralized by utilizing an interpreter which doesn't have the GIL
Jpython is typically a favorite, though Stackless (used to write EVE Online) uses a remarkable implementation which
gains all the benefits (or at least most) without many of the drawbacks of multi-threading.


The solution to sharing resources without creating race conditions to access data is by use of things like semaphores
and mutexes

semaphores  - used to guard limited resources. If you only have 5 slots available for a taks, a semaphore can be used to
            ensure that only 5 slots are allowed in use
            - this is accomplished by means of an internal counter. Every time someone acquires the semaphore, this
            counter decreases. Every time someone releases the semaphore, this counter increases.
mutexes - (mutually exclusive lock) is a means of controlling access to a resource. If one thread is using a file
        handle, a mutex prevents another thread from accessing the file handle


'''

import threading


'''
threading.Thread()  - instantiate a thread
threading.start()   - begin execution
threading.isAlive() - see if thread is extant 
'''

from time import sleep

def funct1(arg1, arg11):
    pass
def funct2(arg2):
    pass
def funct3(arg3, arg33, str_arg):
    pass
def multiple_threads():
    function_list = [funct1, funct2, funct3]
    args_list = [(arg1, arg11), (arg2,), (arg3, arg33, "arg333")]    # arguments are passed as tuples
    threads_list = []

    for i in range(len(function_list)):
        threads_list.append(threading.Thread(None, function_list[i], args_list[i]))

    for i in threads_list:
        i.start()
        sleep(1)