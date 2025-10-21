# Test Hugging Face Token
import os
from dotenv import load_dotenv

# Carica variabili da .env
load_dotenv()

# Leggi token
hf_token = os.getenv("HUGGINGFACE_TOKEN")

# Verifica
if hf_token:
    print("✅ Hugging Face Token caricato!")
    print(f"Token (primi 10 caratteri): {hf_token[:10]}...")

    # Test API
    from huggingface_hub import whoami

    try:
        info = whoami(token=hf_token)
        print(f"\n🎉 Autenticato come: {info['name']}")
        print(f"📧 Email: {info.get('email', 'N/A')}")
        print("\n✅ Hugging Face funziona perfettamente!")
    except Exception as e:
        print(f"❌ Errore: {e}")
else:
    print("❌ Token non trovato! Verifica file .env")
