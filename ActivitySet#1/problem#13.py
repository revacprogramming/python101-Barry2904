# Network Programming
# https://www.py4e.com/lessons/network
'''
Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
'''

name = "dataset/mbox-short.txt"
handle = open(name)
counts = {}
for line in handle:
    word = line.split()
    if len(word) < 3 or word[0] != "From" : continue
    full_hour = word[5]
    hour = full_hour.split(":")
    hour = str(hour[:1])
    hour = hour[2:4]
    if hour in counts :
        counts[hour] = 1 + counts[hour]
    else :
        counts.update({hour:1})
lst = list()
for k, v in counts.items():
    new_tup = (k, v)
    lst.append(new_tup)
 
lst = sorted(lst)    
for k, v in lst:
    print(k,v)
    

