from crypt import methods
from flask import Flask, render_template,request, flash, redirect, url_for
from forex_python.converter import CurrencyRates

app = Flask(__name__)
app.config["SECRET_KEY"] = "curren$y"

# codes = CurrencyCodes()
#store all currency rates into a variable as a dictionary
c = CurrencyRates()
rates = c.get_rate('USD')

# show homepage
@app.route("/", methods=["POST","GET"])
def home():
    return render_template("home.html")

#show results page, should arrive to results.html if input is correct
@app.route("/results", methods=["POST","GET"])
def results():
    #grab user information from form and change characters to uppercase

    conv_from = (request.form.get('ConvertFrom').upper())
    conv_to = (request.form.get('convertTo').upper())
    amount = float(request.form.get('amount'))
    print(amount)

    if conv_from not in rates:
        flash(f"Not Valid Code: {conv_from}")

    if conv_to not in rates:
        flash(f"Not Valid Code: {conv_to}")

    if not isinstance(amount, float) :
        flash("Not a valid amount.")

    if conv_to not in rates or conv_from not in rates or not isinstance(amount, float):
        return redirect(url_for('home'))
    else :
        return render_template('results.html', conv_from=conv_from, conv_to=conv_to, amount=amount)


















    
    

    # try:
    #     results = round(rates.convert(conv_from, conv_to, amount), 2)
    #     symbol = codes.get_symbol(conv_to)
    #     return render_template("index.html", conv_from=conv_from, conv_to=conv_to, amount=amount, results=results, symbol=symbol)
    # # except RatesNotAvailableError:
    # #     flash("Please enter a valid currency")
    # #     return redirect('/')
    # except (ValueError, TypeError):
    #     flash("Oops something went wrong")
    #     return redirect('/')
    




