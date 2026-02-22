import requests

def chat_avec_bot():
    print("--- Bienvenue sur mon Chatbot API (TP 5) ---")
    print("Tapez 'quitter' pour arrêter.\n")
    
    while True:
        message = input("Vous : ")
        if message.lower() == "quitter":
            break
            
        # Ici, on simule l'appel à une API de chat
        # Dans un vrai projet, on utiliserait une clé API OpenAI ou Gemini
        reponse = f"Echo du Bot : J'ai bien reçu votre message : '{message}'"
        
        print(f"Bot : {reponse}\n")

if __name__ == "__main__":
    chat_avec_bot()
