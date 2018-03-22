from flask import Flask, Response, request
import requests
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!"


@application.route('/requeststest')
def requeststest():
    #logging.info('*******import requests*************')
    result = requests.post("http://httpbin.org/post",
    					data={'great job': 'super'},
    					headers={'Referer': 'https://pamyat-naroda.ru/', 'User-Agent': 'Mozilla'})  # verify=False not working
    return Response(result.content, headers={'Access-Control-Allow-Origin': '*'})


@app.route('/obd/<path:path>', methods=['GET','POST'])
def proxy(path):
    #https://cloud.google.com/appengine/docs/python/urlfetch/
    #from google.appengine.api import urlfetch
    
    #return request.method + "<br>" + request.url_root + "<br>" + request.data
    # http://flask.pocoo.org/docs/0.10/api/#flask.Request.get_json
    # request.get_data()    # To get the raw data, regardless of content type.
    # page = request.args.get("page")
    # password = request.form.get('password')
    
    #https://cdn.pamyatnaroda.mil.ru
    url = 'https://cdn.pamyat-naroda.ru/ind/' + path
    
    #https://cloud.google.com/appengine/docs/standard/python/issue-requests
    result = requests.post(url=url,
        data=request.data,
        headers={'Referer': 'https://pamyat-naroda.ru/', 'User-Agent': 'Mozilla'})

#    if result.status_code == 200:
#      doSomethingWithResult(result.content)

    return Response(result.content, headers={'Access-Control-Allow-Origin': '*'})

if __name__ == "__main__":
    application.run()
