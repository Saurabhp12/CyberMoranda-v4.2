# ⚔️ CYBER MORANDA v4.2 ⚔️

**Advanced Termux-based Ethical Hacking Toolkit**  
Coded by [@CyberMoranda](https://github.com/Saurabhp12)

## 🚀 Features
- IP Logger with Telegram alerts
- Port Scanner (Fast & Customizable)
- Phishing Auto-host (PHP + Ngrok)
- Telegram bot integration
- Ngrok Launcher with URL fetch
- Colorful & modular CLI

## 📦 Requirements
- Termux (Android)
- Python 3.x
- PHP
- Ngrok
- Git

## 🔧 Installation
```bash
pkg install git python php curl wget -y
git clone https://github.com/Saurabhp12/CyberMoranda-v4.2.git
cd CyberMoranda-v4.2
chmod +x ngrok
python main.py

Ngrok setup 
./ngrok config add-authtoken YOUR_TOKEN_HERE
./ngrok http 8080