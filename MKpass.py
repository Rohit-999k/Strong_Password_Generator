import random
import string

def generate_strong_password():
    
    special_characters = "!@#$%&*_-"

    length = random.randint(10, 14) # set length bet 10 to 14

    num_special = random.randint(1, 2) # set special char 1 or 2

    uppercase = random.choice(string.ascii_uppercase)
    lowercase = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    specials = [random.choice(special_characters) for _ in range(num_special)]

    remaining_length = length - (3 + num_special)

    all_characters = string.ascii_letters + string.digits

    remaining_chars = [random.choice(all_characters) for _ in range(remaining_length)]

    # Combine everything
    password_list = [uppercase, lowercase, digit] + specials + remaining_chars

    # Shuffle the pass
    random.shuffle(password_list)

    password = "".join(password_list)

    return password


if __name__ == "__main__":
    print("🔐 Strong Password Generator")
    print("-" * 30)
    
    password = generate_strong_password()
    print("Generated Password: " ,end="")
    print(password,"\n")
