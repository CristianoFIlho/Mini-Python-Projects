import random
import string


def generate_password():
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = []
    password.append(random.choice(string.ascii_uppercase))
    password.append(random.choice(string.ascii_lowercase))
    password.append(random.choice(string.digits))
    password.append(random.choice(string.punctuation))

    for i in range(12):
        password.append(random.choice(all_characters))

    random.shuffle(password)
    return "".join(password)


password = generate_password()
print(password)

# Save the password to a file
with open("key.key", "w") as f:
    f.write(password)
