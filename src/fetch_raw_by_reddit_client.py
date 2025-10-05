"""Fetch raw comments using RedditClient for a specific date range and save to gzip JSONL.

Usage: set environment variables (API_CLIENT_ID, API_CLIENT_SECRET, API_USER_AGENT, SUBREDDIT_NAME)
then run this module. It will write to data/raw/comments_2022-01-01_2022-01-31.jsonl.gz
"""
from datetime import datetime, timedelta
import os
import sys

from reddit_client import RedditClient
from utils import to_timestamp, append_jsonl_gz
from config import API_CLIENT_ID, API_CLIENT_SECRET, API_USER_AGENT, SUBREDDIT_NAME


def ensure_output_dir(path):
    d = os.path.dirname(path)
    if d and not os.path.exists(d):
        os.makedirs(d, exist_ok=True)


def fetch_and_save(subreddit: str, start_iso: str, end_iso: str, out_path: str):
    # Convert to timestamps (seconds since epoch)
    start_ts = to_timestamp(start_iso)
    # Make end inclusive by setting to end of the day if a date-only string was provided
    # If caller provided a full datetime, to_timestamp will preserve it.
    end_dt = datetime.fromisoformat(end_iso)
    if end_dt.time() == datetime.min.time():
        end_dt = end_dt + timedelta(days=1, seconds=-1)
    end_ts = int(end_dt.timestamp())

    if not all([API_CLIENT_ID, API_CLIENT_SECRET, API_USER_AGENT]):
        print("Missing Reddit API credentials. Please set API_CLIENT_ID, API_CLIENT_SECRET, API_USER_AGENT in your environment (see .env).")
        sys.exit(1)

    client = RedditClient(API_CLIENT_ID, API_CLIENT_SECRET, API_USER_AGENT)

    print(f"Fetching comments from r/{subreddit} between {start_iso} ({start_ts}) and {end_dt.isoformat()} ({end_ts})")
    gen = client.fetch_comments(subreddit, start_ts, end_ts)

    ensure_output_dir(out_path)

    # Stream to gzip JSONL in small batches to avoid high memory use
    batch = []
    batch_size = 500
    total = 0
    for rec in gen:
        batch.append(rec)
        if len(batch) >= batch_size:
            append_jsonl_gz(out_path, batch, batch_size=len(batch))
            total += len(batch)
            print(f"Saved {total} comments so far...")
            batch = []

    if batch:
        append_jsonl_gz(out_path, batch, batch_size=len(batch))
        total += len(batch)

    print(f"Finished. Total comments saved: {total}")


if __name__ == '__main__':
    # Defaults: use config.SUBREDDIT_NAME if available, otherwise 'laptop'
    subreddit = SUBREDDIT_NAME or os.getenv('SUBREDDIT', 'laptop')
    start_iso = '2022-01-01'
    end_iso = '2022-01-31'
    out_path = 'data/raw/comments_2022-01-01_2022-01-31.jsonl.gz'

    fetch_and_save(subreddit, start_iso, end_iso, out_path)
