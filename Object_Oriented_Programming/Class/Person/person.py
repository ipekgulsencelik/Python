from uuid import uuid4
import re


class Person:
    id = 0
    first_name = ""
    last_name = ""
    gender = ""
    age = 0
    birth_date = ""
    phone = ""
    email = ""
    city = ""
    address = ""
    user_name = ""
    password = ""
    salary = 0


def show_information(id: int, first_name: str, last_name: str, gender: str, age: int, birth_date: str, phone: str, email: str, city: str, address: str, user_name: str, password, salary: int):
    print('Person Information:\n'
          f'ID: {id}\n'
          f'Name: {first_name}\n'
          f'Surname: {last_name}\n'
          f'Gender: {gender}\n'
          f'Age: {age}\n'
          f'Birth Date: {birth_date}\n'
          f'Phone Number: {phone}\n'
          f'Email Address: {email}\n'
          f'City: {city}\n'
          f'Address: {address}\n'
          f'User Name: {user_name}\n'
          f'Password: {password}\n'
          f'Salary: {salary}\n')


def create_mail_address(full_name: str):
    # return f"{full_name.split(' ')[0]}.{full_name.split(' ')[-1]}@mail.com"
    return create_user_name(full_name) + "@mail.com"


def create_user_name(full_name: str):
    return f"{full_name.split(' ')[0]}.{full_name.split(' ')[-1]}"


def check_password():
    while True:
        password = input("Enter Your Password: ")
        if len(password) < 8 or len(password) > 20:
            print("Password length should be between 8 and 20 characters")
        elif not re.search(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,20}$", password):
            print("Password should have at least 8 characters including uppercase, lowercase, numbers and special characters")
            if not re.search("[0-9]", password):
                print("Password should have at characters including numbers")
            if not re.search("[A-Z]", password):
                print("Password should have at characters including uppercase")
            if not re.search("[a-z]", password):
                print("Password should have at characters including lowercase")
            if not re.search("[@$!%*?&]", password):
                print("Password should have at characters including special characters") 
        else:
            print("Password is valid")
            break
    return password


person_1 = Person()

person_1.id = uuid4()
person_1.first_name = "Michelle"
person_1.last_name = "Smith"
person_1.gender = "Woman"
person_1.age = 38
person_1.birth_date = "10.10.1985"
person_1.phone = "+90 (535) 123-45-67"
person_1.email = "michella@gmail.com"
person_1.city = "London"
person_1.address = "London, UK"
person_1.user_name = "michelle.smith"
person_1.password = "12345"
person_1.salary = 10000

show_information(person_1.id, person_1.first_name, person_1.last_name, person_1.gender, person_1.age, person_1.birth_date,
                 person_1.phone, person_1.email, person_1.city, person_1.address, person_1.user_name, person_1.password, person_1.salary)

person_2 = Person()

person_2.id = uuid4()
person_2.first_name = input("Enter Your Name: ")
person_2.last_name = input("Enter Your Surname: ")
person_2.gender = input("Enter Your Gender: ")
person_2.age = int(input("Enter Your Age: "))
person_2.birth_date = input("Enter Your Birth Date: ")
person_2.phone = input("Enter Your Phone Number: ")
# person_2.email = input("Enter Your Email Address: ")
full_name = person_2.first_name.lower().strip() + ' ' + \
person_2.last_name.lower().strip()
person_2.email = create_mail_address(full_name)
person_2.city = input("Enter Your City: ")
person_2.address = input("Enter Your Address: ")
# person_2.user_name = input("Enter Your User Name: ")
person_2.user_name = create_user_name(full_name)
# person_2.password = input("Enter Your Password: ")
person_2.password = check_password()
person_2.salary = int(input("Enter Your Salary: "))

show_information(person_2.id, person_2.first_name, person_2.last_name, person_2.gender, person_2.age, person_2.birth_date,
                 person_2.phone, person_2.email, person_2.city, person_2.address, person_2.user_name, person_2.password, person_2.salary)
