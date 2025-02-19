/* global $ */
$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    const movies = data.results;
    movies.forEach(function (movie) {
      $('#list_movies').append('<li>' + movie.title + '</li>');
    });
  }).fail(function () {
    $('#list_movies').append('<li>Failed to load movies.</li>');
  });
});
