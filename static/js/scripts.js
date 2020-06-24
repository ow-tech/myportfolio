// var scroll = new SmoothScroll('a[href="#"]')

$(document).ready(function() {
    $(window).scroll(function(){
        $('nav').toggleClass('scolled', $(this).scrollTop()>760);
    });
});
