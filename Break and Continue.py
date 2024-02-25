for i in range(13):
    if (i == 10):
        break; # break skips the whole table after 10
    print("5 x", i , "=", 5*i)
print("break leaves the loop")


for j in range(13):
    if (j == 10):
        print("No 10 skipped by continue")
        continue;    #continue will skip the 10th iteration or 10th no. table
    print("5 x", j , "=", 5*j)
print("break leaves the loop")

k = 15
print(k%2) #Modulus/% gives remainder of the division

l = 0
while True:
    print(l)
    l= l+1
    if (l%100 == 0):
        break
    
while True:
    number = int(input("Enter a positive number: "))
    print(number)
    if not number>0:
        break
    
