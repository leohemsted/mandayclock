'use strict';
/* global moment */

var headcount;
var start_time = null;
var refresh_timer = null;
var factoid_timer = null;
var started = false;

var time_span = document.getElementById('time');
var the_word_start = document.getElementById('start');
var people_input = document.getElementById('peeps');

var factoid_list = document.getElementById('interesting_factoids');

var uname_input = document.getElementById('username');
var pword_input = document.getElementById('password');
var exchange_button = document.getElementById('exchange');

var exchange_div = document.getElementById('exchange_info');
var current_event_list = document.getElementById('current_events');
var future_event_list = document.getElementById('future_events');

var set_attrs = function(el, attrs) {
    for (var attr in attrs) {
        el.setAttribute(attr, attrs[attr]);
    }
};

var factoid_ajax = function(headcount, secs) {
    var url = 'trivia?number_of_attendees='+headcount+'&elapsed_seconds='+secs;
    var ajax = new XMLHttpRequest();
    ajax.onreadystatechange = function() {
        if (ajax.readyState === XMLHttpRequest.DONE) {
           if (ajax.status === 200){
                update_factoid_json(ajax.responseText);
           } else {
                update_factoid_basic();
           }
        }
    };

    ajax.open("GET", url, true);
    ajax.send();
};

var exchange_ajax = function(un, pw) {
    var url = 'ex_trivia';
    var ajax = new XMLHttpRequest();
    ajax.onreadystatechange = function() {
        if (ajax.readyState === XMLHttpRequest.DONE) {
            update_exchange(ajax.responseText);
        }
    };

    ajax.open("POST", url, true);
    ajax.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    ajax.send(JSON.stringify({username:un, password:pw}));
};

/***************************************************/

var start_clock = function() {
    // change started->start

    //lock down the
    the_word_start.textContent = 'started';
    time_span.textContent = 'just now!';

    start_time = moment();
    refresh_timer = setInterval(function() {
        time_span.textContent = start_time.fromNow();
    }, 1000);
    factoid_timer = setInterval(function() {
        factoid_ajax(headcount, (moment() - start_time) / 1000.0);
    }, 1000 * 10);
};

var stop_clock = function() {
    window.clearInterval(refresh_timer);
    window.clearInterval(factoid_timer);
    the_word_start.textContent = '';
    time_span.textContent = 'has ended! go home.';
};

var update_factoid_json = function(json_string) {
    var data = JSON.parse(json_string);
    update_factoid_html(data.trivia);
};

var update_factoid_basic = function() {
    if (headcount) {
        var secs_so_far = (moment() - start_time) / 1000.0;
        var mandays = headcount * secs_so_far / 86400.0;
        update_factoid_html(['you have wasted ' + mandays + ' man days so far']);
    }
};

var update_factoid_html = function(factoids) {
    while (factoid_list.firstChild) {
        factoid_list.removeChild(factoid_list.firstChild);
    }

    for (var i in factoids) {
        var nugget_of_gold = document.createElement('li');
        nugget_of_gold.textContent = factoids[i];
        factoid_list.appendChild(nugget_of_gold);
    }
};

var create_event_node = function(event) {
    var el = document.createElement('li');
    el.innerHTML = (
        '<span class="big">' + event.subject + '</span> (' + event.start_date + ')</br>' +
        event.attendees.length + ' attendees</br>' + event.trivia.join('</br>')
    )
    return el;
};

var update_exchange = function(exchange_data) {
    var exchange_info = JSON.parse(exchange_data);

    while (current_event_list.firstChild) {
        current_event_list.removeChild(current_event_list.firstChild);
    }
    while (future_event_list.firstChild) {
        future_event_list.removeChild(future_event_list.firstChild);
    }
    var no_events = document.createElement('li');
    no_events.innerHTML = 'nothing at all! <span class="small">nothing at all!</span> </span class="smaller">nothing at all!</span>';


    if (exchange_info.current_events) {
        for (var i in exchange_info.current_events) {
            var current_event = exchange_info.current_events[i];
            current_event_list.appendChild(create_event_node(current_event));
        }
    } else {
        current_event_list.appendChild(no_events.cloneNode());
    }

    if (exchange_info.future_events) {
        for (var i in exchange_info.future_events) {
            var future_event = exchange_info.future_events[i];
            var node = create_event_node(future_event);
            node.setAttribute('class', 'future');
            future_event_list.appendChild(node);
        }
    } else {
        future_event_list.appendChild(no_events.cloneNode());
    }
};

/***************************************************/

people_input.addEventListener('click', function() {
    var input = document.createElement('input');
    set_attrs(input, {
        'id': 'peeps',
        'type': 'number',
        'class': 'clickable',
        'value': '7'
    });
    headcount = 7;
    input.addEventListener('change', function() {
        headcount = +input.value;
    });

    people_input.parentElement.replaceChild(input, people_input);
    people_input = input;
    input.focus();
});

pword_input.addEventListener('click', function() {
    var input = document.createElement('input');
    set_attrs(input, {
        'id': 'peeps',
        'type': 'password',
        'class': 'clickable',
        'placeholder': '********'
    });

    pword_input.parentElement.replaceChild(input, pword_input);
    input.focus();
    pword_input = input;
});

uname_input.addEventListener('click', function() {
    var input = document.createElement('input');
    set_attrs(input, {
        'id': 'username',
        'type': 'text',
        'class': 'clickable',
        'placeholder': 'fred'
    });
    uname_input.parentElement.replaceChild(input, uname_input);
    uname_input = input;
    input.focus();
});

exchange_button.addEventListener('click', function() {
    exchange_div.removeAttribute('class');
    exchange_ajax(uname_input.value, pword_input.value);
});

time_span.addEventListener('click', function() {
    if (started) {
        stop_clock();
    } else {
        start_clock();
    }
    started = !started;
});
