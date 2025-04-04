import requests
import json
import random
import time
import sys
Atempts = 0
loop = True
while loop == True:
    IP1 = random.randint(0, 255)
    IP2 = random.randint(0, 255)
    IP3 = random.randint(0, 255)
    IP4 = random.randint(0, 255)
    IP = f"{str(IP1)}.{str(IP2)}.{str(IP3)}.{str(IP4)}"
    url = f"http://ip-api.com/json/{IP}"
    r = requests.get(url)
    data = r.json()
    sys.stdout.write(f'\r [{str(Atempts)}] loading: |')
    time.sleep(0.5)
    sys.stdout.write(f'\r [{str(Atempts)}] loading: /')
    time.sleep(0.5)
    sys.stdout.write(f'\r [{str(Atempts)}] loading: -')
    time.sleep(0.5)
    sys.stdout.write(f'\r [{str(Atempts)}] loading: \\')
    time.sleep(0.5)

    if "zip" in data:
        print("")
        print("Results:")
        print(f'City: {data["city"]}')
        print(f'Country: {data["country"]}')
        print(IP)
        loop = False
        if data["country"] == "China":
            print("Common")
        if data["country"] == "United States":
            print("Common")
        if data["country"] == "Japan":
            print("Uncommon")
        if data["country"] == "The Netherlands":
            print("Rare")
        if data["country"] == "Kazakhstan":
            print("Uncommon")
        if data["country"] == "Africa":
            print("Mythic")
        if data["country"] == "South Korea":
            print("Uncommon")
        if data["country"] == "Sweden":
            print("Rare")
        if data["country"] == "Brazil":
            print("Ultra Rare")
        if data["country"] == "Indonesia":
            print("Ultra Rare")
        if data["country"] == "France":
            print("Uncommon")
        if data["country"] == "Algeria":
            print("Common")
        if data["country"] == "Russia":
            print("Uncommon")
        if data["country"] == "Indonesia":
            print("Ultra Rare")
        if data["country"] == "Colombia":
            print("Legendary")
        if data["country"] == "Italy":
            print("Rare")
        if data["country"] == "Greece":
            print("Ultra Rare")
        if data["country"] == "Philippines":
            print("Uncommon")
        if data["country"] == "New Zealand":
            print("Legendary")
        if data["country"] == "Germany":
            print("Uncommon")
        if data["country"] == "Hungary":
            print("Ultra Rare")
        if data["country"] == "Switzerland":
            print("Rare")
        if data["country"] == "Canada":
            print("Rare")
        if data["country"] == "South Africa":
            print("Legendary")            
        if data["country"] == "Uganda":
            print("Ultra Rare")
        if data["country"] == "Finland":
            print("Rare")
        if data["country"] == "Spain":
            print("Rare")
        if data["country"] == "Trinidad and Tobago":
            print("Ultra Rare")  
        if data["country"] == "United Kingdom":
            print("Uncommon")
        if data["country"] == "India":
            print("Ultra Rare")
        if data["country"] == "Poland":
            print("Rare")
        if data["country"] == "Ireland":
            print("Uncommon")  
        if data["country"] == "Australia":
            print("Rare") 
        if data["country"] == "Hong Kong":
            print("Uncommon")
        if data["country"] == "Denmark":
            print("Rare") 
        if data["country"] == "Norway":
            print("Legendary")
        if data["country"] == "Hawaii":
            print("Mythic") 
        if data["country"] == "Taiwan":
            print("Ultra Rare")  
        if data["country"] == "Austria":
            print("Ultra Rare")
        if data["country"] == "Vietnam":
            print("Rare") 
        if data["country"] == "Lithuania":
            print("Rare")
        if data["country"] == "North Korea":
            print("Divine")
        if data["country"] == "Oman":
            print("Rare")
        if data["country"] == "Morocco":
            print("Legendary")
        if data["country"] == "Argentina":
            print("Rare")
        if data["country"] == "Iran":
            print("Uncommon")
        if data["country"] == "Togo":
            print("Ultra Rare")
        if data["country"] == "Venezuela":
            print("Ultra Rare")
        if data["country"] == "Mexico":
            print("Mythic")
        if data["country"] == "Egypt":
            print("Legendary")            
    else:
        Atempts = Atempts + 1
