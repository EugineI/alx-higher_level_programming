/* global $ */
$(document).ready(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
    $('#hello').text(data.hello);
  }).fail(function () {
    $('#hello').text('Failed to load greeting.');
  });
});
