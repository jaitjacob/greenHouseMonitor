#!/usr/bin/env python3
import requests
import json
import os

ACCESS_TOKEN = "o.Uku0RMLmpUV18bnGkAgkpYQB2mGzyAko"

def send_notification_via_pushbullet(title, body):
    """ Sending notification via pushbullet.
        Args:
            title (str) : Title of text.
            body (str) : Body of text.
    """
    data = { "type": "note", "title": title, "body": body }

    response = requests.post("https://api.pushbullet.com/v2/pushes", data = json.dumps(data),
        headers = { "Authorization": "Bearer " + ACCESS_TOKEN, "Content-Type": "application/json" })

    if(response.status_code != 200):
        raise Exception()

    print("Notification sent.")

# Main function.
def main():
    ip_address = os.popen("hostname -I").read()
    send_notification_via_pushbullet(ip_address, "From Raspberry Pi")

# Execute.
if __name__ == "__main__":
    main()
