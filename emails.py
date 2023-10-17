def extract_name(email):
    name = email.split('@')[0]
    return name.replace('.', ' ').title()

def main():
    user_data = {}

    while True:
        email = input("Email: ")
        if not email:
            break

        name = extract_name(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirmation == 'n':
            name = input("Name: ").strip()

        user_data[email] = name

    print("\nName and Email Pairs:")
    for email, name in user_data.items():
        print(f"{name} ({email})")

if __name__ == "__main__":
    main()
