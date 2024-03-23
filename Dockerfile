# Використовуємо офіційний образ Python з Docker Hub
FROM python:3.12

# Встановлюємо залежності за допомогою pipenv
RUN pip install pipenv

# Копіюємо файли програми в контейнер
COPY . /app

# Переходимо в робочу директорію /app
WORKDIR /app

# Встановлюємо залежності з Pipfile.lock
RUN pipenv install --deploy --ignore-pipfile

# Встановлюємо працюючу директорію
ENV PYTHONPATH=/app

# Команда для запуску вашого додатку
CMD ["python", "main.py"]