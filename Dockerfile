# Imagem base oficial do Python
FROM python:3.11-slim

# Diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos 
COPY . .

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta 5000
EXPOSE 5000

# Comando para iniciar a aplicação
CMD ["python", "run.py"]
