(function($){
    'use strict';
    function init() {
        // for chinese/english switch
        $('li.inactive img')
            .mouseenter(function(){
                $(this).removeClass('gray-img');
            })
            .mouseleave(function(){
                $(this).addClass('gray-img');
            });
        // for affix navbar
        $(window).scroll(function(){
            var navAnchor = $('.cv-title').offset().top;
            if ($(this).scrollTop() > navAnchor && $('.nav').css('position') !== 'fixed') {
                $('.nav').css({
                    'position': 'fixed',
                    'top': '-1px'
                }).addClass('splited');
            } else if ($(this).scrollTop() < navAnchor && $('.nav').css('position') !== 'relative') {
                $('.nav').css({
                    'position': 'relative'
                }).removeClass('splited');
            }
        });
    }

    $(init);
})(jQuery);
