$(document).ready(() => $.ajax({
  url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
  dataType: 'json',
  success: (data) => $('DIV#hello').text(data.hello)
}));
