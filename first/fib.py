import time


def fib_1(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib_1(n - 1) + fib_1(n - 2)


def fib_2(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        a = 1
        b = 1
        temp = 0
        for i in range(n - 2):
            a += b  # a = a + b
            temp = b
            b = a
            a = temp
        return b


if __name__ == '__main__':
    startTime = time.time() 
    for i in range(37): # if i < 20:
        print("result", i + 1," is ", fib_1(i + 1))
        # i = i + 1
    endTime = time.time()
    print("run time is :", endTime - startTime)
    print("***********************************************")
    startTime = time.time()
    for i in range(37):
        print("result", i + 1," is ", fib_2(i + 1))    
    endTime = time.time()
    print("run time is :", endTime - startTime)