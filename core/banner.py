from colorama import init, Fore
import pyfiglet

init(autoreset=True)

def display_banner():
    banner = pyfiglet.figlet_format("CyberMoranda v4.2")
    print(Fore.CYAN + banner)
    print(Fore.GREEN + "[+] Ethical Hacking Toolkit for Termux")
    print(Fore.YELLOW + "[+] Coded by @CyberMoranda\n")
