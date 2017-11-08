/**
 * Created by JDW on 2017-11-08.
 */
$(function() {

    /*** custom css only button popup ***/
    $(".custom-popup").tablesorter({
        theme: 'blue',
        widgets: ['zebra', 'columnSelector', 'stickyHeaders'],
        widgetOptions : {
            // target the column selector markup
            columnSelector_container : $('#columnSelector'),
            // column status, true = display, false = hide
            // disable = do not display on list
            columnSelector_columns : {
                0: 'disable' /* set to disabled; not allowed to unselect it */
            },
            // remember selected columns (requires $.tablesorter.storage)
            columnSelector_saveColumns: true,

            // container layout
            columnSelector_layout : '<label><input type="checkbox">{name}</label>',
            // layout customizer callback called for each column
            // function($cell, name, column){ return name || $cell.html(); }
            columnSelector_layoutCustomizer : null,
            // data attribute containing column name to use in the selector container
            columnSelector_name  : 'data-selector-name',

            /* Responsive Media Query settings */
            // enable/disable mediaquery breakpoints
            columnSelector_mediaquery: true,
            // toggle checkbox name
            columnSelector_mediaqueryName: 'Auto: ',
            // breakpoints checkbox initial setting
            columnSelector_mediaqueryState: true,
            // hide columnSelector false columns while in auto mode
            columnSelector_mediaqueryHidden: true,

            // set the maximum and/or minimum number of visible columns; use null to disable
            columnSelector_maxVisible: null,
            columnSelector_minVisible: null,
            // responsive table hides columns with priority 1-6 at these breakpoints
            // see http://view.jquerymobile.com/1.3.2/dist/demos/widgets/table-column-toggle/#Applyingapresetbreakpoint
            // *** set to false to disable ***
            columnSelector_breakpoints : [ '20em', '30em', '40em', '50em', '60em', '70em' ],
            // data attribute containing column priority
            // duplicates how jQuery mobile uses priorities:
            // http://view.jquerymobile.com/1.3.2/dist/demos/widgets/table-column-toggle/
            columnSelector_priority : 'data-priority',

            // class name added to checked checkboxes - this fixes an issue with Chrome not updating FontAwesome
            // applied icons; use this class name (input.checked) instead of input:checked
            columnSelector_cssChecked : 'checked',

            // class name added to rows that have a span (e.g. grouping widget & other rows inside the tbody)
            columnSelector_classHasSpan : 'hasSpan',

            // event triggered when columnSelector completes
            columnSelector_updated : 'columnUpdate',

            // ** NOTE: All default ajax options have been removed from this demo,
            // see the example-widget-pager-ajax demo for a full list of pager
            // options

            // css class names that are added
            pager_css: {
                container   : 'tablesorter-pager',    // class added to make included pager.css file work
                errorRow    : 'tablesorter-errorRow', // error information row (don't include period at beginning); styled in theme file
                disabled    : 'disabled'              // class added to arrows @ extremes (i.e. prev/first arrows "disabled" on first page)
            },

            // jQuery selectors
            pager_selectors: {
                container   : '.pager',       // target the pager markup (wrapper)
                first       : '.first',       // go to first page arrow
                prev        : '.prev',        // previous page arrow
                next        : '.next',        // next page arrow
                last        : '.last',        // go to last page arrow
                gotoPage    : '.gotoPage',    // go to page selector - select dropdown that sets the current page
                pageDisplay : '.pagedisplay', // location of where the "output" is displayed
                pageSize    : '.pagesize'     // page size selector - select dropdown that sets the "size" option
            },

            // output default: '{page}/{totalPages}'
            // possible variables: {size}, {page}, {totalPages}, {filteredPages}, {startRow}, {endRow}, {filteredRows} and {totalRows}
            // also {page:input} & {startRow:input} will add a modifiable input in place of the value
            pager_output: '{startRow:input} – {endRow} / {totalRows} rows', // '{page}/{totalPages}'

            // apply disabled classname to the pager arrows when the rows at either extreme is visible
            pager_updateArrows: true,

            // starting page of the pager (zero based index)
            pager_startPage: 0,

            // Reset pager to this page after filtering; set to desired page number
            // (zero-based index), or false to not change page at filter start
            pager_pageReset: 0,

            // Number of visible rows
            pager_size: 10,

            // f true, child rows will be counted towards the pager set size
            pager_countChildRows: false,

            // Save pager page & size if the storage script is loaded (requires $.tablesorter.storage in jquery.tablesorter.widgets.js)
            pager_savePages: true,

            // Saves tablesorter paging to custom key if defined. Key parameter name
            // used by the $.tablesorter.storage function. Useful if you have
            // multiple tables defined
            pager_storageKey: "tablesorter-pager",

            // if true, the table will remain the same height no matter how many records are displayed. The space is made up by an empty
            // table row set to a height to compensate; default is false
            pager_fixedHeight: true,

            // remove rows from the table to speed up the sort of large tables.
            // setting this to false, only hides the non-visible rows; needed if you plan to add/remove rows with the pager enabled.
            pager_removeRows: false // removing rows in larger tables speeds up the sort

        }
    }).tablesorterPager({container: $("#pager")});
    

});