import time
import string
import random
from classes import find_by_tag

def randomtag():

    time1=time.time()
    a=str(int(time1))
    b=a[-2:]
    c=b[:1]
    d=b[1:]


    while (True):
        i=6
        tag=""
        while i>0:
            tag=tag+random.choice(string.ascii_letters)
            i=i-1
        if find_by_tag(tag) is None:
            return d+tag+c
