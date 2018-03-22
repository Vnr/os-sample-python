from flask import Flask
import requests
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/requeststest')
def requeststest():
    #logging.info('*******import requests*************')
    return requests.get("http://httpbin.org/get",
    					headers={'Referer': 'https://pamyat-naroda.ru/', 'User-Agent': 'Mozilla'}).content  # verify=False not working


if __name__ == "__main__":
    app.run()
