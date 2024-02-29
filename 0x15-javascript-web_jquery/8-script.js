// get list of title and list them
$(function() {
    // Fetch data from the API
    $.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
        // Iterate through each movie and add its title to the list
        $.each(data.results, function(index, movie) {
            $('#list_movies').append('<li>' + movie.title + '</li>');
        });
    });
});