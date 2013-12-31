(function($){
    'use strict';
    function init() {
        // chinese/english switch
        $('li.inactive img')
            .mouseenter(function(){
                $(this).removeClass('gray-img');
            })
            .mouseleave(function(){
                $(this).addClass('gray-img');
            });
        // affix navbar
        $(window).scroll(function(){
            var navAnchor = $('.cv-title').offset().top;
            if ($(this).scrollTop() > navAnchor) {
                $('.nav').addClass('splited');
            } else if ($(this).scrollTop() < navAnchor) {
                $('.nav').removeClass('splited');
            }
        });
        // navbar slide
        $('ul.nav a').click(function(e){
            e.preventDefault();
            slideToElement($(this).attr('href'));
            // apply to select nav
            $('select.nav').val($(this).attr('href'));
        });
        $('select.nav').change(function(){
            slideToElement($(this).val());
        });
        function slideToElement(ele) {
            $('html, body').stop().animate({
                scrollTop: $(ele).offset().top - 30
            }, 1500, 'easeInOutExpo');
        }
    }

    $(init);
})(jQuery);
