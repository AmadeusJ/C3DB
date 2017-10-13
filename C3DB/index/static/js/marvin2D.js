/**
 * Created by use on 2016-09-19.
 */
    /* This is for the molecule 2D sketcher...!!! */
var marvinController,
    inputController;

$(document).ready(function handleDocumentReady (e) {
    MarvinJSUtil.getEditor("#sketch").then(function (sketcherInstance) {

        marvinController = new MarvinControllerClass(
            sketcherInstance,
            $("#chbx-coloring"),
            $("#chbx-map"),
            $("#chbx-carbonVis")
        );

        inputController = new InputControllerClass(
            $("#btn-setMdlmolfile"),
            $("#btn-paste"),
            $("#list-inputformat"),
            $("#btn-clearTxt"),
            $("#btn-molExport"),
            $("#molsource-box")
        );

    }, function () {
        alert("Cannot retrieve sketcher instance from iframe");
    });

    $("#molsource-box").val(caffeineSource);
});

/* The first Class ! */
var InputControllerClass = (function () {

    var delay = 5;

    function InputControllerClass ( importButton,
                                    pasteButton,
                                    formatDropdown,
                                    resetButton,
                                    molExportButton,
                                    srcTextBox ) {

        this.importButton		= importButton;
        this.pasteButton		= pasteButton;
        this.formatDropdown		= formatDropdown;
        this.resetButton		= resetButton;
        this.molExportButton	= molExportButton;
        this.srcTextBox 		= srcTextBox;
        this.init();
    }

    InputControllerClass.prototype.init = function init () {
        this.importButton.on("click", $.proxy(this.handleImportBtnClick, this));
        this.pasteButton.on("click", $.proxy(this.handlePasteBtnClick, this));
        this.resetButton.on("click", $.proxy(this.clearTxt, this));
        this.molExportButton.on("click", $.proxy(this.handleMolExportBtnClick, this));
    };

    InputControllerClass.prototype.handleImportBtnClick = function handleImportBtnClick (e) {
        this.delayCall(importMolAction, [this.getTxt(), this.getFormat()]);
    };

    InputControllerClass.prototype.handlePasteBtnClick = function handleImportBtnClick (e) {
        this.delayCall(pasteMolAction, [this.getTxt(), this.getFormat()]);
    };

    InputControllerClass.prototype.handleMolExportBtnClick = function handleMolExportBtnClick (e) {
        this.delayCall(exportMolAction, [this.getFormat()]);
    };



    InputControllerClass.prototype.delayCall = function delayCall (method, args) {
        setTimeout(function () {
            method.apply(null, args);
        }, delay);
    };

    InputControllerClass.prototype.getTxt = function getTxt () {
        return this.srcTextBox.val();
    };

    InputControllerClass.prototype.setTxt = function setTxt (txt) {
        this.srcTextBox.val(txt);
    };

    InputControllerClass.prototype.clearTxt = function clearTxt () {
        this.setTxt("");
    };

    InputControllerClass.prototype.getFormat = function getFormat (e) {
        return this.formatDropdown.val();
    };

    return InputControllerClass;

}());
/* The Second Class */
var MarvinControllerClass = (function () {

    function MarvinControllerClass ( sketcherInstance, cpkCheckbox, mapCheckbox, carbonCheckbox) {
        this.sketcherInstance 	= sketcherInstance;
        this.cpkCheckbox 		= cpkCheckbox;
        this.mapCheckbox 		= mapCheckbox;
        this.carbonCheckbox 	= carbonCheckbox;
        this.init();
    }

    MarvinControllerClass.prototype.init = function init () {
        this.carbonCheckbox.on("change", $.proxy(this.handleCarbonCheckBoxChange, this));
        this.mapCheckbox.on("change", $.proxy(this.handleMapCheckBoxChange, this));
        this.cpkCheckbox.on("change", $.proxy(this.handleCpkCheckBoxChange, this));
    };

    MarvinControllerClass.prototype.handleCarbonCheckBoxChange = function handleCarbonCheckBoxChange (e) {
        this.sketcherInstance.setDisplaySettings({
            "carbonLabelVisible" : this.carbonCheckbox.is(':checked')
        });
    };

    MarvinControllerClass.prototype.handleMapCheckBoxChange = function handleMapCheckBoxChange (e) {
        this.sketcherInstance.setDisplaySettings({
            "atomMapsVisible" : this.mapCheckbox.is(':checked')
        });
    };

    MarvinControllerClass.prototype.handleCpkCheckBoxChange = function handleCpkCheckBoxChange (e) {
        this.sketcherInstance.setDisplaySettings({
            "cpkColoring" : this.cpkCheckbox.is(':checked')
        });
    };

    return MarvinControllerClass;

}());

var caffeineSource = 	"\n\n\n"+
    " 14 15  0  0  0  0  0  0  0  0999 V2000\n"+
    "    0.5089    7.8316    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0\n"+
    "    1.2234    6.5941    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0\n"+
    "    1.2234    7.4191    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0\n"+
    "   -0.2055    6.5941    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0\n"+
    "   -0.9200    7.8316    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0\n"+
    "    0.5089    5.3566    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0\n"+
    "   -0.2055    7.4191    0.0000 N   0  0  0  0  0  0  0  0  0  0  0  0\n"+
    "    0.5089    6.1816    0.0000 N   0  0  0  0  0  0  0  0  0  0  0  0\n"+
    "   -0.9200    6.1816    0.0000 O   0  0  0  0  0  0  0  0  0  0  0  0\n"+
    "    0.5089    8.6566    0.0000 O   0  0  0  0  0  0  0  0  0  0  0  0\n"+
    "    2.4929    7.0066    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0\n"+
    "    2.0080    7.6740    0.0000 N   0  0  0  0  0  0  0  0  0  0  0  0\n"+
    "    2.0080    6.3391    0.0000 N   0  0  0  0  0  0  0  0  0  0  0  0\n"+
    "    2.2630    8.4586    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0\n"+
    "  1  7  1  0  0  0  0\n"+
    "  8  2  1  0  0  0  0\n"+
    "  1  3  1  0  0  0  0\n"+
    "  2  3  2  0  0  0  0\n"+
    "  7  4  1  0  0  0  0\n"+
    "  4  8  1  0  0  0  0\n"+
    "  4  9  2  0  0  0  0\n"+
    "  7  5  1  0  0  0  0\n"+
    "  8  6  1  0  0  0  0\n"+
    "  1 10  2  0  0  0  0\n"+
    "  3 12  1  0  0  0  0\n"+
    "  2 13  1  0  0  0  0\n"+
    " 13 11  2  0  0  0  0\n"+
    " 12 11  1  0  0  0  0\n"+
    " 12 14  1  0  0  0  0\n"+
    "M  END\n";

function pasteMolAction (txt, format) {
    var pastePromise = marvinController.sketcherInstance.pasteStructure(format, txt);
    pastePromise.then(function() {}, function(error) {
        alert(error);
    });
}

function importMolAction (txt, format) {
    var importPromise = marvinController.sketcherInstance.importStructure(format, txt);
    importPromise.then(function() {}, function(error) {
        alert(error);
    });
}

function exportMolAction (format) {
    var ic = inputController;

    var exportPromise = marvinController.sketcherInstance.exportStructure(format, null);
    exportPromise.then(function(source) {
        ic.setTxt(source);
    }, function(error) {
        ic.setTxt(error);
    });
}
