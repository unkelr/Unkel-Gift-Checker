import asyncio
import aiohttp
import os
import discord
from colorama import Fore
import time



def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

cls()
os.system('title UNKEL GIFT CHECKER')
print(Fore.RED + "Star : https://github.com/unkelr/Unkel-Gift-Checker/")

async def check_gift_code(code, session, proxy):
    try:
        async with session.get(f'https://discord.gift/{code}', proxy=proxy) as resp:
            if resp.status == 200:
                return f"Valid Nitro Gift Code!"
            elif resp.status == 404:
                return "Invalid Nitro Gift Code!"
            else:
                return "An error occurred while checking the code."
    except aiohttp.ClientProxyConnectionError:
        return "Error: Proxy Connection Failed"

def read_codes():
    try:
        with open('codes.txt', 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        return []

def read_proxies():
    try:
        with open('proxies.txt', 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        return []

def write_codes(codes):
    with open('codes.txt', 'w') as file:
        file.writelines(codes)

async def main():
    print(Fore.RED + "Do you want to use proxies? (y/n): ")
    use_proxies = input().lower().strip() == 'y'

    if use_proxies:
        proxies = read_proxies()

    print(f"""{Fore.RED}


╦ ╦╔╗╔╦╔═╔═╗╦    ╔═╗╦ ╦╔═╗╔═╗╦╔═╔═╗╦═╗
║ ║║║║╠╩╗║╣ ║    ║  ╠═╣║╣ ║  ╠╩╗║╣ ╠╦╝
╚═╝╝╚╝╩ ╩╚═╝╩═╝  ╚═╝╩ ╩╚═╝╚═╝╩ ╩╚═╝╩╚═

          1. Check Codes

          2. Clear All Codes

    """)
    option = input("    option: ")

    if option == '1':
        codes = read_codes()
        if not codes:
            print("The file is empty.")
            time.sleep(2)
            return
        for code in codes:
            proxy = None
            if use_proxies and proxies:
                proxy = aiohttp.ProxyConnector.from_url(proxies.pop(0).strip())
            async with aiohttp.ClientSession() as session:
                result = await check_gift_code(code.strip(), session, proxy)
            print(f"Code: {code.strip()} - {result}")
    elif option == '2':
        write_codes([])
        print("All codes cleared.")
    else:
        print("Invalid option.")

if __name__ == "__main__":
    asyncio.run(main())
