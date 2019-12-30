# agrv is string, can't be used now, need convert to right format
import json
import re
from datetime import datetime,timedelta

def convert(argv):
	keyinfo = []
	account = argv[1] # string ->string
	keyinfo.append(account)
	
	password = argv[2] # string -> string
	keyinfo.append(password)
	
	preiod = argv[3] #string -> string
	keyinfo.append(preiod)

	money = argv[4] #string-> string
	keyinfo.append(money)

	print(keyinfo)
	
	return keyinfo