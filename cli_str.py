def divider(char="/", length=80):
    print(char * length)

def banner():
    divider("=")
    print()
    print("        🚀 BINANCE FUTURES TRADING BOT CLI 🚀")
    print()
    divider("=")

def menu():
    print("\nSelect an option:")
    print("1. Check Balance")
    print("2. Place Market Order")
    print("3. Place Limit Order")
    print("4. Place Stop-Limit Order")
    print("5. Grid Trading Strategy")
    print("6. TWAP Trading Strategy")
    print("7. Exit")
    choice = input("Enter your choice : ")
    return choice

def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
