students_DB={}
#ask input from user or 'q' to exit
while True:
    line=input('Please input the id and name separated by comma or q to exit:')
    if line == 'q':
        break
    id, name = line.split(',')
    students_DB.update({id:name})

for x,y in students_DB.items():
    print(x,y)

key=input('Enter id to search:')
if key in students_DB:
    print('key=',key,'value=',students_DB[key])
else:
    print('key not found')
