$(document).ready(() => {
  const translate = () => {
    const code = $('INPUT#language_code').prop('value');
    $.ajax({
      url: 'https://hellosalut.stefanbohacek.dev/?lang=' + code,
      dataType: 'json',
      success: (data) => $('DIV#hello').text(data.hello)
    });
  };

  $('INPUT#btn_translate').click(translate);
  $('INPUT#language_code').on('change', translate);
  $('INPUT#language_code').focus();
});
