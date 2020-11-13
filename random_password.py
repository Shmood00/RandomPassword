import secrets, string

def generate_random_password(length):
    secretGenerator = secrets.SystemRandom()

    pass_chars = string.ascii_letters+string.punctuation

    finalPass = ""

    for _ in range(length):
        randNum = secretGenerator.randint(0,9)
        randChar = secretGenerator.choice(pass_chars)

        finalPass += secretGenerator.choice(str(randNum)+randChar)

    return finalPass