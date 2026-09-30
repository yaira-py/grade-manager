students_grades={}

def add_student(name,grade):
    students_grades[name]=grade
    print(f'Added {name} with a {grade}')

def update_student(name,grade):
    if name in students_grades:
        students_grades[name]=grade
        print(f'{name} with marks are updated {grade}')

    else:
        print(f'{name} not found')

def deleted_student(name):
    if name in students_grades:
      del students_grades[name]

    else:
        print(f'{name} not found')


def view_all():
    if students_grades:
        for name,grade in students_grades.items():
            print(f'{name} : {grade}\n')

    else:
        print('No Student Found/Added')


def main():
    while True:
        print('---main---')
        print('1.Add Student\n , 2.Update Student\n , 3.View Students\n , 4.Delete Student\n , 5.Exit\n')

        choice=input('Enter your choice: ')
        if choice=="1":
            name=input('Enter Student Name: ')
            grade=input('Enter Student Grade: ')
            add_student(name,grade)

        elif choice=='2':
            name=input('Enter Student Name: ')
            grade=input('Enter Student Grade: ')
            update_student(name,grade)

        elif choice=='3':
            view_all()

        elif choice=='4':
            name=input('Enter Student Name: ')
            deleted_student(name)

        elif choice=='5':
            break

        else:
            print('Invalid Choice')


main()
