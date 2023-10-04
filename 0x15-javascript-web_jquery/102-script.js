$(document).ready(() => {
  $('INPUT#btn_translate').click(() => {
    const code = $('INPUT#language_code').prop('value');
    $.ajax({
      url: 'https://hellosalut.stefanbohacek.dev/?lang=' + code,
      dataType: 'json',
      success: (data) => $('DIV#hello').text(data.hello)
    });
  });
});
