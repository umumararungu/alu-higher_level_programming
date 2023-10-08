$(document).ready(function() {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'GET',
    success: function(data) {
      // Loop through the results and append movie titles to the list
      for (var i = 0; i < data.results.length; i++) {
        var title = data.results[i].title;
        $('#list_movies').append('<li>' + title + '</li>');
      }
    },
    error: function() {
      $('#list_movies').append('<li>Error fetching movies</li>');
    }
  });
});
