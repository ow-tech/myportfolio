// $(document).ready(function() {
    $(window).scroll(function(){
        $('nav').toggleClass('scolled', $(this).scrollTop()>760);
    });
// });