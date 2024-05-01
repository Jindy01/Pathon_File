# with open('new_FL', 'w') as f:
#     f.write('Hello ! New File')

# with open('new_FL', 'r') as f:
#     content = f.read()
#     print(content)

# Создание базы сотрудников !
with open('employees.txt', 'w') as f:
    f.write('John Doe 30\n')
    f.write('Alice Smith 25\n')
    f.write('Bob Johnson 35\n')
    f.write('Emily Brown 28\n')


with open('employees.txt', 'r') as f:
    for line in f:
        data = line.split()
        first_name = data[0]
        last_name = data[1]
        age = data[2]
        print(line)
        print(f"First Name: {first_name}, Last Name: {last_name}, Age: {age}")



