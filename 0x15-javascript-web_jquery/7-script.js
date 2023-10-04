$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
  dataType: 'json',
  success: (data) => $('DIV#character').text(data.name)
});
