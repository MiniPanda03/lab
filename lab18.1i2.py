import linecache
a_file = open('pantadeusz.txt',encoding="utf8")

# zad 1
print(a_file.read())
# zad2
print("\n//////////////////////////////////////////////////")
a_file = open('pantadeusz.txt',encoding="utf8")
lines = [8,12,60,98,104]

for position, line in enumerate(a_file):
    if position in lines:
        print(position,line)
