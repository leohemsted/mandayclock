import flask
from service.trivia import TriviaService
from service import Fact

facts = [Fact('Toyota sold {total_value} cars in this time globally!', 32, 10),
         Fact(u'You have been exposed to {total_value}\u00B5Sv of radiation during this time!', 0.345, 3600),
         ]

app = flask.Flask('mandayclock', static_url_path='/static')

@app.route('/')
def i_dont_even_know():
    # like this while i dev
    return app.send_static_file('front.html')
#     return flask.render_template('index.html', stuff=[1, 'poo', False])

@app.route('/trivia')
def i_probably_know_some_stuff():
    res = {
        'status': 'OK',
        'type': 'actual',
        'trivia': [],
    }

    attendees = flask.request.args.get('number_of_attendees', 0)
    elapsed_seconds = flask.request.args.get('elapsed_seconds', 0)

    if not attendees or not elapsed_seconds:
        res['status'] = 'Error'
    try:
        attendees, elapsed_seconds = int(attendees), int(elapsed_seconds)
    except:
        res['status'] = 'Error'

    trivia = TriviaService(facts, attendees, elapsed_seconds)
    res['trivia'] = trivia.get_facts(2)

    return flask.make_response(flask.jsonify(**res),
        500 if res['status'] == 'Error' else 200)

if __name__ == "__main__":
    app.run(debug=True)
