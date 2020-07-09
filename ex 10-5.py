#Write a function called has_duplicates that takes a list and returns True if there is any
#element that appears more than once. It should not modify the original list.
def has_duplicate(lii):
    i=0
    for item in lii:
        li=lii[:i]+lii[i+1:]
        if item in li:
            return True
        i+=1
    return False
l=[1,"*","*",5,8,0]
print(has_duplicate(l))
print(l)