# https://www.codingame.com/ide/puzzle/mime-type

table = {}

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    table[ext.lower()] = mt
for i in range(q):
    fname = input().split('.')  # One file name per line.

    if len(fname) > 1:
        try:
            print(table[fname[-1].lower()])
        except KeyError:
            print("UNKNOWN")
    else:
        print("UNKNOWN")
