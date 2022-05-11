largest = 0
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        temp=int(num)
    except:
        print("Invalid input")
        continue
    if smallest is None:
        smallest=temp
    if largest<temp:
        largest=temp
    elif temp<smallest:
        smallest=temp    

print("Maximum is", largest)
print("Minimum is", smallest)
            