import praw

reddit = praw.Reddit(client_id='YOUR_CLIENT_ID',
                     client_secret='YOUR_CLIENT_SECRET',
                     user_agent='YOUR_APP_NAME')

subreddit_name = 'SubredditName'

subreddit = reddit.subreddit(subreddit_name)

print(f"Latest posts in /r/{subreddit_name}:\n")
for post in subreddit.new(limit=10):  # You can change 'new' to 'hot', 'top', etc.
    print(f"Title: {post.title}\nURL: {post.url}\n")

