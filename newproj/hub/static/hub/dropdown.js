$(document).ready(function(){
    $(".dropbtn").click(function(){
        $(".dropdown-content").fadeToggle("fast");
    });

    // Close the dropdown if the user clicks outside of it
    $(window).click(function(e) {
        if (!e.target.matches('.dropbtn')) {
            $(".dropdown-content").fadeOut("fast");
        }
    });
});
