from __future__ import unicode_literals
from utils.time import humanize_timedelta
import telegram
import praw
import time
import logging
import os
import sys
import logging
from logging import log
from dotenv import load_dotenv
from time import sleep
from datetime import datetime
import html
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

load_dotenv('credentials.env')

"""
Creating Logging system
"""

log = logging.getLogger('doggo')
log.setLevel(logging.DEBUG)

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
log.addHandler(ch)

"""
Defining required variables
"""

redditapp = os.getenv('redditapp')
telegramtoken = os.getenv('telegram')
reddit_cID = os.getenv('clientID')
reddit_secret = os.getenv('clientSecret')
subredditname = os.getenv('subreddit')
reddituser = os.getenv('reddituser')
redditpass = os.getenv('redditpass')
try:
    telegramChannelID = int(os.getenv('telegramChannel'))
except:
    log.exception("You did not provide a valid Telegram channel ID")
    exit()

processed_submissions = []

post = False

r = praw.Reddit(user_agent=redditapp,
                client_id=reddit_cID,
                client_secret=reddit_secret,
                username=reddituser,
                password=redditpass)

r.read_only = True
subreddit = r.subreddit(subredditname)

bot = telegram.Bot(token=telegramtoken)

start_time = round(time.time())

log.info("App started!")

def start(update, context):
    """Send a message about the bot when /start is used"""
    update.message.reply_text("I'm a bot created purely to get the latest posts from /r/" + subredditname + " and post it here. I am open-source and you can view my source code using the link below.\n\n", reply_markup=telegram.InlineKeyboardMarkup([[telegram.InlineKeyboardButton(text='My GitHub repository', url="https://github.com/argo0n/reddit-telegram-crosspostbot")]]))

def main():
    updater = Updater(telegramtoken, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    while True:
        try:
            log.info("Checking for new submissions")
            already_processed = []
            for submission in subreddit.new(limit=5):
                link = "https://redd.it/{id}".format(id=submission.id)
                try:
                    if submission.id in processed_submissions:
                        already_processed.append(submission.id)
                        pass
                    else:
                        log.info("Processing submission with ID {}...".format(submission.id))

                        if submission.link_flair_text == "Task":
                            title = html.escape(submission.title or '')
                            user = html.escape(submission.author.name or '') + f" *{humanize_timedelta(seconds=round(time.time())-submission.created_utc)}* ago"
                            text = html.escape(submission.selftext or '')
                            template = "*{title}*\n\n{text}\n\nCreated by u/{user}"
                            message = template.format(title=title, text=text[:600] + '...' if len(text) > 600 else text, link=link, user=user)

                            log.info("Posting {}".format(link))
                            bot.sendMessage(chat_id=telegramChannelID, text=message, reply_markup=telegram.InlineKeyboardMarkup([[telegram.InlineKeyboardButton(text='View on Reddit', url=submission.url)]]), parse_mode = telegram.ParseMode.MARKDOWN)
                            articlewords = ['article', 'writer', 'blog']
                            def check_if_article_task():
                                for word in articlewords:
                                    if word in title.lower() or word in text.lower():
                                        return True
                                return False
                            if check_if_article_task():
                                bot.sendMessage(chat_id=telegramChannelID, text="@iqeyial @jehrrrome dis might be what you're looking for")
                        processed_submissions.append(submission.id)
                except Exception as e:
                    log.exception("Error parsing {}".format(link))
            if len(already_processed) > 0:
                log.info(f"These {len(already_processed)} submissions were already processed before: {', '.join(already_processed)}")
        except Exception as e:
            log.exception("Error fetching new submissions, restarting in 10 secs")
        sleep(10)


if __name__ == '__main__':
    main()