from flask import Flask,render_template

#other packages
from covid import Covid
from main import country_list, active_list, confirmed_list, death_list

app = Flask(__name__)

covid = Covid()
bruh = covid.get_data()

@app.route('/')
def home():
    return render_template('index.html', len = len(country_list), country_list = country_list, active_list = active_list, confirmed_list = confirmed_list, death_list = death_list)

if __name__ == "__main__":
    app.run(debug=True)