#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__    = "Leonid Rusnac <leonidrusnac4 at gmail.com>"
__license__   = "MIT"
__copyright__ = "Copyright 2014, Leonid Rusnac"
__version__   = "0.1"

import requests
from lxml import html

class Attack(object):
	'''A class that contains methods for attacks'''

	def __init__(self, session, userConfig):
		self.session = session
		self.config = userConfig

	def attack(self, typeA='', min=0, max=0, id=0):
		'''
		if id attack by id, if not type attack by levels 
		else attack by type
		'''
		if id != 0:
			print 'Attack by id'
			response = self.session.post(self.config['siteUrl']+'alley/', data={
				'action': 'attack',
				'player': id,
				'werewolf': 0,
				'useitems': 0
			})

			if 'fight' in response.url:
				print 'Attack done'
				tree = html.fromstring(response.text)
				print "You have won: " + tree.xpath('//span[@class="tugriki"]/text()')[0]
			else:
				print 'Something gone wrong'
		elif typeA == '':
			print 'Attack by levels'
		else:
			print 'Attack by type'
			types = 'equal' , 'weak' , 'strong' , 'enemy' , 'victim'
			if typeA not in types:
				typeA = types[0]

			response = self.session.post(self.config['siteUrl']+'alley/search/type/', data={
				'type': typeA,
				'werewolf': 0
			})

			if 'alley/search' in response.url:
				tree = html.fromstring(response.text)

				if max > -1:
					i = 0
					while i < 50:
						i += 1
						victimLvl = tree.xpath('//div[@class="fighter2"]//span[@class="level"]/text()')[0]
						victimLvl = int(victimLvl.split('[')[1].split(']')[0])
						victimID = 0

						if (victimLvl <= max) and (victimLvl >= min):
							break
						response = self.session.get(self.config['siteUrl']+'alley/search/again/')
						tree = html.fromstring(response.text)
				else:
					victimLvl = tree.xpath('//div[@class="fighter2"]//span[@class="level"]/text()')[0]
					victimLvl = victimLvl.split('[')[1].split(']')[0]

				victimID = tree.xpath('//a[contains(@onclick,"alleyAttack")]/@onclick')[0]
				victimID = victimID.split('(')[1].split(',')[0]
				#print victimID
				self.attack(id=victimID)
			else:
				print 'Error'

