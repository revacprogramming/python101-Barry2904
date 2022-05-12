# Regular Expressions
# https://www.py4e.com/lessons/regex

# name = input("Enter file:")
#if len(name) < 1:

count=0
max=0
dictionary=dict()
name = "dataset/mbox-short.txt"
handle = open(name)
for line in handle:
    pos=line.find("From ")
    if pos==0:
        words=line.split()
        if words[1] not in dictionary.keys():
            add={words[1]:1}
            dictionary.update(add)

        elif words[1] in dictionary.keys():
            count=dictionary.get(words[1])
            count=count+1
            add={words[1]:count}
            dictionary.update(add)
            
bigcount=0
for word,count in dictionary.items(): 
    if count > bigcount:
        bigcount = count
        bigword = word

print (bigword,bigcount)
