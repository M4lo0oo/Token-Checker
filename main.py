import requests
import os

def check_token(token):
    url = "https://discord.com/api/v9/users/@me"
    headers = {
        "Authorization": token
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(f"Error during connection: {e}")
        return False

def print_colored(message, color):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "reset": "\033[0m"
    }
    return f"{colors.get(color, colors['reset'])}{message}{colors['reset']}"

def main():
    if not os.path.exists("token.txt"):
        print("The file 'token.txt' was not found. Make sure it is in the same folder as this script.")
        return

    with open("token.txt", "r") as file:
        tokens = file.readlines()

    tokens = [token.strip() for token in tokens if token.strip()]

    if not tokens:
        print("No tokens found in 'token.txt'.")
        return

    print("\n--- Starting token validation ---\n")

    for token in tokens:
        is_valid = check_token(token)
        if is_valid:
            print(print_colored(f"[VALID] The token is valid: {token}", "green"))
        else:
            print(print_colored(f"[INVALID] The token is invalid: {token}", "red"))

    print("\n--- Token validation completed ---")

if __name__ == "__main__":
    main()
