from flask import Flask, render_template, request, redirect, url_for
import praw

app = Flask(__name__)

reddit = praw.Reddit(client_id='YOUR_CLIENT_ID',
                     client_secret='YOUR_CLIENT_SECRET',
                     user_agent='YOUR_APP_NAME')

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
