/*!
* Start Bootstrap - Grayscale v7.0.5 (https://startbootstrap.com/theme/grayscale)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-grayscale/blob/master/LICENSE)
*/
//
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {

    // Navbar shrink function
    var navbarShrink = function () {
        const navbarCollapsible = document.body.querySelector('#mainNav');
        if (!navbarCollapsible) {
            return;
        }
        if (window.scrollY === 0) {
            navbarCollapsible.classList.remove('navbar-shrink')
        } else {
            navbarCollapsible.classList.add('navbar-shrink')
        }

    };

    // Shrink the navbar 
    navbarShrink();

    // Shrink the navbar when page is scrolled
    document.addEventListener('scroll', navbarShrink);

    // Activate Bootstrap scrollspy on the main nav element
    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            offset: 74,
        });
    };

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });

});

// Favorite
$("input[type=submit]").hide();


// delegated event handler
$("#job-list").on('click','i', function (event) {
    $(this).closest('i').css('color','orange');
    var link = $(this).closest('tr').attr('data-pid');
    console.log(link);
    $.post(fav_url, {'link' : link}, updateSingleJob);
});

// for saved list
$("#saved-list").on('click','i', function (event) {
    console.log('clicking recognized');
    $(this).closest('i').css('color','grey');
    var link = $(this).closest('tr').attr('data-pid');
    console.log(link);
    $.post(saved_url, {'link' : link}, updateSingleJob);
});

function updateSingleJob(resp) {
    var link = resp.link;
    console.log('response is',resp);
    // $('[data-tt=' + link + ']').find('.favbutton').value(1);
};


// when loading the page, show which posts are already saved
function revealButtons(){
    var saved = document.getElementById('savelink').value;
    var opp = document.getElementById('intlink').value;
    console.log('Saving:' + saved);
    console.log('Opp: ' + opp);
    if (saved == opp){
        console.log("match");
    }
}