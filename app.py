from flask import Flask,render_template
from github import Github

import sys,os

template_dir = os.path.abspath('./html')
app = Flask(__name__, template_folder=template_dir)

@app.route("/v1/<filename>")
def showMessage(filename):
    g = Github()
    repo_url = str(sys.argv[1]).split("/")

    repo = g.get_user(repo_url[3]).get_repo(repo_url[4])

    file = repo.get_file_contents(filename)

    if file is None:
        page_not_found

    if (filename.endswith(".yml")) or (filename.endswith(".json")):
        return file.decoded_content
    else:
        return render_template('403.html'), 403

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/")
def hello():
    return "Hello from Dockerized Flask App!! "

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')