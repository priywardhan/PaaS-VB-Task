from flask import Flask, request
import requests
app = Flask(__name__)
@app.route('/', methods = ['GET'])
def home():
    if(request.method == 'GET'):
        servers = ['http://seller', 'http://buyer']
        data = {"servers": []}
        for server in servers:
            try:
                response = requests.get(server)
                if(response.status_code == 200):
                    data['servers'].append(str(server) + ' is up and running')
                else:
                    data['servers'].append(str(server) + ' is down... Status code: ' + str(response.status_code))
            except Exception as e:
                data['servers'].append(str(e))
    return data


if __name__ == '__main__':

	app.run(debug=True, host='0.0.0.0', port=80)


