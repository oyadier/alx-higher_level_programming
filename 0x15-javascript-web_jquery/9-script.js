const $ = window.$;
const url = 'https://fourtonfish.com/hellosalut/?lang=fr';

window.Document.$.getJSON(url, function (body) {
  const hello = body.hello;
  $('DIV#hello').text(hello);
});