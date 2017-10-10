#!/usr/bin/env python
# -*- coding:utf-8 -*-


import time, subprocess, settings_gbf, json, sys
from requests_oauthlib import OAuth1Session


oauth_key = OAuth1Session(settings_gbf.CK, settings_gbf.CS, settings_gbf.ATK, settings_gbf.ATS)

params = {
    "count": "15"
}

req = oauth_key.get("https://api.twitter.com/1.1/statuses/home_timeline.json", params = params)

timeline = json.loads(req.text)

#--------------------
# ステータスコード確認
#--------------------
if req.status_code != 200:
    print ("Twitter API Error: %d" % req.status_code)
    sys.exit(1)

def main():
    for tweet in timeline:
        text = tweet[u'text']
        created_at = tweet[u'created_at']
        tweet_id = tweet[u'id_str']
        screen_name = tweet[u'user'][u'screen_name']
        user_name = tweet[u'user'][u'name']
        profile_image_url = tweet[u'user'][u'profile_image_url']

        if "media" in tweet:
            media = tweet['extended_entities']['media']
            for url in media:
                url_list.append(url['media_url'])

        print "投稿日: ", created_at
        print "ユーザID: ", screen_name
        print "tweetID: ", tweet_id
        print "ユーザ名: ", user_name
        print "ツイート内容: ", text
        # print "PIU: ",profile_image_url デバック用
        if "media_url" in tweet:
            print "画像のID: ",media_url
            cmd = "curl -s " + media_url + "| imgcat"
            subprocess.call(cmd, shell = True)

        time.sleep(10)

if __name__ == "__main__":
    main()
