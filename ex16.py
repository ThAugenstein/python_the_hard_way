from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit Ctrl-C(^C).")
print("If you do want that, hit Return.")

input("?")

print("Opening the file...")
target = open(filename, "w")

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line1> ")
line2 = input("line2> ")
line3 = input("line3> ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()

text = open(filename)
print(f"This is the content of the file {filename}:")
print("-" * 20)
print(text.read(), end="")
print("-" * 20)
