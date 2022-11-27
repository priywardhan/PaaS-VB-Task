from flask import Flask, request,render_template
from urllib.request import urlopen
import json
# password - seller123
app = Flask(__name__, template_folder='template')
@app.route('/', methods = ['GET'])
def home():
    if(request.method == 'GET'):
        response = urlopen("https://dummyjson.com/products/")
        jsonReturn=json.loads(response.read())
        productList=[]
        for i in range(len(jsonReturn['products'])):
            dictTemp={"Title": jsonReturn['products'][i]['title'], 
            "Description": jsonReturn['products'][i]['description'],
            "Stock":jsonReturn['products'][i]['stock'],
            "Brand":jsonReturn['products'][i]['brand'],
            "Price":jsonReturn['products'][i]['price']}
            productList.append(dictTemp)
        return render_template('seller.html',prodList=productList)
def writeItems():
    response = urlopen("https://dummyjson.com/products/")
    jsonReturn=json.loads(response.read())
    productList=[]
    for i in range(len(jsonReturn['products'])):
        dictTemp={"Title": jsonReturn['products'][i]['title'], 
        "Description": jsonReturn['products'][i]['description'],
        "Stock":jsonReturn['products'][i]['stock'],
        "Brand":jsonReturn['products'][i]['brand'],
        "Price":jsonReturn['products'][i]['price']}
        productList.append(dictTemp)
    prettyList = json.dumps (productList, indent=4)
    return prettyList
@app.route('/backupitems', methods = ['GET'])
def backup():
    if(request.method == 'GET'):
        messageWeb = 'Backing up your items...'
        file = open('/tmp/backupItems.txt' , 'a')
        file.write(str(writeItems()) + '\n')
        file.close()
        
        with open('/tmp/backupItems.txt') as f:
            for line in f:
                messageWeb += '\n'
                messageWeb += line
        f.close()
        return messageWeb
if __name__ == '__main__':

	app.run(debug=True, host='0.0.0.0', port=80)


