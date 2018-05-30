#To access page:
#   Find out IPv4 address of host
#   Go to device connected to same network
#   Open browser
#   Type the address in, followed by ":5000"
#   If address = 192.168.0.1, then type 192.168.0.1:5000

#Imports
from flask import Flask
app = Flask(__name__)

#Page
@app.route("/")
def hello():
    return "Here's some text"

#Host the page
if __name__ == "__main__":
    app.run(host = "0.0.0.0")

