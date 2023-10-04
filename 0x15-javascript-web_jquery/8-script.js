$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  dataType: 'json',
  success: (data) => {
    data.results.forEach((movie) => {
      $('UL#list_movies').append(`<li>${movie.title}</li>`);
    });
  }
});
