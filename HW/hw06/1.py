class Link:
    empty = ()
    def __init__(self,first,rest = empty):
        assert rest is Link.empty or isinstance(rest,Link)
        self.first = first
        self.rest = rest
    
    def __str__(self):
        s = '<'
        while self.rest is not Link.empty:
            s = s + self.first.__str__() + ','
            self = self.rest
        return s + str(self.first) + '>'


def list_concat(a,b):
    if b is Link.empty or a is Link.empty:
        return a or b
    if a.rest is Link.empty :
        return Link(a.first,b)
    else:
        return Link(a.first,list_concat(a.rest,b))

def dupilcate(lst):
    if lst is Link.empty:
        return lst
    elif lst.rest is Link.empty:
        return Link(lst.first,lst)
    
    
def insert (element,lst,index):
    if index == 0:
        new = Link(element)
        new.rest = lst
        lst = new
    else:
        insert(element,lst.rest,index - 1)
        
        