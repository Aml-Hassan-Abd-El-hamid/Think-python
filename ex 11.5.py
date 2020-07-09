#Exercise 11.5 Read the documentation of the dictionary method setdefault and use it to write a
#more concise version of invert_dict.
def invert_dict(d):
    inv=dict()
    for key in d:
        val=d.setdefault(key,-1)
        if val!=-1:
            if val not in inv:
                inv[val]=[key]
            else:
                inv[val].append(key)
    print(inv)
invert_dict({"a":5,"t":8,"c":9,"l":5})