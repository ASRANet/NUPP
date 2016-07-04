window.onload = function(){
    checkKeyDeadlines();
};

//Check if date of key deadlines has passed and update HTML and progress bar as required
function checkKeyDeadlines() {

    var keyDeadlines = [{event: "Deadline for abstracts", textDate: $("#abstractDeadline").text()},
        {event: "Notification of acceptance", textDate: $("#acceptanceDeadline").text()},
        {event: "Submission of full papers", textDate: $("#papersDeadline").text()},
        {event: "Registration closes", textDate: $("#registrationDeadline").text()}];
    var months = ["Jan.", "Feb.", "Mar.", "Apr.", "May", "June", "July", "Aug.", "Sept.", "Oct.", "Nov.", "Dec."];
    var currentDate = new Date();
    var day = currentDate.getDate();
    var month = currentDate.getMonth();
    var year = currentDate.getFullYear();
    var lastDeadline = -1;
    var lastDeadlineChanged = false;
    var newHTML = "<tr>";

    for (var index =  0; index < keyDeadlines.length; index++) {

        lastDeadlineChanged = false;
        var newDate = keyDeadlines[index].textDate.split(" ");

        if (newDate[2] < year) {
            lastDeadline = index;
            lastDeadlineChanged = true;
        }

        else if (newDate[2] == year) {
            if (months.indexOf(newDate[0]) < month) {
                lastDeadline = index;
                lastDeadlineChanged = true;
            }

            else if (months.indexOf(newDate[0]) == month) {

                if (newDate[1].replace(",", "") < day) {
                    lastDeadline = index;
                    lastDeadlineChanged = true;
                }

            }

        }

        if(lastDeadlineChanged){
            newHTML += "<td><del>" + keyDeadlines[index].event + "</del><br><del>" + keyDeadlines[index].textDate + "</del></td>";
        }
        else{
            newHTML += "<td><p>" + keyDeadlines[index].event + "<br>" + keyDeadlines[index].textDate + "</p></td>";
        }

    }

    var newProgress = (lastDeadline + 1) * (100 / keyDeadlines.length);
    $("#datesProgress").css('width', newProgress +'%').attr('aria-valuenow', newProgress);

    newHTML += "</tr>";
    $("#keyDeadlinesTable").html(newHTML);

}
