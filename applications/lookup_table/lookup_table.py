# Your code here: ----------------------------v
import math
import random

lookup_table = {}
#---------------------------------------------^
def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

# ---------------------------------------------v
for i in range(2, 14):
    for k in range(3, 6):
        lookup_table[(i, k)] = slowfun_too_slow(i, k)
# ---------------------------------------------^

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here -------------------------------------------------------------v
    return lookup_table[(x, y)]
    # ----------------------------------------------------------------------------^

# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')

####################lookup table#######################

# import math

# lookup_table = {}

# def inverse_root(n):
#     return 1 / math/sqrt(n)

# def build_lookup_table():

#     for i in range(1, 10):
#         lookup_table[i] = inverse_root(n)

# build_lookup_table()