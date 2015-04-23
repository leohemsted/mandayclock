import flask


app = flask.Flask('mandayclock', static_url_path='/static')

@app.route('/')
def i_dont_even_know():
    # like this while i dev
    return app.send_static_file('front.html')
#     return flask.render_template('index.html', stuff=[1, 'poo', False])

if __name__ == "__main__":
    app.run(debug=True)
