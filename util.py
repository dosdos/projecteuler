import random


print('-'*30)
#===============================================================================
# ARGS & KWARGS
#===============================================================================
def print_args(p, *args):
    print('param: ', p, '\nargs: ',)
    for a in args: print(a,)

print_args("ciao", ('A','B','C'), 3, 2.5, 'hello')

def print_kwargs(f, g, **kwargs):
    # Check for a key
    m = kwargs['m'] if 'm' in kwargs else None
    if m: print("Value '%s' founded for key '%s'! :)" % (str(m), str(kwargs['m'])))
    # Print all keys
    for k in kwargs.keys(): print(kwargs[k])

print_kwargs("ciao", "mondo", m="amico", n="mio", t="Tony")
args = {'m':"amico", 'n':"mio", 't':"Tony"}
print_kwargs("ciao", "mondo", **args)


print('-'*30)
#===============================================================================
# FOR + DICT + ENUMERATE
#===============================================================================
choices = ['pizza', 'pasta', 'salad', 'nachos']
print('Your choices are:')
for index, item in enumerate(choices):
    print(index, item)

for e in enumerate(choices):
    print(e)


print('-'*30)
#===============================================================================
# ELSE IN FOR AND WHILE CYCLES
#===============================================================================
def else_in_cycles():

    fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']
    print('You have...')
    for f in fruits:
        if f == 'tomato':
            print('A tomato is not a fruit!') # (It actually is.)
            break
        print('A', f)
    else:
        print('A fine selection of fruits!')

    print("Lucky Numbers! 3 numbers will be generated.", "If one of them is a '5', you lose!")
    count = 0
    while count < 3:
        num = random.randint(1, 6)
        print(num)
        count += 1
        if num == 5:
            print("Sorry, you lose!")
            break
    else:
        print ("You win!")

else_in_cycles()

