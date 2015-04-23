import flask


app = flask.Flask('mandayclock')

@app.route('/')
def i_dont_even_know():
    return render_template('index.html', stuff=[1, 'poo', False])

if __name__ == "__main__":
    app.run(debug=True)
