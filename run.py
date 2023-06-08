import os
from argparse import ArgumentParser

from src.priority_queue import BucketList

BUCKET_LIST_FILE = "bucket_list.csv"

parser = ArgumentParser(description="""View and modify bucket list via command line""")

parser.add_argument("-add", type=str, action="store")
parser.add_argument("-remove", type=str, action="store")
parser.add_argument("-prioritize", type=str, action="store")
parser.add_argument("-get", action="store_true")
parser.add_argument("-list", action="store_true")

args = parser.parse_args()
if BUCKET_LIST_FILE in os.listdir("./"):
    bucket_list = BucketList.from_file(BUCKET_LIST_FILE)
else:
    bucket_list = BucketList()

if args.add:
    bucket_list.add(args.add)
if args.remove:
    bucket_list.remove(args.remove)
if args.prioritize:
    bucket_list.prioritize(args.prioritize)
if args.get:
    print(bucket_list.get())
if args.list:
    bucket_list.print(verbose=True)
bucket_list.to_file(BUCKET_LIST_FILE)
