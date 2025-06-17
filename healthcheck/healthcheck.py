import requests
import time

# ✅ Configurações
URL_TO_CHECK = "https://infra-simulada-devops.onrender.com/health"
CHECK_INTERVAL = 60  # segundos

TELEGRAM_TOKEN = "SEU_TOKEN_AQUI"
TELEGRAM_CHAT_ID = "SEU_CHAT_ID_AQUI"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }
    try:
        response = requests.post(url, data=payload)
        if response.status_code != 200:
            print(f"Erro ao enviar mensagem: {response.text}")
    except Exception as e:
        print(f"Erro na conexão com Telegram: {e}")

def check_health():
    try:
        response = requests.get(URL_TO_CHECK, timeout=5)
        if response.status_code == 200:
            print(f"✅ {URL_TO_CHECK} está no ar.")
        else:
            print(f"❌ {URL_TO_CHECK} retornou status {response.status_code}")
            send_telegram_message(f"🚨 Healthcheck ERROR: {URL_TO_CHECK} retornou status {response.status_code}")
    except Exception as e:
        print(f"❌ Erro na requisição: {e}")
        send_telegram_message(f"🚨 Healthcheck ERROR: {URL_TO_CHECK}\nErro: {e}")

if __name__ == "__main__":
    while True:
        check_health()
        time.sleep(CHECK_INTERVAL)
