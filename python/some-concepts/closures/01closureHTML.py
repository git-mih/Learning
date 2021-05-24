def outer(tag):
    def inner(msg):
        print(f"{tag} {msg} {tag[0]}/{tag[1:]}")
    print("outer CELL: ", id(outer.__code__.co_freevars))
    print(outer.__code__.co_freevars)
    return inner

h1 = outer("<h1>") # inner still have access to tag variable
h1("hello world")

print("h1 CELL: ", id(h1.__code__.co_cellvars))
print(h1.__code__.co_freevars)