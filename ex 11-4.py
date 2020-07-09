#Exercise 11.4 Modify reverse_lookup so that it builds and returns a list of all keys that map to v,
#or an empty list if there are none.
def reverse_lookup(v,d):
    keys=[]
    for k in d:
        if d[k]==v:
            keys+=[k]
    return keys
d={"t":1,"y":9,"u":9}
print(reverse_lookup(8,d))