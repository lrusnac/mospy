#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__    = "Leonid Rusnac <leonidrusnac4 at gmail.com>"
__license__   = "MIT"
__copyright__ = "Copyright 2014, Leonid Rusnac"
__version__   = "0.1"

import requests
from lxml import html

class Gift(object):
    def __init__(self, session, userConfig):
        self.session = session
        self.config = userConfig

    def makeGift(self, receiver, giftId):
        #grab the user details whom to send the gift

        #get token
        response = self.session.get(self.config['siteUrl']+"shop/section/gifts/#all")

        if response.url == (self.config['siteUrl']+"shop/section/gifts/#all"):
            #get info of the player search info inside the response.text

            print "ook"
            tree = html.fromstring(response.text)

            # onClick Shop.checkAndBuy  
            #//a[contains(@onclick,"alleyAttack")]/@onclick

            token = tree.xpath('//span[contains(@onclick,"Shop.checkAndBuy")]/@onclick')[0].split("'")[3]

            response = self.session.post(self.config['siteUrl']+'shop/', data={
                'action': 'buy',
                'item': giftId,
                'playerid': receiver,
                'key': token,
                'comment': ' ',
                'private': 'yes',
                'anonimous': 'yes'
            })

        else:
            print "error gifts"
