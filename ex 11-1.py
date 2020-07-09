#Write a function that reads the words in words.txt and stores them as keys in a
#dictionary. It doesn’t matter what the values are. Then you can use the in operator as a fast way to
#check whether a string is in the dictionary.
fin=open("words.txt")
d=dict()
for line in fin:
    s=line.strip()
    d[s]=1
#print(d)
def search_dict(s,dd):
    if s in dd:
        return True
    else:
        return False
#use the function reverse_pairs() here show the big diffrence between searching in dict and by bisect
def reverse_pairs():
    for word in d:
        s=[]
        i=len(word)-1
        while i>=0:
            s+=word[i]
            i-=1
        delimiter=""
        if search_dict(delimiter.join(s),d):
            print (delimiter.join(s),word)
reverse_pairs()