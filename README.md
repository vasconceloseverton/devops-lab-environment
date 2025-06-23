
# 🚀 Infra Simulada DevOps

Bem-vindo ao **Infra Simulada DevOps**, um projeto desenvolvido para simular uma infraestrutura moderna utilizando práticas de **DevOps**, **CI/CD**, **Docker**, **Monitoramento** e **Automação**.

Este projeto é ideal para demonstrar competências na área de DevOps, sendo voltado tanto para aprendizado quanto para apresentação em portfólios profissionais.

---

## 📚 Índice

- [📦 Sobre o Projeto](#-sobre-o-projeto)
- [🛠️ Tecnologias Utilizadas](#️-tecnologias-utilizadas)
- [⚙️ Arquitetura do Projeto](#️-arquitetura-do-projeto)
- [🚀 Funcionalidades](#-funcionalidades)
- [🐳 Docker e Deploy Local](#-docker-e-deploy-local)
- [☁️ Deploy na Nuvem](#️-deploy-na-nuvem)
- [🔧 CI/CD com GitHub Actions](#-cicd-com-github-actions)
- [📊 Monitoramento com Telegram](#-monitoramento-com-telegram)
- [📁 Estrutura de Pastas](#-estrutura-de-pastas)
- [🤝 Contribuição](#-contribuição)
- [📄 Licença](#-licença)

---

## 📦 Sobre o Projeto

O projeto é composto por dois serviços principais:

1. **Aplicação Web Flask:**  
   - Uma aplicação simples com rotas de status, informações e métricas.  
   - Simula um serviço em produção.

2. **Healthcheck Monitor:**  
   - Um serviço separado que realiza verificações periódicas na aplicação Flask.  
   - Envia alertas para o Telegram caso detecte quedas ou falhas no serviço.

---

## 🛠️ Tecnologias Utilizadas

- 🐍 **Python 3.11**
- 🌐 **Flask 3.0.0**
- 🐳 **Docker**
- ☁️ **Render (Cloud Hosting)**
- 🔧 **GitHub Actions (CI/CD)**
- 📲 **Telegram Bot API (Monitoramento)**
- 🔍 **Requests (Healthcheck)**

---

## ⚙️ Arquitetura do Projeto

```plaintext
+------------------------+            +-----------------------------+
|   🧠 Usuário/Cliente    | <------->  | 🌐 Flask App (Web Service)   |
+------------------------+            +-----------------------------+
                                              ▲
                                              │ (Verificação constante)
+--------------------------------------------------------------+
| 🚨 Healthcheck Monitor (Envio de Alertas p/ Telegram)        |
+--------------------------------------------------------------+
```

---

## 🚀 Funcionalidades

### 🌐 **Flask App**
- `/` — Página inicial
- `/about` — Página sobre o projeto
- `/health` — Healthcheck (para CI/CD e Monitoramento)
- `/info` — Informações da aplicação
- `/metrics` — Métricas simuladas

### 🚨 **Healthcheck Monitor**
- Verifica periodicamente se a aplicação está no ar.
- Notifica automaticamente no **Telegram** em caso de falha.
- Pode rodar localmente, em container ou na nuvem.

---

## 🐳 Docker e Deploy Local

### 🔧 **Build e execução do Flask App:**

```bash
docker build -t infra-simulada-flask .
docker run -d -p 5000:5000 infra-simulada-flask
```

Acesse em:  
👉 http://localhost:5000

---

### 🔧 **Build e execução do Healthcheck Monitor:**

```bash
cd healthcheck
docker build -t infra-healthcheck .
docker run -e URL_TO_CHECK="https://seuapp.onrender.com/health"            -e TELEGRAM_TOKEN="seu_token"            -e TELEGRAM_CHAT_ID="seu_chat_id"            -e CHECK_INTERVAL=60            infra-healthcheck
```

---

## ☁️ Deploy na Nuvem

- ✅ **Render.com** (utilizando Docker)
- ✅ **Railway.app**
- ✅ **Fly.io**
- ✅ Pode ser adaptado para AWS, Azure, Google Cloud.

---

## 🔧 CI/CD com GitHub Actions

O pipeline realiza:  
- 🚀 Deploy automático para o Render quando há push na branch `main`.  
- ✅ Deploy tanto do Flask App quanto do Healthcheck Monitor.

### 🔐 Secrets no GitHub:

| Nome                         | Descrição                              |
|------------------------------|-----------------------------------------|
| `RENDER_API_KEY`             | API Key do Render                      |
| `RENDER_SERVICE_ID_FLASK`    | Service ID do App Flask                |
| `RENDER_SERVICE_ID_HEALTHCHECK` | Service ID do Healthcheck Monitor    |

### 📜 Workflow:

```yaml
.github/workflows/deploy.yml
```

---

## 📊 Monitoramento com Telegram

- ✅ Crie um bot com [@BotFather](https://t.me/botfather).
- ✅ Obtenha seu Chat ID usando [@userinfobot](https://t.me/userinfobot).
- ✅ Configure as variáveis de ambiente no serviço Healthcheck:
  - `TELEGRAM_TOKEN`
  - `TELEGRAM_CHAT_ID`
  - `URL_TO_CHECK`
  - `CHECK_INTERVAL` (em segundos)

---

## 📁 Estrutura de Pastas

```plaintext
infra-simulada-devops/
├── app/               # Código da aplicação Flask
│   ├── __init__.py
│   ├── routes.py
│   └── templates/
├── healthcheck/       # Script de monitoramento com alertas no Telegram
│   ├── healthcheck.py
│   ├── requirements.txt
│   └── Dockerfile
├── run.py             # Start da aplicação Flask
├── Dockerfile         # Dockerfile do Flask
├── requirements.txt   # Dependências do Flask
├── .github/workflows/ # Pipeline CI/CD
│   └── deploy.yml
├── README.md          # Este arquivo
```

---

## 🤝 Contribuição

Contribuições são bem-vindas!  

1. Fork este repositório.  
2. Crie uma branch (`git checkout -b feature/NovaFeature`).  
3. Commit suas alterações (`git commit -m 'Adicionando nova feature'`).  
4. Push para a branch (`git push origin feature/NovaFeature`).  
5. Abra um Pull Request.

---

## 📄 Licença

Distribuído sob a licença MIT. Consulte `LICENSE` para mais informações.

---

## 💼 Autor

Desenvolvido por Everton Vasconcelos 🚀  

---
