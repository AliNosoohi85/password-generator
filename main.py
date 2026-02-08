import string, random

def generate_char_set(use_lower : bool = True, use_upper : bool = True, use_numbers : bool = True, use_special : bool = True) -> set[str]:
    char_set = set()
    if use_lower: char_set.update(set(string.ascii_lowercase))
    if use_upper: char_set.update(set(string.ascii_uppercase))
    if use_numbers: char_set.update(set(string.digits))
    if use_special: char_set.update(set(string.punctuation))

    if not char_set:
        char_set.update(set(string.ascii_lowercase))

    return char_set

def generate_password(password_length : int, char_set : set[str]) -> str:
    char_list = list(char_set)
    return "".join(random.choice(char_list) for _ in range(password_length))

def ask_int() -> int:
    while True:
        try:
            password_length = int(input("Enter the length of password: "))
            if password_length <= 0:
                print("Password length must be a positive integer.")
                continue
        except ValueError:
            print("Password must be a positive integer.")
            continue
        else:
            break
    return password_length

if __name__ == "__main__":
    password_length = ask_int()

    use_lower = input("Use lowercase characters in password?(y/n) ").lower() == "y"
    use_upper = input("Use uppercase characters in password?(y/n) ").lower() == "y"
    use_numbers = input("Use numbers in password?(y/n) ").lower() == "y"
    use_special = input("Use special character in password?(y/n) ").lower() == "y"

    char_set = generate_char_set(use_lower, use_upper, use_numbers, use_special)
    password = generate_password(password_length, char_set)
    print("Your password: ", password)