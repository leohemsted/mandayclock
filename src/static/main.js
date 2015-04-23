'use strict';
/* global moment */

var people_input = document.getElementById('peeps');
people_input.addEventListener('click', function() {
    var input = document.createElement('input');
    input.setAttribute('id', 'peeps');
    input.setAttribute('type', 'number');
    input.setAttribute('class', 'clickable');
    input.setAttribute('maxlength', '2');
    input.setAttribute('size', '2');
    input.setAttribute('value', '7');
    people_input.parentElement.replaceChild(input, people_input);
    input.focus();
});


var start_time = null;
var refresh_timer = null;

var time_span = document.getElementById('time');
var the_word_start = document.getElementById('start');
var started = false;

var start_clock = function() {
    // change started->start

    //lock down the
    the_word_start.textContent = 'started';
    time_span.textContent = 'just now!';

    start_time = moment();
    refresh_timer = setInterval(function() {
        time_span.textContent = start_time.fromNow();
    }, 1000);
}
var stop_clock = function() {
    window.clearInterval(refresh_timer);
    the_word_start.textContent = '';
    time_span.textContent = 'has ended! Go home.';
}

time_span.addEventListener('click', function() {
    if (started) {
        stop_clock();
    } else {
        start_clock();
    }
    started = !started;

});
