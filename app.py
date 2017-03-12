from flask import Flask
from git import Repo

import sys, shutil, os
from os import listdir
from os.path import isfile

app = Flask(__name__)

local_path = "./config"

def fetchRepo():
    if (os.path.isdir(local_path)):
        shutil.rmtree(local_path)
    else:
        pass

    repo_url = str(sys.argv[1])
    repository = Repo.clone_from(repo_url, local_path)

@app.route("/v1/<filename>")
def showMessage(filename):
    if isfile(local_path+"/"+filename):
        file = open(local_path+"/"+filename) 
        return file.read()
    else:
        return "Page not found"

@app.route("/")
def hello():
    return "Hello from Dockerized Flask App!!"

if __name__ == "__main__":
    fetchRepo()
    app.run(debug=True,host='0.0.0.0')