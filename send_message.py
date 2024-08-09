import requests

def send_message():
    url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=cb6c67a2-8e6e-46cd-95fb-12014d909d5b'
    headers = {'Content-Type': 'application/json'}
    data = {
        "msgtype": "text",
        "text": {
            "content": "dingyuanying2004"
        }
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print(f"Failed to send message. Status code: {response.status_code}, Response: {response.text}")

if __name__ == "__main__":
    send_message()
