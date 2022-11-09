from flask import Flask, render_template

import pandas as pd

app = Flask(__name__)

# reading the data in the csv file
df=pd.read_excel("Book2.xlsx")


# route to html page - "table"
@app.route('/')
@app.route('/table')
def table():
	# converting csv to html
	data = pd.read_excel("Financials.xlsx", header=0)
	return render_template('index.html', tables=[data.to_html()], titles=[''])

if __name__ == "__main__":
	app.run(debug=False, host="0.0.0.0")
