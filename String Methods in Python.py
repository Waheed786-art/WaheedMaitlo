#Strings are immutable(unchangeable)
a = "!!!Waheed!!!! Naveed Ali Waheed"
print(a.count("Waheed"))
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!")) # Strip means skip.. it only skips the character only at the end.
print(a.replace("Waheed","Naveed"))
print(a.split(" "))

friendname="atif"
print(friendname.capitalize())

str1 = "Welcome to the console!"
print(len(str1))
print(str1.center(50))
print(len(str1.center(50)))
print(str1.endswith("console"))
print(str1.endswith("console!"))

name= "His name is Najaf. He is an honest man."
print (name.find("is")) # used when we want answer even if the letter is not present in the sentence
print(name.find("ishh")) # Output -1
print(name.index("is")) # if we want that our program through an error if the letter is not present in the word or sentence.

str2 = "WelcomeToTheConsole"
print(str2.isalnum()) #It means that str2 contains alphanumeric data alphbet like A-Z, a-z, 0-9..

str3 = "Welcome7"
print(str3.isalpha()) # Only alphabet
print(str2.isalnum()) # Alphabet and numeric both

str4 = "HELLOW"
str5 = "how are you"
print(str5.islower()) # All letters in str5 are small so it will give true in output
print(str4.islower()) #Output   False because str4 has capital letters stored
print(str4.isupper()) # All letters must be in Uppercase so that is upper will work

str6 = "Education is the weapon through which a person can change the world\n"
print(str6.isprintable()) #\n is not printable it just provides new line so it is not printable

str7 = "        "
print(str7.isspace()) # True because str7 contains only spaces
str8 = "    Naveed   "
print(str8.isspace()) # return false because str8 contains aphabets 

str9 = "World Health Organization"
print(str9.istitle()) # if first letter of every word is capital then it will return true otherwise false.

str10 = "Organisation of Islamic Cooperation"
print(str10.startswith("Organisation")) # gives true because str10 starts with Organisation.

str11 = "Python is an Interpreted Language"
print(str11.swapcase()) # converts uppercase into lower and lower into upper 

str12 = "His name is Dan. He is an honest man"
print(str12.title())# makes first letter of every word capital


