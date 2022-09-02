# 1.

# # for x in range(151):
# #     print(x)


# 2.
# # for x in range(5,1000,5):
# #     print(x)

# 3.
# # for x in range(1,100):
# #     if x % 5 == 0:
# #         print ("Coding")
# #     if x % 10 == 0:
# #         print ("Coding Dojo")
# #     else:
# #         print (x)
# 4.
# # sum=0
# # for x in range(0,50):
# #     if (x % 2) != 0:
# #         sum = sum + x
# #         print(sum)



# 5.
# # for x in range(2018,0,-4):
# #     print(x)

# 6.
# # for x in range(1,500):
# #     if x % 5 == 0:
# #         print(x)





# def be_cheerful(name='', repeat=1):
# 	print(f"good morning {name}\n" * repeat)
# # # be_cheerful()    # output: good morning (repeated on 2 lines)
# # be_cheerful("tim")    # output: good morning tim (repeated on 2 lines)
# # be_cheerful(name="john")    # output: good morning john (repeated on 2 lines)
# # be_cheerful(repeat=6)    # output: good morning (repeated on 6 lines)
# be_cheerful(name="michael", repeat=5)    # output: good morning michael (repeated on 5 lines)
# # # NOTE: argument order doesn't matter if we are explicit when sending in our arguments!
# # be_cheerful(repeat=3, name="kb") 



# def multiply(num_list, num):
#     for x in num_list:
#         x *= num
#     return num_list
# a = [2,4,10,16]
# b = multiply(a,5)
# print(b)






# #3
# def number_of_books_on_hold():
#     return 5
#     return 10
# print(number_of_books_on_hold())



# def number_of_fingers():
#     return 5
#     print(10)
# print(number_of_fingers())


# person = {"first": "Ada", "last": "Lovelace", "age": 42, "is_organ_donor": True}
# # Adds a new key value pair for email to person
# person["email"] = "alovelace@codingdojo.com"
        
# # Changes person's "last" value to "Bobada"
# person["last"] = "Bobada"
# print(person)




# # print(person["first"])
# # full_name = person["first"] + " " + person["last"]








# # if "email" not in person:
# #     person["email"] = "newemail@email.com"
# # else:
# #     print("Would you like to replace your existing email?")






# # person = {"first": "Ada", "last": "Lovelace", "age": 42, "is_organ_donor": True}
# # capitals = {} #create an empty dictionary then add values
# # capitals["svk"] = "Bratislava"
# # capitals["deu"] = "Berlin"
# # capitals["dnk"] = "Copenhagen"

# # value_removed = capitals.pop('svk') # will remove the key 'svk' and return it's value
# # del capitals['dnk'] 



# users = [
#     {"first": "Ada", "last": "Lovelace"}, # index 0
#     {"first": "Alan", "last": "Turing"}, # index 1
#     {"first": "Eric", "last": "Idle"} # index 2
# ]
# # Dictionary of lists
# resume_data = {
#     #        	     0           1           2
#     "skills": ["front-end", "back-end", "database"],
#     #                0           1
#     "languages": ["Python", "JavaScript"],
#     #                0              1
#     "hobbies":["rock climbing", "knitting"]



# print(resume_data["skills"][1])


# print(users[2]["first"])



# def number_of_fingers():
#     return 5
#     print(10)
# print(number_of_fingers())

# def number_of_military_branches():
#     return 5
# print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())


person = {"first": "Ada", "last": "Lovelace", "age": 42, "is_organ_donor": True}
# Adds a new key value pair for email to person
person["email"] = "alovelace@codingdojo.com"
        
# Changes person's "last" value to "Bobada"
# person["last"] = "Bobada"
# print(person)

# print(person["first"])
# full_name = person["first"] + " " + person["last"]
# print(full_name)



# person.pop('last')
# print(person)


# del person['first']
# print(person)


def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())




