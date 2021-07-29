import os
from flask import Flask, flash, request, redirect, url_for, render_template


import urllib.request

import os




app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
