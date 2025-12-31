# Bot de Monitoramento - Mercado Livre

Este projeto é um script de automação em Python que vigia a página de um produto no Mercado Livre e notifica o usuário via Telegram assim que o item volta a ficar disponível (estoque reposto ou pausa removida).

## Funcionalidades
- **Monitoramento contínuo:** Verifica a página a cada 5 minutos.
- **Notificação em Tempo Real:** Envia alerta no celular via Bot do Telegram.
- **Segurança:** Utiliza variáveis de ambiente (`.env`) para proteger Tokens e IDs.
- **Anti-Bloqueio:** Simula um navegador real (User-Agent) para evitar bloqueios simples.

## Tecnologias Utilizadas
- Python 3
- Requests (Para acessar o site)
- BeautifulSoup4 (Para ler o HTML)
- Python-Dotenv (Para segurança das chaves)

## Como usar

### 1. Instalação
Clone o repositório e instale as dependências:
```bash
pip install -r requirements.txt
``` 

### 2. Configuração
Crie um arquivo .env na raiz do projeto e adicione suas credenciais:
```ini
TOKEN_DO_TELEGRAM=seu_token_aqui
CHAT_ID_DO_TELEGRAM=seu_id_aqui
```

### 3. Rodando
No arquivo monitor.py, adicione o link do produto desejado na variável URL_PRODUTO e execute:
```bash
python monitor.py

Aviso: Este projeto é para fins educacionais. O uso excessivo de requisições (web scraping) pode bloquear seu IP temporariamente no site alvo. 