/**
 * Particleground demo
 * @author Jonathan Nicol - @mrjnicol
 */
//
$(document).ready(function() {
  $('#particles').particleground({
    // dotColor: '#5cbdaa',
    // lineColor: '#5cbdaa'
    lineColor:'black'
  });
  $('.intro').css({
    'margin-top': -($('.intro').height() / 2)
  });
});