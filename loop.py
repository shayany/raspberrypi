from sys import argv

x = 11
try:
    if(argv[1].isdigit()):
        x = int(argv[1]) + 1
except Exception:
    print("10x10 Multipication table")
    
for i in range(1,x):
    for j in range(1,x):
        print("%3d" % (i*j)," ", end="")
    print("\n")
