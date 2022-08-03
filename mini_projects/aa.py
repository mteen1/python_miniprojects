def do_twice(f,a):
    f(a)
    f(a)

	
def print_spam(a):
    print(a)
do_twice(print_spam, 5)
def print_twice(a):
    print(a)
    print(a)

do_twice(print_twice, "spam")
def do_four(f, a):
    do_twice(f, a)
    do_twice(f, a)

do_four(print_spam, "matin")
