# test_veo.py
"""
Script de test pour générer une vidéo avec OpenAI VEO
⚠️ Ne met jamais ta clé API en clair dans le code public.
"""

import os
from openai import OpenAI

# Récupération sécurisée de la clé API depuis une variable d'environnement
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError(
        "❌ Erreur : la clé API n'est pas définie.\n"
        "Définis-la avant d'exécuter le script :\n"
        "   export OPENAI_API_KEY='ta_clé_secrète'   (Linux/Mac)\n"
        "   setx OPENAI_API_KEY 'ta_clé_secrète'    (Windows)\n"
        "Ou dans Colab :\n"
        "   import os\n   os.environ['OPENAI_API_KEY'] = 'ta_clé_secrète'"
    )

# Initialisation du client
client = OpenAI(api_key=api_key)

# 🔹 Exemple de génération de vidéo
def generate_video(prompt, output_file="output.mp4"):
    print(f"🎬 Génération en cours pour : {prompt}")

    # Appel à l'API OpenAI (modèle VEO)
    result = client.videos.generate(
        model="veo-1",  # modèle vidéo
        prompt=prompt,
        size="1024x1024",  # résolution
        duration=5        # durée en secondes
    )

    # Récupération du flux vidéo
    video_url = result.data[0].url

    print(f"✅ Vidéo générée : {video_url}")
    print(f"👉 Télécharge-la et enregistre-la en tant que {output_file}")


if __name__ == "__main__":
    # Exemple de test
    generate_video("Un chat qui joue au piano dans un style cartoon")
