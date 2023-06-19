from flask import Flask, render_template

app = Flask (__name__)

@app.route('/')
def home():
    return render_template('home.html', is_home=True)

@app.route('/projetos')
def projetos():
    return render_template('projetos.html')

@app.route('/informacoeseducacionais')
def informacoeseducacionais():
    return render_template('informacoeseducacionais.html', is_informacoeseducacionais=True)

@app.route('/interesses')
def interesses():
    return render_template('interesses.html', is_interesses=True)

if __name__ == '__main__':
    app.run(debug=True)