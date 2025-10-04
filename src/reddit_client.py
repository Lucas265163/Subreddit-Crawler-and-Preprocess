class RedditClient:
    def __init__(self, client_id, client_secret, user_agent):
        import praw
        self.reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent
        )

    def get_subreddit(self, subreddit_name):
        return self.reddit.subreddit(subreddit_name)

    def fetch_comments(self, subreddit_name, start_date, end_date):
        """Yield comment records as dicts with selected fields.

        Each yielded dict will contain: body, created_utc, author, submission_id, submission_title
        """
        subreddit = self.get_subreddit(subreddit_name)
        for submission in subreddit.new(limit=None):
            if submission.created_utc < start_date or submission.created_utc > end_date:
                continue
            submission.comments.replace_more(limit=0)
            for comment in submission.comments.list():
                yield {
                    'body': getattr(comment, 'body', None),
                    'created_utc': getattr(comment, 'created_utc', None),
                    'author': getattr(comment, 'author', None).name if getattr(comment, 'author', None) else None,
                    'submission_id': getattr(submission, 'id', None),
                    'submission_title': getattr(submission, 'title', None),
                }

    def authenticate(self):
        # This method can be used to check if the client is authenticated
        return self.reddit.user.me() is not None