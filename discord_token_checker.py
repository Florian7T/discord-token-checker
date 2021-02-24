import os,requests,subprocess
from colorama import Fore

api = 'https://discord.com/api/v8/'

title = Fore.YELLOW+"""
  ______      __                 ________              __            
 /_  __/___  / /_____  ____     / ____/ /_  ___  _____/ /_____  _____
  / / / __ \/ //_/ _ \/ __ \   / /   / __ \/ _ \/ ___/ //_/ _ \/ ___/
 / / / /_/ / ,< /  __/ / / /  / /___/ / / /  __/ /__/ ,< /  __/ /    
/_/  \____/_/|_|\___/_/ /_/   \____/_/ /_/\___/\___/_/|_|\___/_/     
"""

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def checkTokens(token_in:list):
    headers = {
        'Authorization': '',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
    }
    for x in token_in:
        tokebn =str(x).replace('\n','')
        headers['Authorization'] = tokebn
        request = requests.post(f'{api}users/@me/channels', headers=headers)
        if request.status_code != 401:
            print(Fore.GREEN+f'- {tokebn} | valid!')


if __name__=="__main__":
    clear()
    print(title)
    file_path = input("Tokenlist file: ")
    tokens = None
    if not os.path.exists(file_path):
        print(Fore.RED+"Invalid filepath: "+file_path+Fore.RESET)
        exit(0)
    else:
        with open(file_path,'r') as f:
            tokens = f.readlines()
    checkTokens(tokens)
    print(Fore.RESET)
