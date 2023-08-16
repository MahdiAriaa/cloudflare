import requests
from time import sleep
import pyfiglet
from colorama import Fore
import os

def update_cloudflare():
    API_KEY = "DZVImvsEMDdx1IPcN48F0OGq3-c3TpbzpANdWH0g"
    EMAIL = "mahdiaria138@gmail.com"
    ZONE_ID = "c15081d54dcca11db92654694a527c9f"
    
    subdomains = input("Enter subdomains: ").split()

    new_ip = "193.187.175.91"

    for subdomain in subdomains:
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
        url = f"https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records?type=A&name={subdomain}"

        response = requests.get(url, headers=headers)
        data = response.json()

        if "result" in data and data["result"]:
            record_id = data["result"][0]["id"]
            update_url = f"https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records/{record_id}"

            update_data = {
                "type": "A",
                "name": subdomain,
                "content": new_ip
            }
            update_response = requests.put(
                update_url, headers=headers, json=update_data)

            if update_response.status_code == 200:
                print(f"DNS record updated successfully for {subdomain}.")
            else:
                print(f"Failed to update DNS record for {subdomain}.")
        else:
            print(f"No DNS record found for {subdomain}.")



update = input("Do you want to update the IP of the subdomain in Cloudflare? (yes/no)").lower()
if update == "yes" or update == "y":
    print(Fore.YELLOW + "Please wait a moment..." + Fore.RESET)
    sleep(5)
    update_cloudflare()
elif "no":
    print("Goodbye!!!")
