# f = open('myfile.txt' , 'r')
# i = 0
# while True:
#     i = i+1
#     line = f.readline()
#     if not line:
#         break
#     m1 = int(line.split(",")[0])
#     m2 = int(line.split(",")[1])
#     m3 = int(line.split(",")[2])
#     print(f"Marks of Student {i} in Maths is {m1}")
#     print(f"Marks of Student {i} in English is {m2}")
#     print(f"Marks of Student {i} in SST is {m3}")
#     print(line)
#     print(f"Total Marks of Student {i} are: {m1+m2+m3} \n")
    

g = open('myfile2.txt' , 'w')
line2 = ["How are you?" , "What about you?" , "Who are you?"]
for line1 in line2:
    print(line1 + "\n")
g.writelines(line2)
g.close()
 

with open('file.txt', 'r') as j:
    print(type(j))
    j.seek(10) # move to the 10th byte/letter in file.txt
    # Read the next 5 bytes
    print(j.tell())  # tells us about the end of seek
    data = j.read(5)   # reads the next 5 bytes/letters after 10th byte/letter as in seek(10)
    print(data)
    
    
# For levying/imposing limit of read
with open("sample.txt", "w") as k:
    k.write("Waheed!, How are you?")
    k.truncate(6)   # means it prints the first five characters/bytes and deletes the further letters.

with open('sample.txt' , 'r') as l:
    read = l.read()
    print(read)

 



    