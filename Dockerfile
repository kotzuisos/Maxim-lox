FROM python:3.11-slim

WORKDIR /app

# Устанавливаем curl, git и скачиваем sshx
RUN apt-get update && apt-get install -y curl git && \
    curl -sSf https://sshx.io/get | sh && \
    rm -rf /var/lib/apt/lists/*

# Копируем зависимости и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь код бота
COPY . .

# Запускаем sshx. Ссылка для входа в терминал будет в логах контейнера.
CMD ["./sshx"]
