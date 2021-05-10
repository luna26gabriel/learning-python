usersnames = ['Luna', 'Batata', 'Anna']
passwords = ("123", "password", 'abcd')

# users = zip(usersnames, passwords)
# users = list(zip(usersnames, passwords))
users = dict(zip(usersnames, passwords))

for (key,value) in users.items():
    print(key, value)