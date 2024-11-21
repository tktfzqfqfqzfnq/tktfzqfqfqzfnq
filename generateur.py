import random
import string
import os

characters = string.ascii_uppercase + string.digits

def generate_steam_code(length):
    return ''.join(random.choice(characters) for _ in range(length))

def generate_amazon_activation_codes():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
    print("Generating Amazon Activation Codes:")
    num_codes = 20  # Generate 20 codes
    code_length = 20
    while num_codes > 0:
        code = ''.join(random.choice(characters) for _ in range(code_length))
        print(f"https://www.amazon.com/activate/{code}")
        num_codes -= 1
    input("Press Enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen

def generate_steam_activation_codes():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
    print("Generating Steam Activation Codes:")
    num_codes = 20  # Generate 20 codes
    code_length = 15
    while num_codes > 0:
        steam_code = generate_steam_code(code_length)
        print(f"https://store.steampowered.com/account/registerkey?key={steam_code}")
        num_codes -= 1
    input("Press Enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen

def generate_roblox_redemption_codes():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
    print("Generating Roblox Redemption Codes:")
    num_codes = 20  # Generate 20 codes
    code_length = 10
    while num_codes > 0:
        code = ''.join(random.choice(characters) for _ in range(code_length))
        print(f"https://www.roblox.com/gamecard-redeem/{code}")
        num_codes -= 1
    input("Press Enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen

def generate_google_play_redeem_codes():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
    print("Generating Google Play Redeem Codes:")
    num_codes = 20  # Generate 20 codes
    code_length = 16
    while num_codes > 0:
        code = ''.join(random.choice(characters) for _ in range(code_length))
        print(f"https://play.google.com/store/redeem?code={code}")
        num_codes -= 1
    input("Press Enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen

def generate_apple_activation_codes():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
    print("Generating Apple Activation Codes:")
    num_codes = 20  # Generate 20 codes
    code_length = 16
    while num_codes > 0:
        code = ''.join(random.choice(characters) for _ in range(code_length))
        print(f"https://www.apple.com/activate/{code}")
        num_codes -= 1
    input("Press Enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen

def main():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen

    # ASCII logo
    print(r'''
   _ _       ____  ____   ___________   __
  /   | |     / / __ \/ ____/  / ____/ ____/ | / /
 / /| | | /| / / /_/ / /      / / __/ __/ /  |/ / 
/ _ | |/ |/ / , _/ /__   / /_/ / /___/ /|  /  
/_/  |_|__/|__/_/ |_|\____/   \____/_____/_/ |_/   
                                                  
    ''')

    print("Made by wock")

    while True:
        print("\nGen options:")
        print("\033[36m1. Amazon Gen")
        print("2. Steam Gen")
        print("3. Roblox Gen")
        print("4. Google Play Gen")
        print("5. Apple Gen")
        print("6. Exit\033[0m")
        choice = input("Enter your choice: ")

        if choice == "1":
            generate_amazon_activation_codes()
        elif choice == "2":
            generate_steam_activation_codes()
        elif choice == "3":
            generate_roblox_redemption_codes()
        elif choice == "4":
            generate_google_play_redeem_codes()
        elif choice == "5":
            generate_apple_activation_codes()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()