import flask


app = flask.Flask('mandayclock')


@app.route('/')
def i_dont_even_know():
    return (
"""
HELLO
"""
)

if __name__ == "__main__":
    app.run()
