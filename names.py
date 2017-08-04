#part 1

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

for key in students:
     print key['first_name'], key['last_name']

#part II
 
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ], 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
 
def show_all(users):
      
    for key, data in users.items():
        count = 0  
        print key
        for value in data:
            count += 1
            first_name = value['first_name'].upper()
            last_name = value['last_name'].upper()
            length = len(first_name) + len(last_name)
            print "{} - {} {} - {}".format(count, first_name, last_name, length)
            
show_all(users)