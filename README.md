# An Rclone Telegram bot to transfer to and from many clouds

## Features:

- Mirror from Telegram to cloud.
- Leech files and folders from cloud to Telegram.
- Copy from one cloud to another.
- Button panels to interact with clouds.
- Renaming of Telegram files.
- Progress bar when downloading and uploading.

## Commands for bot(set through @BotFather)

```
mirror - mirror to selected cloud 
leech - leech from cloud to telegram
copy - copy from cloud to cloud
myfiles - file manager
config - select cloud and folder for mirror
logs - get logs from server
server - get server info
speedtest - test speed of server
cleardata- clear downloads
restart - restart bot
```

## Deploying on Heroku
<p><a href="https://github.com/1141879423/Rclone-Tg-Bot/tree/heroku"> <img src="https://img.shields.io/badge/Deploy%20Guide-blueviolet?style=for-the-badge&logo=heroku" width="170""/></a></p>


## Deploy on VPS: 

1. **Installing requirements**
 
 - Update & Install requirements:
 
       sudo apt-get update 
       sudo apt-get upgrade
       apt-get install git wget curl python3 python3-pip python3-venv locales ffmpeg p7zip-full 
 
 - Install rclone:
 
       curl https://rclone.org/install.sh | bash

 - Clone repo:

        git clone https://github.com/Sam-Max/Rclone-Tg-Bot rclonetgbot/ && cd rclonetgbot
 
 - Pip install requirements:
 
        pip3 install -r requirements.txt 

2. **Set up config file**

        cp sample_config.env config.env 

- Fill up variables:

   - Mandatory variables:
        - `API_ID`: get this from https://my.telegram.org. Don't put this in quotes.
        - `API_HASH`: get this from https://my.telegram.org
        - `OWNER_ID`: your Telegram User ID (not username) of the owner of the bot.
        - `ALLOWED_USERS`: list of IDs of allowed users who can use this bot separated by spaces
        - `ALLOWED_CHATS`: list of IDs of allowed chats who can use this bot separated by spaces
        - `BOT_TOKEN`: The Telegram Bot Token (get from @BotFather) 
        - `RCLONE_CONFIG`: content of the rclone.conf file generated with rclone command-line program.

   - Non mandatory variables:
        - `UPSTREAM_REPO`: if your repo is private add your github repo link with format: `https://username:{githubtoken}@github.com/{username}/{reponame}`, so you can update your app from private repository on each restart. Get token from [Github settings](https://github.com/settings/tokens)
        - `UPSTREAM_BRANCH`: Upstream branch for update. 
        - `TG_SPLIT_SIZE`: Telegram upload limit in bytes (max `2097151000` which is ~2GB), to automatically slice the file bigger that this size into small parts to upload to Telegram.
        - `EDIT_SLEEP_SECS`: Seconds for update the progress message regulary. Default to 10. 

3. **Deploying on VPS**

       chmod 777 start.sh 
       ./start.sh


## Repositories used to develop this bot:

1- [TorToolkit-Telegram](https://github.com/yash-dk/TorToolkit-Telegram) 

2- [Conversation-Pyrogram](https://github.com/Ripeey/Conversation-Pyrogram/archive/refs/heads/main.zip)

3- [Rclone](https://github.com/rclone/rclone)

4- [Telethon]() and [Pyrogram]()



