from flask import Flask, render_template, request, redirect, url_for
import praw
import config
app = Flask(__name__)

user_agent = "Searchbot_01"
reddit = praw.Reddit(username=config.reddit_username,
                    password =config.reddit_password,
                    client_id=config.reddit_client_secret,
                    client_secret= config.reddit_client_id,
                    user_agent=user_agent,
                    check_for_async=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        subreddit_name = request.form['subreddit']
        return redirect(url_for('subreddit', subreddit_name=subreddit_name))
    return render_template('index.html')

@app.route('/r/<subreddit_name>')
def subreddit(subreddit_name):
    subreddit = reddit.subreddit(subreddit_name)
    posts = []
    try:
        for post in subreddit.new(limit=10):
            posts.append({'title': post.title, 'url': post.url})
    except Exception as e:
        posts.append({'title': 'Error fetching data', 'url': '#'})
    return render_template('subreddit.html', posts=posts, subreddit_name=subreddit_name)

if __name__ == '__main__':
    app.run(debug=True)
