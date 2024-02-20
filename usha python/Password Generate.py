import string
import random

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

def main():
    length = int(input("Enter the length of the password: "))
    password = generate_password(length)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()