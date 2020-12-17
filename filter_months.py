import json
import argparse
from datetime import datetime

parser = argparse.ArgumentParser("")
parser.add_argument("tweet_file", help= "A jsonl file of tweets to parse")
args = parser.parse_args()

with open(args.tweet_file) as tweet_file:
	for tweet_json in tweet_file:
		tweet_dict = json.loads(tweet_json)
		date = tweet_dict['created_at']
		date = datetime.strptime(date, "%a %b %d %H:%M:%S %z %Y\n")
		print(date)