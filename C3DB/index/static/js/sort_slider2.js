var htmlSlider00 = document.getElementById('MW_slider2');
noUiSlider.create(htmlSlider00,{
    start : [0, 0],
    connect : true,
    range : {'min': -200, 'max':1000}
});
var inputNumber11 = document.getElementById('id_molweight_min2');
var inputNumber22 = document.getElementById('id_molweight_max2');
htmlSlider00.noUiSlider.on('update', function(values, handle){
    var value = values[handle];
    if(handle){
        inputNumber22.value = value;
    }else {
        inputNumber11.value = Math.round(value);
    }
});

inputNumber11.addEventListener('change', function(){
   htmlSlider00.noUiSlider.set([this.value, null]);
});

inputNumber22.addEventListener('change', function(){
    htmlSlider00.noUiSlider.set([null, this.value]);
});
///////////////////////////////////////////////////////////
var htmlSlider22 = document.getElementById('ringnum_slider2');
noUiSlider.create(htmlSlider22,{
    start : [0, 0],
    connect : true,
    range : {'min': -200, 'max':1000}
});
var inputNumber33 = document.getElementById('id_ringnum_min2');
var inputNumber44 = document.getElementById('id_ringnum_max2');
htmlSlider22.noUiSlider.on('update', function(values, handle){
    var value = values[handle];
    if(handle){
        inputNumber44.value = value;
    }else {
        inputNumber33.value = Math.round(value);
    }
});

inputNumber33.addEventListener('change', function(){
    htmlSlider22.noUiSlider.set([this.value, null]);
});

inputNumber44.addEventListener('change', function(){
    htmlSlider22.noUiSlider.set([null, this.value]);
});
////////////////////////////////////////////////////////////
var htmlSlider33 = document.getElementById('logp_slider2');
noUiSlider.create(htmlSlider33,{
    start : [0, 0],
    connect : true,
    range : {'min': -200, 'max':1000}
});
var inputNumber55= document.getElementById('id_LogP_min2');
var inputNumber66 = document.getElementById('id_LogP_max2');
htmlSlider33.noUiSlider.on('update', function(values, handle){
    var value = values[handle];
    if(handle){
        inputNumber66.value = value;
    }else {
        inputNumber55.value = Math.round(value);
    }
});

inputNumber55.addEventListener('change', function(){
    htmlSlider33.noUiSlider.set([this.value, null]);
});

inputNumber66.addEventListener('change', function(){
    htmlSlider33.noUiSlider.set([null, this.value]);
});

//////////////////////////////////////////////////////////////////////
$(document).ready(function(){
    $(".chzn-select").chosen({no_results_text: "Sorry, We don't have such datab ;-)"});
});
