#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Define color variables
green = "\033[1;32m"
clear = "\033[0m"

# ASCII art banner
ascii = ">  \r\n"
ascii += "██████╗  █████╗ ███████╗███████╗██╗███████╗██╗███████╗██████╗     \r\n"
ascii += "██╔══██╗██╔══██╗██╔════╝██╔════╝██║██╔════╝██║██╔════╝██╔══██╗    \r\n"
ascii += "██████╔╝███████║███████╗███████╗██║█████╗  ██║█████╗  ██████╔╝    \r\n"
ascii += "██╔═══╝ ██╔══██║╚════██║╚════██║██║██╔══╝  ██║██╔══╝  ██╔══██╗    \r\n"
ascii += "██║     ██║  ██║███████║███████║██║██║     ██║███████╗██║  ██║    \r\n"
ascii += "╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝    \r\n"
ascii += "                                                                  \r\n"
ascii += "                                                                  \r\n"
ascii += "   ={>   C Y B E R T E C H   M A V E N   <}=                      \r\n"
ascii += "                                                                  \r\n"
ascii += "         GitHub   : Thectechmaven                                 \r\n"
ascii += "         Medium   : @jbtechmaven                                  \r\n"
ascii += "         Twitter  : @CyberTechMaven                               \r\n"

# Add colors
intro = green + ascii.replace(">", "").replace("<", "") + clear

# Print the banner
print(intro)

word = input("> Enter a word to modify into a password: ")
password = ''

for char in word:
    if char == 'i':
        password += '1'
    elif char == 'a':
        password += '@'
    elif char == 'm':
        password += 'M'
    elif char == 'B':
        password += '8'
    elif char == 's':
        password += '$'
    else:
        password += char

password += '!'
print(password)
