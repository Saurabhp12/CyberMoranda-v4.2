import requests
from config.telegram import send_alert

def run():
    ip = input("Enter victim's IP: ")
    try:
        data = requests.get(f"http://ip-api.com/json/{ip}").json()
        print(data)
        send_alert(f"[IP LOGGED] {data}")
    except Exception as e:
        print("Error:", e)
