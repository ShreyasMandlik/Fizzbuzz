def fizzBuzz(n):
    list1=[]
    for i in range(1,n+1):
        if i%3 == 0 and i>=3:
            list1.append("Fizz")
        elif i%5 == 0 and i>=5:
            list1.append("Buzz")
        else:
            list1.append(i)
    return list1
