var htmlSlider0000 = document.getElementById('MW_slider4');
noUiSlider.create(htmlSlider0000,{
    start : [0, 0],
    connect : true,
    range : {'min': -200, 'max':1000}
});
var inputNumber1111 = document.getElementById('id_molweight_min4');
var inputNumber2222 = document.getElementById('id_molweight_max4');
htmlSlider0000.noUiSlider.on('update', function(values, handle){
    var value = values[handle];
    if(handle){
        inputNumber2222.value = value;
    }else {
        inputNumber1111.value = Math.round(value);
    }
});

inputNumber1111.addEventListener('change', function(){
   htmlSlider0000.noUiSlider.set([this.value, null]);
});

inputNumber2222.addEventListener('change', function(){
    htmlSlider0000.noUiSlider.set([null, this.value]);
});
///////////////////////////////////////////////////////////
var htmlSlider2222 = document.getElementById('ringnum_slider4');
noUiSlider.create(htmlSlider2222,{
    start : [0, 0],
    connect : true,
    range : {'min': -200, 'max':1000}
});
var inputNumber3333 = document.getElementById('id_ringnum_min4');
var inputNumber4444= document.getElementById('id_ringnum_max4');
htmlSlider2222.noUiSlider.on('update', function(values, handle){
    var value = values[handle];
    if(handle){
        inputNumber4444.value = value;
    }else {
        inputNumber3333.value = Math.round(value);
    }
});

inputNumber3333.addEventListener('change', function(){
    htmlSlider2222.noUiSlider.set([this.value, null]);
});

inputNumber4444.addEventListener('change', function(){
    htmlSlider2222.noUiSlider.set([null, this.value]);
});
////////////////////////////////////////////////////////////
var htmlSlider3333 = document.getElementById('logp_slider4');
noUiSlider.create(htmlSlider3333,{
    start : [0, 0],
    connect : true,
    range : {'min': -200, 'max':1000}
});
var inputNumber5555 = document.getElementById('id_LogP_min4');
var inputNumber6666 = document.getElementById('id_LogP_max4');
htmlSlider3333.noUiSlider.on('update', function(values, handle){
    var value = values[handle];
    if(handle){
        inputNumber6666.value = value;
    }else {
        inputNumber5555.value = Math.round(value);
    }
});

inputNumber5555.addEventListener('change', function(){
    htmlSlider3333.noUiSlider.set([this.value, null]);
});

inputNumber6666.addEventListener('change', function(){
    htmlSlider3333.noUiSlider.set([null, this.value]);
});

//////////////////////////////////////////////////////////////////////
$(document).ready(function(){
    $(".chzn-select").chosen({no_results_text: "Sorry, We don't have such datab ;-)"});
});
