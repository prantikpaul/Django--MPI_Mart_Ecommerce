
'use strict';
jQuery(document).ready(function ($) {
    $(document).on('click', '.sticky-demo', function (e) {
        e.preventDefault();
        var $this = $(this),
            $iframe = $("#prebuilt-frame"),
            $wrapper = $this.closest('.sticky-demo-wrapper');
        if ('' == $iframe.attr('src')) {
            $iframe.attr('src', 'https://www.portotheme.com/wordpress/porto_landing/demos.html');
            $( '.sticky-prebuilts' ).addClass( 'loading' );
            $iframe.on('load', function (e) {
                $( '.sticky-prebuilts' ).removeClass('loading');
            })
        }
        $wrapper.toggleClass('active');
    });
    $(document).on('click', '.sticky-demo-wrapper.active .sticky-overlay', function (e) {
        e.preventDefault();
        $(this).closest('.sticky-demo-wrapper').removeClass('active');
    });
});