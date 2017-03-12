from flask import Flask
#from pygit2 import clone_repository
from git import Repo

import sys, shutil, os
from os import listdir
from os.path import isfile, join

app = Flask(__name__)

local_path = "./configRepo"
file_list = []

def process():
    if (os.path.isdir(local_path)):
        shutil.rmtree(local_path)
    else:
        pass

    repo_url = str(sys.argv[1])
    print repo_url
    #repo_url = "https://github.com/sithu/assignment1-config-example"
    repository = Repo.clone_from(repo_url, local_path)

@app.route("/v1/<filename>")
def message(filename):
    if isfile(local_path+"/"+filename):
        file = open(local_path+"/"+filename) 
        return file.read()
    else:
        return "Page not found"

@app.route("/")
def hello():
    return "Hello from Dockerized Flask App!!"

if __name__ == "__main__":
    process()
    app.run(debug=True,host='0.0.0.0')