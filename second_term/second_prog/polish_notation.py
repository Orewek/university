from ctypes import WinDLL

parser = WinDLL(r".\parser.dll")
print("PARSER WAS SUCCESSFULLY LOADED")

# our_string = str(input())
parser.main()

with open("stack.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        print(line)
        print("here")
