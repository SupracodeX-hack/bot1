"""
Fichier de configuration Globale du bot et API
Createur: Spectre
"""
import os
from dotenv import load_dotenv

# chargement des variables d'environnement
load_dotenv()

# TELEGRAM TOKEN
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# GEMINI API
AI_API_KEY = os.getenv("AI_API_KEY")

# CLES PRESENTES?
if not TELEGRAM_TOKEN or not AI_API_KEY:
    raise ValueError("ERREUR : Les variables d'environnement sont manquantes !")
