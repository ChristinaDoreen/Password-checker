while True:
    pwd = input("\nEnter your password: ")

    if pwd.lower() in ["qwerty", "abcdefg", "password", "123456", "admin"]:
        print("\nPassword is too common. Please choose a stronger password.")
    elif len(pwd) < 8:
        print("\nPassword must be at least 8 characters long.")
    elif not any(char.isupper() for char in pwd):
        print("\nPassword must contain at least one uppercase letter.")
    elif not any(char.islower() for char in pwd):
        print("\nPassword must contain at least one lowercase letter.")
    elif not any(char.isdigit() for char in pwd):
        print("\nPassword must contain at least one digit.")
    elif not any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" for char in pwd):
        print("\nPassword must contain at least one special character.")
    else:
        print("\nPassword is valid.")
        break