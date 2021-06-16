import string
import secrets

print("Recomendamos o uso de uma senha com mais de 8 caracteres.")

n = input("Digite o tamanho da senha (Recomendado = 16): ") or 16
n = int(n)

special_chars = "!@#$%^&*()"

def isspecial(char):
    if char in special_chars:
        return True
    return False

def password_generator(n):
    if n < 6:
        return "A senha que voce esta tentando gerar e muito curta."
    char_set = string.ascii_letters + string.digits + special_chars

    while True:
        password = ''.join(secrets.choice(char_set) for i in range(n))
        if (any(c.islower() for c in password) and any(c.isupper()
                                                       for c in password)
                and any(c.isdigit() for c in password)
                and any(isspecial(c) for c in password)):
            return password


print(password_generator(n))
