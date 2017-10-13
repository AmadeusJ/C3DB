var htmlSlider0 = document.getElementById('MW_slider');
noUiSlider.create(htmlSlider0,{
    start : [0, 0],
    connect : true,
    range : {'min': -200, 'max':1000}
});
var inputNumber1 = document.getElementById('id_molweight_min');
var inputNumber2 = document.getElementById('id_molweight_max');
htmlSlider0.noUiSlider.on('update', function(values, handle){
    var value = values[handle];
    if(handle){
        inputNumber2.value = value;
    }else {
        inputNumber1.value = Math.round(value);
    }
});

inputNumber1.addEventListener('change', function(){
   htmlSlider0.noUiSlider.set([this.value, null]);
});

inputNumber2.addEventListener('change', function(){
    htmlSlider0.noUiSlider.set([null, this.value]);
});
///////////////////////////////////////////////////////////
var htmlSlider2 = document.getElementById('ringnum_slider');
noUiSlider.create(htmlSlider2,{
    start : [0, 0],
    connect : true,
    range : {'min': -200, 'max':1000}
});
var inputNumber3 = document.getElementById('id_ringnum_min');
var inputNumber4 = document.getElementById('id_ringnum_max');
htmlSlider2.noUiSlider.on('update', function(values, handle){
    var value = values[handle];
    if(handle){
        inputNumber4.value = value;
    }else {
        inputNumber3.value = Math.round(value);
    }
});

inputNumber3.addEventListener('change', function(){
    htmlSlider2.noUiSlider.set([this.value, null]);
});

inputNumber4.addEventListener('change', function(){
    htmlSlider2.noUiSlider.set([null, this.value]);
});
////////////////////////////////////////////////////////////
var htmlSlider3 = document.getElementById('logp_slider');
noUiSlider.create(htmlSlider3,{
    start : [0, 0],
    connect : true,
    range : {'min': -200, 'max':1000}
});
var inputNumber5 = document.getElementById('id_LogP_min');
var inputNumber6 = document.getElementById('id_LogP_max');
htmlSlider3.noUiSlider.on('update', function(values, handle){
    var value = values[handle];
    if(handle){
        inputNumber6.value = value;
    }else {
        inputNumber5.value = Math.round(value);
    }
});

inputNumber5.addEventListener('change', function(){
    htmlSlider3.noUiSlider.set([this.value, null]);
});

inputNumber6.addEventListener('change', function(){
    htmlSlider3.noUiSlider.set([null, this.value]);
});

//////////////////////////////////////////////////////////////////////
/*$(document).ready(function(){
    $(".chosen-select").chosen({no_results_text: "Sorry, We don't have such datab ;-)"});
});*/


