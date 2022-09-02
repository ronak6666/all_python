
#1


x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20}]



x[1][0]=15
print(x)

students[0]['last_name'] = 'Bryant' 
print(students)

sports_directory['soccer'][0] = 'Andreas' 
print(sports_directory)

z[0]['y'] = 30
print(z)



#2


students = [
{'first_name':  'Michael', 'last_name' : 'Jordan'},
{'first_name' : 'John', 'last_name' : 'Rosales'},
{'first_name' : 'Mark', 'last_name' : 'Guillen'},
{'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


# for x in students:
#     print (x)

def itterate_dictionary(key, key2,list):
    for i in range(0,len(list)):
        print(f"{list[i][key]} - {list[i][key2]}")
        # print(list[i][key], list[i][key2])

itterate_dictionary('first_name','last_name', students)





#3


def itterate_dictionary(key,list):
    for i in range(0,len(list)):
        print(f"{list[i][key]})
        # print(list[i][key], list[i][key2])

itterate_dictionary('first_name', students)






# def current_info(list):
#     for key in list: 
#         print(key)
#         for i in range(len(list[key])):
#             print(list[key][i])


# current_info(students)
# for val in students.values():
#     print(val)

#     print(type(x))


#     students[i][first_name]

# x = students.values()
# print(x)
    


# def iterateDictionary(students):
#     for x in students:
#         return x

# iterateDictionary(students)






# iterateDictionary(students) 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel
















#4


dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}




def printInfo(dict):
    for key in dict:
        print((len(dict[key])),key)
        for j in range(len(dict[key])):
            print(dict[key][j])

printInfo(dojo)



# nums = {
#     '1#':[1,2,3,4,5],
#     '2#':[6,7],
#     '3#':[11,12,13,14,15,19,23]
#     }


# def keyFthree(dict):
#     for key in dict:
#         print(key)
#         for i in range(len(dict[key])):
#             print(dict[key][i])

            #if you want just first 2 of all listes do range(2)in line 137





# keyFthree(nums)
