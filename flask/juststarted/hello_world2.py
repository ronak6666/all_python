# name = "Zen"
# print("My name is", name)


first_name = "Alana"
last_name = "Da Silva"
age = 36
profession = "Software Developer"
years_experience = 5

greeting = (f"Hello my name is {first_name} {last_name} ")

print(greeting) 

print(f"I am {age} years old") 
# Desired output: I am 36 years old

print("I work as a {}.".format(profession))
# Desired output: I work as a Software Developer.

exp_string = f"I have worked in the field for {years_experience} years."
print(exp_string)


# OR 


exp_string = "I have worked in the field for {} years." 
print(exp_string.format(years_experience))

#OR

print( "I have worked in the field for {} years." .format(years_experience))



print("I started in the field when I was " + str(age - years_experience) + " years old.")

print("This is TYPED in the TERMINAL by VIM- SO COOL")
