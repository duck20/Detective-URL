import requests
from colorama import Fore

while True:
    try:
        print(Fore.GREEN + '''
    ▒█▀▀▄ █▀▀ ▀▀█▀▀ █▀▀ █▀▀ ▀▀█▀▀ ░▀░ ▀█░█▀ █▀▀ 　 ▒█░▒█ ▒█▀▀█ ▒█░░░ 
    ▒█░▒█ █▀▀ ░░█░░ █▀▀ █░░ ░░█░░ ▀█▀ ░█▄█░ █▀▀ 　 ▒█░▒█ ▒█▄▄▀ ▒█░░░ 
    ▒█▄▄▀ ▀▀▀ ░░▀░░ ▀▀▀ ▀▀▀ ░░▀░░ ▀▀▀ ░░▀░░ ▀▀▀ 　 ░▀▄▄▀ ▒█░▒█ ▒█▄▄█

                  ●❯────────────｢⊙｣───────────❮●
                  ● Tool created by Mr Empy   ●
                  ● Version 1.0               ●
                  ●❯────────────｢⊙｣───────────❮●
                               ''')

        site=input(Fore.GREEN + '[!] Paste the Site URL: ')
        wdl_directory=input(Fore.GREEN + '[!] Paste your Wordlist directory: ')

        print(Fore.GREEN + '')
        print('=================================================')
        print('[+] URL:', site)
        print('[+] Wordlist:', wdl_directory)
        print('[+] Status: 200, 301, 302, 307, 403')
        print('=================================================')
        print('')

import keyboard  # using module keyboard
while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('ctrl+c'):  # if key 'q' is pressed 
            print('You Pressed A Key!')
            break  # finishing the loop

        wrd_lst=open(wdl_directory, "r")
        read_lines=wrd_lst.readlines()
        for line in read_lines:
            lst=line.strip('\r\n')
            result=requests.get(site + lst)
            if (result.status_code == 200):
                print(Fore.GREEN + '[+]', Fore.WHITE + site + lst, Fore.GREEN + '(status: 200)')
            if (result.status_code == 204):
                print(Fore.GREEN + '[+]', Fore.WHITE + site + lst, Fore.GREEN + '(status: 204)')
            if (result.status_code == 301):
                print(Fore.GREEN + '[+]', Fore.WHITE + site + lst, Fore.GREEN + '(status: 301)')
            if (result.status_code == 302):
                print(Fore.GREEN + '[+]', Fore.WHITE + site + lst, Fore.GREEN + '(status: 302)')
            if (result.status_code == 307):
                print(Fore.GREEN + '[+]', Fore.WHITE + site + lst, Fore.GREEN + '(status: 307)')
            if (result.status_code == 403):
                print(Fore.GREEN + '[+]', Fore.WHITE + site + lst, Fore.GREEN + '(status: 403)')
        print('')
        print(Fore.GREEN + "[+] Finished!")
        break

    except:
        pass
