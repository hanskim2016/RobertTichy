users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
def printPerson(list):
    i=0
    for object in list:
        i=i+1
        object['chars'] = len(object.get('first_name')) + len(object.get('last_name'))
        print i, '-', object.get('first_name').upper(),object.get('last_name').upper(), '-',object['chars']
for userGroup,people in users.items():
    print userGroup
    printPerson(people)

#this is very well done. You can save a tiny bit of typing by doing object['first_name'] instead of using .get, but it also will break if your data set loses those keys, so your choice seems justifiable to me. 	
