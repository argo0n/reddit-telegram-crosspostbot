# reddit-telegram-crosspostbot

This script is written for crossposting posts from a chosen subreddit in Reddit to a chosen Telegram channel.

## Getting Started

### Dependencies

* Libraries needed are listed in [requirements.txt](requirements.txt).
* ex. Windows 10

### Installing

1. run `git clone https://github.com/argo0n/reddit-telegram-crosspostbot/` in a directory where you want the script's files to be shown.
2. `cd reddit-telegram-crosspostbot` and run `pip install -r requirements.txt` to install required dependencies and libraries. 
3. Head over to [Preferences > Apps](https://old.reddit.com/prefs/apps/) on Reddit and select "Create another app". You can input any name and description. 
   - Select "Script" and enter `http://localhost:8080` as the redirect URI, then select "Create App".
   - Keep the Client ID and secret safely. You'll need it later when setting up the script.![alt text](https://cdn.nogra.me/screenshots/brave_bXWsXyq7Qf.png)
4. Head over to Telegram and talk to [@BotFather](https://t.me/BotFather). Send a `/newbot`. 
    - Follow the instructions sent by the bot. Soon, you'll have a token for the bot as shown here: ![alt text](https://cdn.nogra.me/screenshots/brave_cw3NeDmnZZ.png)
5. Create a file called `credentials.env`.
    - Inside the file, enter these: 
    ```
    telegram=Your telegram bot's Token
    clientID=Your Reddit application's Client ID
    clientSecret=Your Reddit application's Client Secret
    subreddit=the name of the subreddit you want the bot to listen to (excluding the /r/ prefix)
    reddituser=Your reddit username
    redditpass=Your reddit password
    redditapp=Your reddit app name
    telegramChannel=Your telegram channel ID, get it from the web version of Telegram.
    ```
   - These credentials are needed for the script to be allowed to connect to the Telegram and Reddit API. 
   - The reddit username and password should belong to the account which you used to create the Reddit applilcation.
   - For the channel ID, an example is shown in this screenshot. However, as channel IDs should be 13 digits long, you will need to add a `100`right after the `-`. For example, for the channel below, the resulting ID should be `-1001216422279`. ![](https://cdn.nogra.me/screenshots/brave_cY0RAraqUs.png)
## Authors

Contributors names and contact info

ex. argo0n

## Version History

* 0.1
    * Initial Release

## License

This project is licensed under the <b>MIT License</b> - see the [LICENSE](license) file for details.
## Acknowledgments


* [praw](https://github.com/praw-dev/praw) - The main library used for communicating with Reddit
* [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) - The main library used for communicating with Telegram
* [cyberShaw](https://github.com/cyberShaw/)