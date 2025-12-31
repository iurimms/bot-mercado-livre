import requests
from bs4 import BeautifulSoup
import time
import os
from dotenv import load_dotenv

load_dotenv()

# --- CONFIGURAÇÕES ---
# Colar o link do produto que você quiser aqui embaixo
URL_PRODUTO = "https://produto.mercadolivre.com.br/MLB-3973778143-gift-card-uber-presente-carto-r-20-reais-digital-_JM" 

# Aqui a mágica acontece: ele busca a senha no "sistema" (que veio do .env)
TELEGRAM_TOKEN = os.getenv("TOKEN_DO_TELEGRAM")
TELEGRAM_CHAT_ID = os.getenv("CHAT_ID_DO_TELEGRAM")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# --- VERIFICAÇÃO DE SEGURANÇA ---
# Se o arquivo .env estiver vazio ou com nomes errados, o bot avisa e para.
if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
    print("ERRO CRÍTICO: Não encontrei o TOKEN ou ID.")
    print("Verifique se o arquivo .env está salvo na mesma pasta e com os nomes certos.")
    exit()

def enviar_telegram(mensagem):
    for tentativa in range(1, 4):
        try:
            url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
            dados = {"chat_id": TELEGRAM_CHAT_ID, "text": mensagem}
            requests.post(url, data=dados, timeout=10)
            print("Mensagem enviada para o Telegram!")
            return 
        except Exception as e:
            print(f"Erro ao enviar (Tentativa {tentativa}/3): {e}")
            time.sleep(5)
            
    print("ERRO FINAL: Não consegui enviar a mensagem.")

def checar_produto():
    print(f"[{time.strftime('%H:%M:%S')}] Verificando...")
    try:
        requisicao = requests.get(URL_PRODUTO, headers=HEADERS)
        
        if requisicao.status_code == 200:
            soup = BeautifulSoup(requisicao.content, 'html.parser')
            texto_site = soup.get_text().lower()

            if "anúncio pausado" in texto_site:
                print("Status: PAUSADO.")
                return False
            elif "estoque indisponível" in texto_site:
                print("Status: SEM ESTOQUE.")
                return False
            elif "republique o anúncio" in texto_site:
                print("Status: ANÚNCIO FINALIZADO.")
                return False
            else:
                print("Status: DISPONÍVEL!!!")
                enviar_telegram(f"🚨 CORREEEEE!🚨\n O produto voltou!\n\nLink: {URL_PRODUTO}")
                return True
        else:
            print(f"Erro ao acessar site: {requisicao.status_code}")
            return False

    except Exception as erro:
        print("Erro no script:", erro)
        return False

# --- LOOP INFINITO ---
print("Bot iniciado com SEGURANÇA (.env) ativada!")
enviar_telegram("Bot reiniciado.")

while True:
    if checar_produto():
        print("Produto encontrado! Encerrando.")
        break
    time.sleep(300)