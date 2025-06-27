import os
import time
from config.telegram import send_alert

def run():
    print("[*] Starting Ngrok...")

    if not os.path.exists("ngrok"):
        print("[!] Ngrok binary not found in your folder.")
        print(">>> Download it from https://ngrok.com/download and place it here.")
        return

    port = input("Enter port to expose (default 8080): ") or "8080"
    os.system(f"./ngrok http {port} > /dev/null &")
    time.sleep(5)

    try:
        url = os.popen("curl -s http://127.0.0.1:4040/api/tunnels | grep -o 'https://[a-z0-9]*\\.ngrok.io' | head -n1").read().strip()
        if url:
            print(f"[+] Ngrok Public URL: {url}")
            send_alert(f"[NGROK LINK] {url}")
        else:
            print("[-] Failed to get Ngrok URL.")
    except Exception as e:
        print("Error:", e)
