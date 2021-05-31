from operator import mul

def acc(combiner,start,n,term):
    if n == 1:
        return combiner(start,term(1))
    return combiner(acc(combiner,start,n-1,term),term(n))

def acc_tail(combiner,start,n,term):
    def help_tail(sum0,x):
        if x == n:
            return sum0
        return help_tail(combiner(sum0,term(x+1)),x+1)
    return help_tail(combiner(start,term(1)),1)


#Disc 12 If-Macro
def if_macro(condition, true_result, false_result):
    """
    >>> eval(if_macro("True", "3", "4"))
    3
    >>> eval(if_macro("0", "'if true'", "'if false'"))
    'if false'
    >>> eval(if_macro("1", "print('true')", "print('false')"))
    true
    >>> eval(if_macro("print('condition')", "print('true_result')", "print('false_result')"))
    condition
    false_result
    """
    "*** YOUR CODE HERE ***"
    return f"{true_result} if {condition} else {false_result}"
    