import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_symbols=True):
    
    characters = string.ascii_lowercase  # Letras minúsculas

    if use_uppercase:
        characters += string.ascii_uppercase  
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation 
        password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    while True:
        length = int(input("Introduce la longitud de la contraseña: "))
        if length < 3:
            print("No se puede crear la contraseña, longitud errónea. Inténtalo de nuevo.")
        else:
            break
    use_uppercase = input("¿Incluir mayúsculas? (Si/No): ").lower() == 's'
    use_digits = input("¿Incluir dígitos? (Si/No): ").lower() == 's'
    use_symbols = input("¿Incluir símbolos? (Si/No): ").lower() == 's'
    password = generate_password(length, use_uppercase, use_digits, use_symbols)
    print("Tu contraseña generada es:", password)