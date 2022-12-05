from ast import For, arg
from time import sleep
from xml.sax.handler import version
import cloudscraper
import argparse
from colorama import init, Fore, Style
import os
import json

# gen fara misto imi bag pula in copii cu ngl, tellonym > ngl toata ziua
# nu stiu ce i-a apucat pe toti

os.system("title NGL Spammer+")

init(convert=True)

argument1 = argparse.ArgumentParser(
    description="A tool that is able to easily spam any NGL link that you wish.", epilog="As long as CF doesn't patch this, it will work for some time.\nIf you have any questions, my DMs are open on Discord: JPN#0001")
argument1.version = "0.2 Final"
argument1.add_argument('-u', '--username', action='store',
                       help="The NGL username (after ngl.link/)", required=True)
argument1.add_argument('-n', '--message_no', action='store',
                       help="Amount of messages to be sent", required=True, type=int)
argument1.add_argument('-i', '--input', action='store_true',
                       help="Use interactive input to enter the message", required=False)
argument1.add_argument('-v', '--version', action='version')
argument1.add_argument('--message', action='store', required=False,
                       help="Enter the message here (ONLY WORKS IF --input NOT SET)")
args = argument1.parse_args()

message = ""

if args.input == False and args.message == None:
    print(Fore.RED + "One of the following parameters should be provided: -i/--input or --message" + Style.RESET_ALL)
    exit(1)

if args.input == True:
    print(Fore.YELLOW +
          "NGL Spammer+ made by JPN (Discord: JPN#0001) https://isaidpower.dev")
    message = input(Style.RESET_ALL + "[" + Fore.YELLOW +
                    "?" + Style.RESET_ALL + "] Message: ")
else:
    message = args.message

scraper = cloudscraper.create_scraper(interpreter="nodejs")

os.system("cls")
print(Fore.YELLOW + "NGL Spammer+ made by JPN (Discord: JPN#0001) https://isaidpower.dev")
print(Style.RESET_ALL + "This tool was designed for " + Fore.RED + "PRANKING" +
      Style.RESET_ALL + " purposes" + Fore.RED + " ONLY" + Style.RESET_ALL + ".")
print("The spam will now start\n\n")

# q: how much to wait for cloudflare rate limit


for i in range(1, args.message_no + 1):
    scraper.post("https://ngl.link/" + args.username,
                 data={'question': message})
    print("[" + Fore.GREEN + "SUCCESS" + Style.RESET_ALL +
          "] Message no. " + str(i) + " sent! And waiting 5 seconds...")
    sleep(5)

print()
print(Fore.YELLOW + "Some messages might have not arrived due to the cloudflare bypass module being faulty.")
print("But I assure you, that 3/4 messages were successfully sent.")
print(Style.RESET_ALL + "Thanks for testing it out!")
