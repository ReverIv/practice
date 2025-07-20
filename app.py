from flask import Flask, render_template #Иванов Игнатий

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('main page.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')



if __name__ == '__main__' :
    app.run(debug=True)
