

inp = input("please enter your string here:")

size = len(inp)
count = 0
i = 0

if size%2 == 0:
    new_size = int(size/2) -1
    for i in range(0,new_size):
        if inp[i] == inp[size-i-1]:
            count = count + 0
        else:
            count = count + 1

if size%2 == 1:
    new_size = int((size-1)/2) - 1
    for i in range(0,new_size):
        if inp[i] == inp[size-i-1]:
            count = count + 0
        else:
            count = count + 1

if count == 0:
    print("Its a palindrome")
else:
    print("Its not a palindrome")


