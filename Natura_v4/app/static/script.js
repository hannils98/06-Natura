


$(document).ready(function(){
    $(".dropdown-toggle").dropdown();
  });



$(document).ready(function () {
        var url = window.location;
    // Will only work if string in href matches with location
        $('ul.nav a[href="' + url + '"]').parent().addClass('active');

    // Will also work for relative and absolute hrefs
        $('ul.nav a').filter(function () {
            return this.href == url;
        }).parent().addClass('active').parent().parent().addClass('active');
    });

//image grid//
    function getRandomSize(min, max) {
        return Math.round(Math.random() * (max - min) + min);
      }
      
      var allImages = "";
      
      for (var i = 0; i < 25; i++) {
        var width = getRandomSize(500, 800);
        var height =  getRandomSize(500, 800);
        allImages += '<img src="/app/static/uploads/{{image}}" ';
      }
      
      $('#photos').append(allImages);

