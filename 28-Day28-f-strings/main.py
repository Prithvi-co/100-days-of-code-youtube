letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Harry"

print(letter.format(country, name))    #country goes to 0 and name goes to 1 in letter
print(f"Hey my name is {name} and I am from {country}")
print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}")      #prints without replacing name and country
price = 49.09999
txt = f"For only {price:.2f} dollars!"        #.2f lgane se two decimal places tkk round off hota h
print(txt)
# print(txt.format())
print(type(f"{2 * 30}"))    #type string
