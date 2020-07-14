#Write a function called sumall that takes any number of arguments and returns their sum.
def sumall(*args):
    sum=0
    for n in args:
        sum+=n
    return sum
sumall(9,5,6,73)