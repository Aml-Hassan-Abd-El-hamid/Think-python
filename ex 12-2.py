#Exercise 12.2 In this example, ties are broken by comparing words, so words with the same length
#appear in alphabetical order. For other applications you might want to break ties at random. Modify
#this example so that words with the same length appear in random order. Hint: see the random
#function in the random module.
import random
def sort_by_length(words):
    t=[]
    for word in words:
        t.append((len(word),random.random(),word))#decorate
    t.sort(reverse=True)#that arg tells sort to go in decreasing order
    res=[]
    for length,ran, word in t:
        res.append(word)#undecorate
    return res
w=["fgdd","ghfd","ee","hdtrr","jhg","ufd","q","as","adhkli","qryiolnff"]
print(sort_by_length(w))