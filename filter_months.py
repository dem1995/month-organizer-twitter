import json
import argparse
import os
from datetime import datetime, timedelta

parser = argparse.ArgumentParser("")
parser.add_argument("tweet_file", help= "A jsonl file of tweets to parse")
parser.add_argument("-o", "--outfolder", default="month-outputs", help="The folder to put the output month-ranged tweet jsonl files to")
args = parser.parse_args()

if not os.path.exists(args.outfolder):
    os.makedirs(args.outfolder)

with open(f"{args.outfolder}/log.txt", 'a+') as logfile:
	logfile.write(f"Started at {datetime.now()}:\n")
	logfile.write(f"{args.tweet_file}")

curfile = None
curopen = None

with open(args.tweet_file, encoding="utf-8") as tweet_file:
	for tweet_json in tweet_file:
		tweet_dict = json.loads(tweet_json)
		date = tweet_dict['created_at']
		date = datetime.strptime(date, "%a %b %d %H:%M:%S %z %Y")
		date = date - timedelta(hours=6)

		datename = date.strftime("%Y-%m.jsonl")
		
		if datename != curopen:
			if curfile != None:
				curfile.close()
			curfile = open(datename, 'a+', encoding="utf-8")
			curopen = datename
		
		curfile.write(tweet_json)
