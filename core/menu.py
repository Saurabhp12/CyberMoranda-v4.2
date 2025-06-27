from modules import ip_logger, port_scanner, phishing, ngrok_launcher
def main_menu():
    while True:
        print("\n[1] IP Logger\n[2] Port Scanner\n[3] Ngrok Launcher\n[4] Phishing\n[0] Exit")
        choice = input("Select Option: ")

        if choice == "1":
            ip_logger.run()
        elif choice == "2":
            port_scanner.run()
        elif choice == "3":
            ngrok_launcher.run()
        elif choice == "4":
            phishing.run()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")
