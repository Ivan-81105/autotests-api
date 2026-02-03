from faker import Faker

fake = Faker('ru_RU')

print(fake.name())
print(fake.address())
print(fake.password(length=14, upper_case=True, lower_case=True))
print(fake.email(domain='rt.com'))

data = {
    "name": fake.name(),
    "email": fake.email(),
    "age": fake.random_int(min=18, max=100)
}
# print(data)