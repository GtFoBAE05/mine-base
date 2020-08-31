import time
import datetime
import constants
import threading

from twitter import Twitter

tw = Twitter()

def start():
    print("Starting program...")
    dms = list()
    while True:
        if len(dms) > 0:
            for i in range(len(dms)):
                message = dms[i]['message']
                # I take sender_id just in case you want to know who's sent the message
                sender_id = dms[i]['sender_id']
                id = dms[i]['id']

                if len(message) > 0 :
                    if "!huh" in message:
                        if len(message) > 0:
                            if dms[i]['media'] is None:
                                print("DM will be posted")
                                tw.post_tweet(message)
                                tw.delete_dm(id)
                            else:
                                print("DM will be posted with media")
                                print(dms[i]['shorted_media_url'])
                                tw.post_tweet_with_media(message, dms[i]['media'],dms[i]['shorted_media_url'], dms[i]['type'])
                                tw.delete_dm(id)


            dms = list()

        else:
            print("Direct message is empty...")
            dms = tw.read_dm()
            if len(dms) == 0 :
                time.sleep(60)

if __name__ == "__main__":
    start()