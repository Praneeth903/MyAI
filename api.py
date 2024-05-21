import json
import requests
import openai 
headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNjA4ZDNkZWMtNTkzNC00Y2I3LWFmMGUtMmUwNmEyODVmODhjIiwidHlwZSI6ImFwaV90b2tlbiJ9.g_U0ET9GqEREJJ7GyvF38qgYV0R9Ijt7qs0tzvevdFU"}

url = "https://api.edenai.run/v2/text/chat"
payload = {
    "providers": "openai",
    "text": "Hello i need your help ! ",
    "chatbot_global_action": "Act as an assistant",
    "previous_history": [],
    "temperature": 0.0,
    "max_tokens": 150,
    "fallback_providers": "abcd"
}




def take(query):
    payload["text"]=query
    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)
    speak(result['openai']['generated_text'])