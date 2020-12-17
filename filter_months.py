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
	logfile.write(f"Started at {datetime.datetime.now()}:\n")
	logfile.write(f"{args.tweet_file}")

monthfiles = dict()

with open(args.tweet_file) as tweet_file:
	for tweet_json in tweet_file:
		tweet_dict = json.loads(tweet_json)
		date = tweet_dict['created_at']
		date = datetime.strptime(date, "%a %b %d %H:%M:%S %z %Y\n")
		date = date - timedelta(hours=6)

		if date not in monthfiles:
			datename = date.strftime("%Y-%m.jsonl")
			monthfiles[date] = open(date.strftime, 'w+')
		
		monthfiles[date].write(tweet_json)

for month, monthfile in monthfiles.items():
	monthfile.close()
