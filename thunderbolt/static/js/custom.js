

$(document).ready(function () {
    'use strict';

    var win = $(window),
        navbar = $('.navbar'),
        scrollUp = $(".scroll-up"),
        sideMenu = $(".side-menu");




    /*========== Start Navbar Auto Change  ==========*/
    win.on('scroll', function () {
        if (win.scrollTop() > 50) {
            navbar.addClass('nav-fixed').removeClass('fixed-top');
        } else {
            navbar.addClass('fixed-top').removeClass('nav-fixed');
        }
    });




    // Sync Navbar Links With Section
    $('body').scrollspy({
        target: '#navtoggler',
        offset: 82
    });
    //// COLLAPSED MENU CLOSE ON CLICK
    // navbar.on('click', '.navbar-collapse', function (e) {
    //     if ($(e.target).is('a')) {
    //         $(this).collapse('hide');
    //     }
    // });



});
