letter = "Hey my name is {} and I'm from {}"
name = "Waheed"
country = "Pakistan"

print(letter.format(name, country))  # this is without f string it can be used but it is not convenient when we are working on a large program/coding
print(f"Hey my name is {name} and I'm from {country}") # this is f-string

price  = 49.0999
txt = f"For only {price:.2f} USD"
print(txt)

multiply = f"{2*30}" # we can do calculation in strings through f-string
print(multiply)