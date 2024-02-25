x = int(input("Enter the value of x only 1 to 5: "))

match x:
     case 1:
         print("1 is stored in x")
     case 2:
         print ("2 is stored in x")
     case 3:
         print ("3 is stored in x")
     case 4:
         print ("4 is stored in x")
     case 5:
         print ("5 is stored in x")
     case 6:  
         print(x)
     case _ if x!=80: # _underscore is used for default case
         print (x,"is not 80")
     case _ if x!=90:  # _underscore is used for default case
         print (x,"is not 90")
     