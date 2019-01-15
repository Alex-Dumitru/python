'''
The Art of Hitting Things with Sticks


What is Fuzzing?

Providing bad (malformed) input of some sort to an application in order to break it in a meaningful way which will
allow you to get execution or bypass some sort of security.

How it works?

Find an application that takes input (pretty much all of them), and start sending data.
You start fairly simply; misspelled commands, bad arguments, etc. As you progress, you get into the bigger stuff;
sending gigs of data, or sending files with bits flipped to change the control paths

Types of fuzzing.

String Mutation - (the most common type) - taking a string or letter, and changing it to find a break condition
    "a" * 1000000000000 # this will break pretty much anything if it's insecure

Metadata/File Format Fuzzing - A bit (actually, a lot) more complicated, but useful when trying to break application
                             which take in files
Malformed Arguments - if you know what kind of arguments a file takes, you can malform them and do some pretty
                    interesting damage

'''


from hashlib import md5
import sys

def passcrack(pass_hash):
    '''
    We are looking into password cracking (brute force) here because it is kind of like fuzzing

    This function will hash the numbers in range [0-1000], then compare with a given hashed pwd.
    In this format, it will only find out pwds that integers are in the given range (but can be improved)
    :param pass_hash:
    :return:
    '''
    for i in range(1001):
        m = md5()                       # reset m
        m.update(str(i).encode('utf-8'))                # calculate the hash
        test_hash = m.hexdigest()
        if (test_hash != pass_hash):    #check the hash
            print('Failed: {}\t{}'.format(test_hash,pass_hash))
        else:
            print('Success: {}\t{}'.format(test_hash, pass_hash))
            print('Success: {}'.format(i))
            return

m = md5()
m.update(str(sys.argv[1]).encode('utf-8'))
passcrack(m.hexdigest())
# here we take input the actual pwd integer and hash it, then use our function to generate hashes for all numbers
# between 0 and 1000 and and compare with the input hash.