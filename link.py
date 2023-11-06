import requests

# Remplacez 'YOUR_WEBHOOK_URL' par l'URL du webhook Discord que vous avez créé
webhook_url = 'https://discord.com/api/webhooks/1167084893788975164/vgdxgapnrjl6NcEaJAOQW0Oi8iF3BXQLVlPNZUfIdr9o-VIlMS7bzZV1u2JiWqRgNI8S'

# Message à envoyer
message = 'Hello, Discord!'

# Créez un dictionnaire contenant le message et d'autres options
data = {
    'content': message
}

# Envoyez le message au webhook
response = requests.post(webhook_url, json=data)

# Vérifiez la réponse
if response.status_code == 204:
    print('Message envoyé avec succès')
else:
    print('Erreur lors de l\'envoi du message :', response.status_code, response.text)