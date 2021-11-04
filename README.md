# How to 
1. Line notifyを使う
2. Line Developersを使う
今回は実装が軽い1の方法を載せておきます。

# Line notify
## トークンの発行
1. Line notify(https://notify-bot.line.me/ja/)にアクセスしてログインする。
2. マイページからトークンのの発行をするを押す。
![トークンの発行](https://i.imgur.com/puH5iRw.png)
3. 送信先のグループや個人を選択する。
![対象の選択](https://i.imgur.com/ZplYSq4.png)
4. 発行されたトークンをコピーする。
![コピー](https://i.imgur.com/6FNujRc.png)

# プログラムを書く
notify.pyをみてください。