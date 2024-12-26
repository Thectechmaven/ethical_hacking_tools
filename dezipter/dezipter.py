# -*- coding: utf-8 -*-

# Define color variables
green = "\033[1;32m"
clear = "\033[0m"

# ASCII art banner
ascii = ">  \r\n"
ascii += "██████╗ ███████╗███████╗██╗██████╗ ████████╗███████╗██████╗   \r\n"
ascii += "██╔══██╗██╔════╝╚══███╔╝██║██╔══██╗╚══██╔══╝██╔════╝██╔══██╗  \r\n"
ascii += "██║  ██║█████╗    ███╔╝ ██║██████╔╝   ██║   █████╗  ██████╔╝  \r\n"
ascii += "██║  ██║██╔══╝   ███╔╝  ██║██╔═══╝    ██║   ██╔══╝  ██╔══██╗  \r\n"
ascii += "██████╔╝███████╗███████╗██║██║        ██║   ███████╗██║  ██║  \r\n"
ascii += "╚═════╝ ╚══════╝╚══════╝╚═╝╚═╝        ╚═╝   ╚══════╝╚═╝  ╚═╝   \r\n"
ascii += "                                                              \r\n"
ascii += "                                                              \r\n"
ascii += "          ={>   C Y B E R T E C H   M A V E N   <}=            \r\n"
ascii += "                                                                \r\n"
ascii += "               GitHub   : Thectechmaven                                \r\n"
ascii += "               Medium   : @jbtechmaven                              \r\n"
ascii += "               Twitter  : @CyberTechMaven                           \r\n"

# Add colors
intro = green + ascii.replace(">", "").replace("<", "") + clear

# Print the banner
print(intro)

from zipfile import ZipFile

# Prompt the user for input values
def attempt_extract(zf_handle, password):
    try:
        zf_handle.extractall(pwd=password.encode())
        print("[+] Password found: " + password)
        return True
    except Exception:
        return False

def main():
    zip_file = input("Enter the path to the zip file: ")
    wordlist_file = input("Enter the path to the wordlist file: ")

    print("[+] Beginning brute force")
    try:
        with ZipFile(zip_file) as zf:
            with open(wordlist_file, 'rb') as f:
                password_found = False  # Flag to track if password is found
                for line in f:
                    password = line.strip().decode('iso-8859-1')
                    if attempt_extract(zf, password):
                        password_found = True  # Set the flag to True
                        break  # Exit the loop if password is found

        if not password_found:
            print("[-] Password not found in list")
    except FileNotFoundError as e:
        print(f"[!] File not found: {e}")
    except Exception as e:
        print(f"[!] An error occurred: {e}")

if __name__ == "__main__":
    main()
