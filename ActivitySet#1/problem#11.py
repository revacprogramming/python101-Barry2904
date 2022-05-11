# Dictionaries

#filename = "dataset/mbox-short.txt"
fname = input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh:
    pos=line.find("From ")
    if pos==0:
        words=line.split()
        print(words[1])
        count=count+1
print("There were", count,"lines in the file with From as the first word")
