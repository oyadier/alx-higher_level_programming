const $ = window.$;
$(function() {
    // Fetch data from the API
    $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data) {
        // Display the translation in the <div id="hello">
        $('DIV#hello').text(data.hello);
    });
});