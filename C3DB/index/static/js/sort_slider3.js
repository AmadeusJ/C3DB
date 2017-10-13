var htmlSlider000 = document.getElementById('MW_slider3');
noUiSlider.create(htmlSlider000,{
    start : [0, 0],
    connect : true,
    range : {'min': -200, 'max':1000}
});
var inputNumber111 = document.getElementById('id_molweight_min3');
var inputNumber222 = document.getElementById('id_molweight_max3');
htmlSlider000.noUiSlider.on('update', function(values, handle){
    var value = values[handle];
    if(handle){
        inputNumber222.value = value;
    }else {
        inputNumber111.value = Math.round(value);
    }
});

inputNumber111.addEventListener('change', function(){
   htmlSlider000.noUiSlider.set([this.value, null]);
});

inputNumber222.addEventListener('change', function(){
    htmlSlider000.noUiSlider.set([null, this.value]);
});
///////////////////////////////////////////////////////////
var htmlSlider222 = document.getElementById('ringnum_slider3');
noUiSlider.create(htmlSlider222,{
    start : [0, 0],
    connect : true,
    range : {'min': -200, 'max':1000}
});
var inputNumber333 = document.getElementById('id_ringnum_min3');
var inputNumber444 = document.getElementById('id_ringnum_max3');
htmlSlider222.noUiSlider.on('update', function(values, handle){
    var value = values[handle];
    if(handle){
        inputNumber444.value = value;
    }else {
        inputNumber333.value = Math.round(value);
    }
});

inputNumber333.addEventListener('change', function(){
    htmlSlider222.noUiSlider.set([this.value, null]);
});

inputNumber444.addEventListener('change', function(){
    htmlSlider222.noUiSlider.set([null, this.value]);
});
////////////////////////////////////////////////////////////
var htmlSlider333 = document.getElementById('logp_slider3');
noUiSlider.create(htmlSlider333,{
    start : [0, 0],
    connect : true,
    range : {'min': -200, 'max':1000}
});
var inputNumber555 = document.getElementById('id_LogP_min3');
var inputNumber666 = document.getElementById('id_LogP_max3');
htmlSlider333.noUiSlider.on('update', function(values, handle){
    var value = values[handle];
    if(handle){
        inputNumber666.value = value;
    }else {
        inputNumber555.value = Math.round(value);
    }
});

inputNumber555.addEventListener('change', function(){
    htmlSlider333.noUiSlider.set([this.value, null]);
});

inputNumber666.addEventListener('change', function(){
    htmlSlider333.noUiSlider.set([null, this.value]);
});

//////////////////////////////////////////////////////////////////////
$(document).ready(function(){
    $(".chzn-select").chosen({no_results_text: "Sorry, We don't have such datab ;-)"});
});
