#Modify print_hist to print the keys and their values in alphabetical order.
def print_hist(h):
        l=[]
        for key in h:
            l+=[key]
        l.sort()
        for key in l:
            print (key,h[key])
print_hist({"l":1,"a":7,"t":4,"x":7,"b":0})