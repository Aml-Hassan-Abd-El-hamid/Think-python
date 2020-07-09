def use_all(word,all):
    for letter in all:
        t=False
        for i in word:
            if letter==i:
                t=True
        if t==False:
            return False
    if t==True:
        return True
print(use_all("addsss","sda"))
def use_only(wor,only):
    return use_all(only,wor)
print(use_only("eeee","ea"))