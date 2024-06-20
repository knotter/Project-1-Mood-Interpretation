import os
import sys
project_root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(project_root_path)


def load(a):
    split = os.path.split(a)
    print(split[1])
    if a == os.path.abspath(split[1]):
        print("Bingo")
    else:
        print(a)
        print(os.path.abspath(split[1]))
        print("poop")

    with open(a)e as file:
        print(file.read(), "GOOOOOOD")
    #dictionary1_path = "../ext-lib/dictionary1.txt"
    #dictionary2_path = "../ext-lib/dictionary2.txt"
    #if dictionary1_path == a or dictionary2_path == a:
        #print("Bingo")
    return "Good"