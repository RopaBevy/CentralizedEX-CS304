
// rating 
$("#movies-list").on('click',
                     '.pid-rating',
    function (event) {
        if(!progressive_on) return;

        if( event.target != this) return;
        $(this).closest("td").find("label").css("font-weight","normal");
        $(this).css("font-weight","bold");
        var pid = $(this).closest("[data-pid]").attr("data-pid");
        var stars = $(this).find("[name=stars]").val();
        // references the uid variable set by the template
        rateMovie(tt, stars);
    });

