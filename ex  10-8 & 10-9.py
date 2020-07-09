#Exercise 10.8 To check whether a word is in the word list, you could use the in operator, but it
#would be slow because it searches through the words in order.
#Because the words are in alphabetical order, we can speed things up with a bisection search, which
#is similar to what you do when you look a word up in the dictionary. You start in the middle and
#check to see whether the word you are looking for comes before the word in the middle of the list.
#If so, then you search the first half of the list the same way. Otherwise you search the second half.
#Either way, you cut the remaining search space in half. If the word list has 113,809 words, it will
#take about 17 steps to find the word or conclude that it’s not there.
#Write a function called bisect that takes a sorted list and a target value and returns the index of the
#value in the list, if it’s there, or None if it’s not.
fin = open("words.txt")
li=[]
for line in fin:
    s=line.strip()
    li.append(s)#that is much faster than t=t+[x] & by the way t+=[x] is fast too
def search_bisect(s,l):
    i=0
    if len(l)==1:
        if s==l[i]:
            return True
        else:
            return False
    else:
        ind=len(l)//2
        if s > l[ind]:
            return search_bisect(s,l[ind:])
        elif s < l[ind]:
            return search_bisect(s,l[:ind])
        else:
            return True 
print(search_bisect("proposers",li))
#Exercise 10.9 Two words are a “reverse pair” if each is the reverse of the other. Write a program
#that finds all the reverse pairs in the word list.
def reverse_pairs():
    for word in li:
        s=[]
        i=len(word)-1
        while i>=0:
            s+=word[i]
            i-=1
        delimiter=""
        if search_bisect(delimiter.join(s),li):
            print (delimiter.join(s),word)
reverse_pairs()
