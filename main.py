import praw

subreddit_name = input("Enter the subreddit name: ")
filter_type = input("Choose the filter (hot, new, top): ").lower()

reddit = praw.Reddit(client_id='YOUR_CLIENT_ID',
                     client_secret='YOUR_CLIENT_SECRET',
                     user_agent='YOUR_APP_NAME')

subreddit = reddit.subreddit(subreddit_name)

print(f"Fetching {filter_type} posts from /r/{subreddit_name}:")

if filter_type == "hot":
    posts = subreddit.hot(limit=10)
elif filter_type == "top":
    posts = subreddit.top(limit=10)
else:  
    posts = subreddit.new(limit=10)

for post in posts:
    print(f"{post.title} (Upvotes: {post.ups})")
