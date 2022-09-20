# -*- coding: UTF-8 -*-
import sys
import json
import emjipy.unicode
import re

# - Strat -

get = json.dumps(emjipy.unicode.Emoji_data)

emoji_uni = json.loads(get)

# - function -
def emoji_get(info, l, k):
	emoji_ = 'None'
	info = info.replace(':','').replace('_',' ')
	for j in emoji_uni:
		
		if emoji_uni[j][l].replace(':','').replace(',','') == info and emoji_uni[j][2] == 'True':
			
			emoji_ = emoji_uni[j][k]
			
	return emoji_

def emoji(name):

	emoji_ = emoji_get(name,3 ,0)

	return emoji_

def emoji_name(emoji_code):

	emoji_ = emoji_get(emoji_code,0 ,3)

	return emoji_

def emoji_unicode(emoji):

	emoji_ = emoji_get(emoji,0 ,1)
	
	return emoji_

def version(emoji):

	emoji_ = emoji_get(emoji,0 ,4)
	
	return emoji_

def emojiz(text):

	get_emoji = re.findall(':.*?:',text)
	for i in get_emoji:
		text = text.replace(i,emoji(i))
		
	return text
