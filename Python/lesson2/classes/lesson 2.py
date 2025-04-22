class User:
    age = 0
    name = ""
    email = ""

phone_number = "+7..."

num1 = 10
num2 = 20

user1 = User()
user1.age = 20
user1.name = 'Имя1'
user1.email = 'email1@mail.ru'

user2 = User()
user2.age = 30
user2.name = 'Имя2'
user2.email = 'email2@mail.ru'

print(user1.age)
user1.age = 45
print(user1.age)
print(user2.age)