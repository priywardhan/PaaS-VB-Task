from flask import Flask, render_template, request
from urllib.request import urlopen
import json
# password - buyer123
app = Flask(__name__,template_folder='template')

@app.route('/', methods = ['GET'])
def home():
    if(request.method == 'GET'):
        response = urlopen("https://dummyjson.com/products/")
        jsonReturn=json.loads(response.read())
        productList=[]
        for i in range(len(jsonReturn['products'])):
            dictTemp={"Title": jsonReturn['products'][i]['title'], 
            "Description": jsonReturn['products'][i]['description'],
            "Brand":jsonReturn['products'][i]['brand'],
            "Price":jsonReturn['products'][i]["price"],
            "Rating": jsonReturn['products'][i]["rating"],
            }
            productList.append(dictTemp)
        return render_template('buyer.html',prodList=productList)
if __name__ == '__main__':

	app.run(debug=True, host='0.0.0.0', port=80)


