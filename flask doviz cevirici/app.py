from crypt import methods
from flask import Flask,render_template,request
import requests

api_key = "your apı key"
url = "https://data.fixer.io/api/latest?access_key=" + api_key

app = Flask(__name__)

@app.route("/",methods = ["GET","POST"])
def index():
    if request.method == "POST" :
        firstCurrency = request.form.get("firstCurrency") #USD
        secondCurrency = request.form.get("secondCurrency") #TRY

        amount = request.form.get("amount") #15
        response = requests.get(url)

        app.logger.info(response)


        infos = response.json()

        firstValue = infos["rates"][firstCurrency] #1.23
        secondValue = infos["rates"][secondCurrency] #4.69
        result = (secondValue/ firstValue) *float(amount)

        currencyInfo =dict()

        currencyInfo["firstCurrency"] = firstCurrency
        currencyInfo["secondCurrency"] = secondCurrency
        currencyInfo["amount"] = amount
        currencyInfo["result"] = result

        app.logger.info(infos)

        return render_template("index.html",info = currencyInfo)
    else:
        return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)