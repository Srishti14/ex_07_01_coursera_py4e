fname = input("Enter file name:")
thefile = open(fname)

for line in thefile:
    line1 = line.rstrip()
    print(line1.upper())
