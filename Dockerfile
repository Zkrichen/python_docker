# Utiliser l'image Python officielle en tant que base
FROM python:3.9-slim



# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers requis dans le conteneur
COPY requirements.txt .

# Installer les dépendances Python
RUN apt-get update && apt-get install -y iputils-ping
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste des fichiers dans le conteneur
COPY . .

# Commande par défaut pour exécuter l'application (modifiable selon votre cas)
CMD ["python", "app.py"]
