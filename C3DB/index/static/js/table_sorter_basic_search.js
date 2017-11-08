/**
 * Created by JDW on 2017-11-08.
 */
$(function() {

    /*** Bootstrap popover demo ***/
    $('#popover')
        .popover({
            placement: 'right',
            html: true, // required if content has HTML
            content: '<div id="popover-target"></div>'
        })
        // bootstrap popover event triggered when the popover opens
        .on('shown.bs.popover', function () {
            // call this function to copy the column selection code into the popover
            $.tablesorter.columnSelector.attachTo( $('.bootstrap-popup'), '#popover-target');
        });

    // initialize column selector using default settings
    // note: no container is defined!
    $(".bootstrap-popup").tablesorter({
        theme: 'blue',
        widgets: ['zebra', 'columnSelector', 'stickyHeaders']
    }).tablesorterPager({container: $("#pager")});

});
