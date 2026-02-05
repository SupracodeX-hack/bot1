"""
Fichier de configuration Globale du bot et API
Createur: Spectre
"""
import os
from dotenv import load_dotenv

# chargement des variables d'environnement
load_dotenv()

# TELEGRAM TOKEN
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "8432705726:AAE-vxL4rqYzf5lQnmLg7zrJNeJB15cMlhA")

# GEMINI API
AI_API_KEY = os.getenv("AI_API_KEY", "AIzaSyANlEkH3uVt3ZhE2JUcm7t1S3L5RGRttH4")


# CLES PRESENTES?
if not TELEGRAM_TOKEN or not AI_API_KEY:
    raise ValueError("ERREUR : Les variables d'environnement sont manquantes !")
