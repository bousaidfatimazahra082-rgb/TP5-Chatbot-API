import requests

# C'est une API publique gratuite pour les tests (Hugging Face)
API_URL = "https://api-inference.huggingface.co/models/gpt2"
# Note : Normalement on utilise un "Token", mais pour un TP de base, 
# certains modèles publics répondent directement.

def demander_a_l_api(message):
    payload = {"inputs": message}
    try:
        response = requests.post(API_URL, json=payload)
        # On récupère le texte généré par l'IA
        return response.json()[0]['generated_text']
    except:
        return "Désolé, l'API est occupée ou le message est mal formé."

def main():
    print("--- Mon Chatbot Connecté à une API ---")
    while True:
        user_input = input("Vous : ")
        if user_input.lower() in ["quitter", "stop"]:
            break
            
        reponse = demander_a_l_api(user_input)
        print(f"IA : {reponse}\n")

if __name__ == "__main__":
    main()
