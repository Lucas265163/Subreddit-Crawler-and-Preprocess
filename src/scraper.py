class Scraper:
    def __init__(self, reddit_client, subreddit, start_date, end_date):
        self.reddit_client = reddit_client
        self.subreddit = subreddit
        self.start_date = start_date
        self.end_date = end_date
    self.batch_size = 1000

    def fetch_comments(self):
        # Call RedditClient's fetch_comments method
        return self.reddit_client.fetch_comments(
            self.subreddit,
            self.start_date,
            self.end_date
        )

    def process_comments(self, comments):
        # comments is expected to be an iterable/generator of dicts
        for c in comments:
            body = c.get('body') if isinstance(c, dict) else None
            if not body:
                continue
            yield {
                'comment': body.strip(),
                'created_utc': c.get('created_utc'),
                'author': c.get('author'),
                'submission_id': c.get('submission_id'),
                'submission_title': c.get('submission_title'),
            }

    def save_comments(self, comments, filename):
    # Append comments (iterable of dicts) to a gzip-compressed JSONL file
    from src.utils import append_jsonl_gz
    append_jsonl_gz(filename, comments, batch_size=self.batch_size)

    def run(self):
        comment_stream = self.fetch_comments()
        batch = []
        for raw in comment_stream:
            # process_comments expects an iterable, so wrap raw in a list
            for processed in self.process_comments([raw]):
                batch.append(processed)
                if len(batch) >= self.batch_size:
                    self.save_comments(batch, 'data/comments.jsonl.gz')
                    batch = []

        if batch:
            self.save_comments(batch, 'data/comments.jsonl.gz')