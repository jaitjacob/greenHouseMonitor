import requests,json,os,sqlite3

def send_notification_via_pushbullet(self, title, body):
        ACCESS_TOKEN = "o.Uku0RMLmpUV18bnGkAgkpYQB2mGzyAko"
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

send_notification_via_pushbullet("this title","ENDGAME is coming")