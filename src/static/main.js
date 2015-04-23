'use strict';
/* global moment */

var headcount;
var start_time = null;
var refresh_timer = null;
var started = false;

var time_span = document.getElementById('time');
var the_word_start = document.getElementById('start');
var people_input = document.getElementById('peeps');

var factoid_span = document.getElementById('interesting_factoid');

var uname_input = document.getElementById('username');
var pword_input = document.getElementById('password');

var set_attrs = function(el, attrs) {
    for (var attr in attrs) {
        el.setAttribute(attr, attrs[attr]);
    }
};

var start_clock = function() {
    // change started->start

    //lock down the
    the_word_start.textContent = 'started';
    time_span.textContent = 'just now!';

    start_time = moment();
    refresh_timer = setInterval(function() {
        time_span.textContent = start_time.fromNow();
        update_factoid(moment() - start_time);
    }, 1000);
};

var stop_clock = function() {
    window.clearInterval(refresh_timer);
    the_word_start.textContent = '';
    time_span.textContent = 'has ended! go home.';
};

var update_factoid = function() {
    if (headcount) {
        var secs_so_far = (moment() - start_time) / 1000.0;
        var mandays = headcount * secs_so_far / 86400.0;
        factoid_span.textContent = 'you have wasted ' + mandays + ' man days so far';
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
    input.addEventListener('change', function() {
        headcount = +input.value;
    });

    people_input.parentElement.replaceChild(input, people_input);
    input.focus();
});

pword_input.addEventListener('click', function() {
    var input = document.createElement('input');
    set_attrs(input, {
        'id': 'peeps',
        'type': 'password',
        'class': 'clickable',
        'value': '********'
    });

    pword_input.parentElement.replaceChild(input, pword_input);
    input.focus();
});

uname_input.addEventListener('click', function() {
    var input = document.createElement('input');
    set_attrs(input, {
        'id': 'username',
        'type': 'text',
        'class': 'clickable',
        'value': 'fred'
    });
    uname_input.parentElement.replaceChild(input, uname_input);
    input.focus();
});

time_span.addEventListener('click', function() {
    if (started) {
        stop_clock();
    } else {
        start_clock();
    }
    started = !started;
});
