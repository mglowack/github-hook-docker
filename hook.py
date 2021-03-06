from github_webhook import Webhook
from flask import Flask
from git import Repo
import os

app = Flask(__name__)  # Standard Flask app
webhook = Webhook(app) # Defines '/postreceive' endpoint

@app.route("/")        # Standard Flask endpoint
def hello_world():
    return "Hello, World!"

@webhook.hook()        # Defines a handler for the 'push' event
def on_push(data):
    name = data['repository']['name']
    branch = data['ref'].split('/')[-1]
    commits = data['commits']
    print("[{2}] Got push on {0} with: {1} commits:".format(branch, len(commits), name))

    for ci in commits:
        print "-", ci['message']

    if not os.path.isdir(name):
        print 'cloning repo: {0}'.format(url)
        Repo.clone_from(url, name)

    repo = Repo(name)
    git = repo.git
    git.checkout(branch)
    git.fetch()
    git.pull()

    print 'switched to branch: {0}'.format(branch)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

