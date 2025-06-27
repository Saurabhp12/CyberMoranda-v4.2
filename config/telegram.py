import requests

BOT_TOKEN = "8007524819:AAHTa87YPcZd9qjadGMRHJTWDrRD-dipnO4"
CHAT_ID = "5999760280"

def send_alert(msg):
    url = f"https://api.telegram.org/bot{8007524819:AAHTa87YPcZd9qjadGMRHJTWDrRD-dipnO4}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": msg}
    requests.post(url, data=data)
