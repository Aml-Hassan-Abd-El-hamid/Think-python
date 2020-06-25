#Exercise 8.9: A string slice can take a third index that specifies the “step size;” that is, the number of spaces between successive characters. A step size of 2 means every other character; 3 means every third, etc.
#>>> fruit = 'banana'
#>>> fruit[0:5:2]
#'bnn'
#A step size of -1 goes through the word backwards, so the slice [::-1] generates a reversed string.
#Use this idiom to write a one-line version of is_palindrome from Exercise 6.6.

def step_size(str,s,e,st):
    b=str[int(s):int(e)]
    ind=0
    i=0
    k=""
    j=len(b)-1
    if st==0:
        while i<=j:
            k+=b[i]
            i+=1
    elif st==-1:
        while j>=0:
            k+=b[j]
            j-=1
    else:
        while i<len(b)//st:
            k+=b[ind]
            ind+=st
            i+=1
    return k
print(step_size("hjasdfghjklgcfcuiop",0,8,-1))

def is_palindrome(str1,str2):
    if str1 == step_size(str2,0,len(str2),-1):return True
    return False

print(is_palindrome("stop","pots"))