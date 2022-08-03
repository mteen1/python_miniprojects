"""this function returns the total value of numbers from 0 to n + the s parameter
but for negative numbers of n raises a RecursionError"""


def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n - 1, n + s)


recurse(-1, 0)
