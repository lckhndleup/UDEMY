def fibonacci():
    a=1
    b=1
    yield a
    yield b

    while True:
        a,b=b,b+a

        yield b

for i in fibonacci():
    if i<100000:
        print(i)
    else:
        break
