const url = 'https://fourtonfish.com/hellosalut/?lang=fr'
$.get(url , function(data, textStatus) {
  if (textStatus == 'success') {
    $('DIV#hello').text(data.hello);
  }
});
