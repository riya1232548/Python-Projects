
import pyperclip
import os

FILE_NAME = "passwords.txt"


def save_password():
    website = input("Enter website: ").strip()
    password = input("Enter password: ")

    if not website or not password:
        print("Website and password cannot be empty.")
        return

    with open(FILE_NAME, "a", encoding="utf-8") as f:
        f.write(f"{website}<|<>{password}\n")

    print("Password saved successfully!")


def get_password():
    website = input("Enter website: ").strip()

    if not os.path.exists(FILE_NAME):
        print("No passwords saved yet.")
        return

    with open(FILE_NAME, "r", encoding="utf-8") as f:
        for line in f:
            saved_website, separator, password = (
                line.rstrip("\n").partition("<|<>")
            )

            if separator and saved_website.lower() == website.lower():
                pyperclip.copy(password)
                print("Password copied to clipboard!")
                return

    print("Website not found.")


def main():
    while True:
        print("\n===== PASSWORD MANAGER =====")
        print("1. Save Password")
        print("2. Get Password")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ").strip()

        if choice == "1":
            save_password()

        elif choice == "2":
            get_password()

        elif choice == "3":
            print("Exiting Password Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
