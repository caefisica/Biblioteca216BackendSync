from flask import Flask

app = Flask(__name__)
app.config.from_object("biblioteca216sync.config")

from biblioteca216sync.routes import api