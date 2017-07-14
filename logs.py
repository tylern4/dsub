from __future__ import print_function
from pprint import pprint
## Optional to have color printing
try:
    from termcolor import cprint
    print_green = lambda x: cprint(x, 'green', attrs=['bold'])
    print_red = lambda x: cprint(x, 'red', attrs=['bold'])
    print_blue = lambda x: cprint(x, 'blue', attrs=['bold'])
    print_white = lambda x: cprint(x, 'white', attrs=['bold'])
    print_yellow = lambda x: cprint(x, 'yellow', attrs=['bold'])
except ImportError, e:
    print_green = lambda x:     print(x)
    print_red = lambda x:       print(x)
    print_blue = lambda x:      print(x)
    print_white = lambda x:     print(x)
    print_yellow = lambda x:    print(x)

## Optional for
try:
    import tqdm
    has_prog = True
except ImportError, e:
    has_prog = False
