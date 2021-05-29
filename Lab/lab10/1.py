def con(f,g):
    def hel(x):
        return f(g(x))
    return hel