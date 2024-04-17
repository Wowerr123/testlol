Python
from microbit import *
import os
sleep(1500)

file = open("foo.txt", "w")
file.write("hello world")
file.close()

s = ""
allFiles = os.listdir()
for str in  allFiles  :
    s+= str

display.scroll(s )
