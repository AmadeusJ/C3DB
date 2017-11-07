/* Show & Hiding Pics */
$('#show_all').change(function(){
    var chk = $(this).is(":checked");
    if(chk){
        $('.mol_img').show();

    }else{
        $('.mol_img').hide();
    }
});


/* Selecting all molecules */
$('#select_all').change(function(){
    $('.mol1').prop('checked', $(this).prop("checked"));
});

$('.mol1').change(function(){
    if (false == $(this).prop("checked")){
        $('#select_all').prop('checked', false);
    }
    if ($('.mol1:checked').length == $('.mol1').length){
        $('#select_all').prop('checked', true);
    }
});


$('.first').on('click', function () {
    var chk = $('#show_all').is(":checked");
    if (chk)
        $('.mol_img').hide();
        $('.mol1').prop('checked', false);

    $('#show_all').attr("checked", false);
    $('#select_all').prop('checked', false);

});

$('.prev').on('click', function () {
    var chk = $('#show_all').is(":checked");
    if (chk)
        $('.mol_img').hide();
        $('.mol1').prop('checked', false);

    $('#show_all').attr("checked", false);
    $('#select_all').prop('checked', false);
});

$('.next').on('click', function () {
    var chk = $('#show_all').is(":checked");
    if (chk)
        $('.mol_img').hide();
        $('.mol1').prop('checked', false);

    $('#show_all').attr("checked", false);
    $('#select_all').prop('checked', false);
});

$('.last').on('click', function () {
    var chk = $('#show_all').is(":checked");
    if (chk)
        $('.mol_img').hide();
        $('.mol1').prop('checked', false);

    $('#show_all').attr("checked", false);
    $('#select_all').prop('checked', false);
});
