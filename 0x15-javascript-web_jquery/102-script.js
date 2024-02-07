const $ = window.$;
window.onload = function () {
  $('INPUT#btn_translate').click(function () {
    const lan = $('INPUT#language_code').val();
    const url = 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + lan;
    $.get(url, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
};
