#!/usr/bin/python3

import subprocess
from flask import Flask, request
from flask_executor import Executor



###############################################################################
# Flask Endpoints
###############################################################################
app = Flask(__name__)
executor = Executor(app)

@app.route("/greeting")
def hello_world():
    return "Welcome to the Halo Test Utility"

@app.route("/start")
def start():
    results = executor.submit(startWatchDate)
    return "Started the flask executor sample"



###############################################################################
# Subprocesses - watch -n 1 'date | tee -a time.log'
###############################################################################
def startWatchDate():
    cmd = ["watch", "-n", "1", "date"]
    subprocessId = subprocess.Popen(cmd, stdout=subprocess.PIPE, text=True)
    # cmd = ["watch -tn 1 date"]
    # subprocessId = subprocess.Popen(cmd, stdout=subprocess.PIPE, bufsize=0, shell=False)
    # while True:
    #     out = subprocessId.stdout.readline()
    #     print(out)
        # if(out == b'' and subprocessId.poll() is not None):
        #     break
        # if(out):
        #     print(subprocessId, type(out), out)
        # rc = subprocessId.poll()
    # for i in range(1, 10):
    #     print(i)



###############################################################################
# Main
###############################################################################
if __name__ == '__main__':

    app.run(port=6769)