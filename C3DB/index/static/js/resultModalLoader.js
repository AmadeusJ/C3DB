/*  */
// Get the modal

function modalRun() {

    var modal = document.getElementById("myModal");

// Get the modal trigger button
    var btn = document.getElementById("show_scatterPlot");

// Get the <span> element that closes the modal
    var span = document.getElementsByClassName("modal-close")[0];

// When the user clicks the button, open the modal
    btn.onclick = function(e) {
        e.stopPropagation();
        e.preventDefault();
        modal.style.display = "block";
    };

// When the user clicks on <span> (x), close the modal
    span.onclick = function(e) {
        e.stopPropagation();
        e.preventDefault();
        modal.style.display = "none";
    };

// When the user clicks anywhere outside of the modal, close it
    /*
    window.onclick = function(event) {
        event.stopPropagation();
        event.preventDefault();

        if (event.target == modal) {
            modal.style.display = "none";
        }
    };
        => This code not working with other 'click' event function !!!!!!!!!!!!!!!!*/
}

