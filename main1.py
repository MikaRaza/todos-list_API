from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from routers.router import router

app = FastAPI(title="TODO-Lists",
    description="""
Bienvenue dans l'API de gestion de liste de tâches ! Cette API vous permet de créer, lire, mettre à jour et supprimer des tâches à faire, vous permettant ainsi d'organiser efficacement votre emploi du temps et de rester productif.

📝 Avec notre API de liste de tâches, vous pouvez facilement ajouter de nouvelles tâches à votre liste, spécifier leur titre et leur état (terminée ou non terminée), mettre à jour les détails des tâches existantes et supprimer les tâches que vous avez accomplies ou que vous ne souhaitez plus voir dans votre liste.

🚀 Grâce à cette API, vous pouvez gérer votre liste de tâches de manière efficace et intuitive, que ce soit pour vos tâches personnelles, professionnelles ou scolaires. Elle vous permet de rester organisé, de prioriser vos tâches et de suivre vos progrès dans l'accomplissement de vos objectifs.

🔑 Pour utiliser cette API, vous devez d'abord vous authentifier en tant qu'utilisateur en fournissant vos informations d'identification. Une fois connecté, vous pouvez accéder à toutes les fonctionnalités de l'API et gérer votre liste de tâches en toute sécurité.

📌 Explorez nos points de terminaison et découvrez comment notre API de liste de tâches peut vous aider à améliorer votre gestion du temps, à rester concentré sur vos objectifs et à mener une vie plus organisée et productive !
""",
    version="1.0.0")

app.include_router(router)
