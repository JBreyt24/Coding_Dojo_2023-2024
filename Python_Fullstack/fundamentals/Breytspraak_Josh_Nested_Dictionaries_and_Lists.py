# 1. Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# Change the last_name of the first student from 'Jordan' to 'Bryant'
# In the sports_directory, change 'Messi' to 'Andres'
# Change the value 20 in z to 30

# x = [ [5,2,3], [10,8,9] ] 
# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

#Outputs:

# x[1][0] = 15
# print(x)

# students[0]['last_name': 'Bryant']
# print(students)

# sports_directory['soccer'][0] = 'Andres'
# print(sports_directory['soccer'])

# z[0]['y'] = 30
# print(z)


# 2. Create a function iterateDictionary(some_list) that, given a list of dictionaries, 
# the function loops through each dictionary in the list and prints each key and the 
# associated value.

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

#Output:

# students = [
#         {'first_name':  'Michael', 'last_name' : 'Jordan'},
#         {'first_name' : 'John', 'last_name' : 'Rosales'},
#         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#         {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]

# def iterateDictionary(list):
#     for people in list:
#         for first_name, last_name in list[people].items():
#             return f"{first_name} - {last_name}"

# print(students)

# 3. Get Values From a List of Dictionaries Create a function iterateDictionary2(key_name, some_list) that, 
# given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. 
# For example, iterateDictionary2('first_name', students) should output:

# Michael
# John
# Mark
# KB

# And iterateDictionary2('last_name', students) should output:

# Jordan
# Rosales
# Guillen
# Tonel

#output:

# students = [
#         {'first_name':  'Michael', 'last_name' : 'Jordan'},
#         {'first_name' : 'John', 'last_name' : 'Rosales'},
#         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#         {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]

# def iterate_dictionary2(key_name,some_list):
#     for students in range(0, len(some_list)):
#         for first_name,last_name in list[students].items():
#             if first_name == key_name:
#                 print(last_name)
                
# iterate_dictionary2('first_name',students)
# iterate_dictionary2('last_name',students)

# 4. Iterate Through a Dictionary with List Values Create a function printInfo(some_dict) that given a dictionary 
# whose values are all lists, prints the name of each key along with the size of its list, 
# and then prints the associated values within each key's list. For example:
# dojo = {
#    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }

# printInfo(dojo)

# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank

# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon

#output:

# dojo = {
#     'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#     'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }

# def printInfo(some_dict):
#     for a,b in some_dict.items():
#         print(f"{len(b)} {a}")
#         for i in range(0, len(b)):
#             print(b[i])

# printInfo(dojo)