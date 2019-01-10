import time
import string
import random

def randomtag():
    time1=time.time()
    time2=time1
    letters=""

    i=5
    while i>0:
        letters=letters+random.choice(string.ascii_letters)
        i=i-1

    tag=letters+(str(time2))
    tag1 = tag.replace(".", "")
    return  tag1
