//Set the side navbar to stick when a certain point in the page is reached
$(function () {

    var sidebarNav = $("#sidebarNav");

    $('#sidebar').height(sidebarNav.height());

    sidebarNav.affix({
        offset: {top: (sidebarNav.offset().top - ($(window).height() / 3))}
    });
});
