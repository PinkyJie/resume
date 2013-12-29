(function($){
    'use strict';
    function init() {
        $('li.inactive img')
            .mouseenter(function(){
                $(this).removeClass('gray-img');
            })
            .mouseleave(function(){
                $(this).addClass('gray-img');
            });
    }

    $(init);
})(jQuery);
