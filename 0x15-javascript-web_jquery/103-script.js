const $ = window.$;
window.onload = function () {
  $('INPUT#btn_translate').click(function () {
    translateHello();
  });
  $('INPUT#language_code').keypress(function (event) {
    if (event.kecode === 13) {
      translateHello();
    }
  });
};

function translateHello () {
  const lan = $('INPUT#language_code').val();
  const url = 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + lan;
  $.get(url, function (data) {
    $('DIV#hello').text(data.hello);
  });
}
