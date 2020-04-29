import os

print(os.getcwd())

# Open to enable to write
f = open("example.txt", "w")
f.write("This\n is\n a\n example")
f.close()

# Open to enable to read
f = open("example.txt", "r")
s = f.read()
f.close()
print(s)