#  print the contents of a directory using the os module

import os

contents=os.listdir()

for content in contents:
    print(content)