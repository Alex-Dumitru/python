LIST_SIZE = 20

def verify_number(number):
    if number in range(LIST_SIZE):
        print('OK!')
    else:
        raise SystemExit('The number {n} is not in the list!'.format(n=number))


verify_number(20)