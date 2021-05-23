def averager():
    total = 0
    count = 0
    def inner(n):
        nonlocal total, count
        total += n
        count += 1
        print(total / count)
    return inner

f = averager()

f(10) # avg 10
f(20) # avg 15
f(30) # avg 20