const url = 'https://swapi-api.hbtn.io/api/films/?format=json'
$.get(url , function(data, textStatus) {
  if (textStatus == 'success') {
    for (const film of data.results) {
      $('UL#list_movies').append('<li>' + film.title + '</li>');
    }
  }
});
