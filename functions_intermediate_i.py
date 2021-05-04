#--1
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#1
x[1][0] = 15
print(x)

#2
students[0]['last_name'] = 'Bryant'
print(students)

#3
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

#4
z[0]['y'] = 30
print(z)


#--2
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_list):
    for i in some_list:
        print(f"first_name - {i['first_name']}, last_name - {i['last_name']}")

iterateDictionary(students)

#--3
def iterateDictionary2(key_name, some_list):
    for i in some_list:
        print(i[key_name])

iterateDictionary2('first_name',students)

#--4
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
# print(dojo['locations'])

def printInfo(some_dict):
    # i=0
    for i in some_dict:
        for n in range(0, len(some_dict[i]), 1):
            num=n+1
            print(num)
            # print(dojo['locations'])
            # print(n)



printInfo(dojo)