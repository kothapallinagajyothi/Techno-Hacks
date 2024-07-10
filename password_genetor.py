import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Random Password Generator")

    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Length should be a positive integer.")
                continue

            password = generate_password(length)
            print(f"Generated Password: {password}")

            break  # Exit the loop after generating the password
        except ValueError:
            print("Invalid input. Please enter a valid integer for the length.")

if __name__ == "__main__":
    main()
