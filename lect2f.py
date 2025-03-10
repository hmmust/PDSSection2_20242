def get_nos(s,e):
    for i in range(s,e):
        yield i

get_nos2  = ( i for i in range(100,150) )

for n in get_nos2:
    print(n)
