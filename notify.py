import requests

def main():
    #好きなメッセージを書く
    send_line_notify('message')

def send_line_notify(notification_message):
    #さっき取得したトークンを入力する
    line_notify_token = 'Your Token'
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {line_notify_token}'}
    data = {'message': f'{notification_message}'}
    #送信
    requests.post(line_notify_api, headers = headers, data = data)

if __name__ == "__main__":
    main()