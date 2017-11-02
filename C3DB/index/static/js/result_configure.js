/* Call & Adjust default result  */
function callingConfiguration(setting) {

    if (setting['MW'] == 1){
        $('.des_mw').prop('checked', true);
    } else {
        $('.des_mw').prop('checked', false);
        $('.result_mw').hide();
    }

    if (setting['Atoms'] == 1){
        $('.des_atom').prop('checked', true);
    } else {
        $('.des_atom').prop('checked', false);
        $('.result_atom').hide();
    }

    if (setting['Bonds'] == 1){
        $('.des_bond').prop('checked', true);
    } else {
        $('.des_bond').prop('checked', false);
        $('.result_bond').hide();
    }

    if (setting['Rings'] == 1){
        $('.des_ring').prop('checked', true);
    } else {
        $('.des_ring').prop('checked', false);
        $('.result_ring').hide();
    }

    if (setting['LogP'] == 1){
        $('.des_logP').prop('checked', true);
    } else {
        $('.des_logP').prop('checked', false);
        $('.result_logP').hide();
    }

    if (setting['Charge'] == 1){
        $('.des_fc').prop('checked', true);
    } else {
        $('.des_fc').prop('checked', false);
        $('.result_fc').hide();
    }

    if (setting['Origin'] == 1){
        $('.des_pub').prop('checked', true);
    } else {
        $('.des_pub').prop('checked', true);
        $('.result_pub').hide();
    }

    if (setting['HBA'] == 1){
        $('.des_hba').prop('checked', true);
    } else {
        $('.des_hba').prop('checked', false);
        $('.result_hba').hide();
    }

    if (setting['HBD'] == 1){
        $('.des_hbd').prop('checked', true);
    } else {
        $('.des_hbd').prop('checked', false);
        $('.result_hbd').hide();
    }

    if (setting['Rotate'] == 1){
        $('.des_rotate').prop('checked', true);
    } else {
        $('.des_rotate').prop('checked', false);
        $('.result_rotate').hide();
    }

    if (setting['Formula'] == 1){
        $('.des_mf').prop('checked', true);
    } else {
        $('.des_mf').prop('checked', false);
        $('.result_mf').hide();
    }

    if (setting['QM'] == 1){
        $('.des_mf').prop('checked', true);
    } else {
        $('.des_mf').prop('checked', false);
        $('.result_mf').hide();
    }

}


function userConfigurationChange() {
    $('.des_mw').change(function (e) {
        e.preventDefault();
        var chk = $(this).is(':checked');
        if (chk){
            $('.result_mw').show();
        } else {
            $('.result_mw').hide();
        }
    });

    $('.des_atom').change(function (e) {
        e.preventDefault();
        var chk = $(this).is(':checked');
        if (chk){
            $('.result_atom').show();
        } else {
            $('.result_atom').hide();
        }
    });

    $('.des_bond').change(function (e) {
        e.preventDefault();
        var chk = $(this).is(':checked');
        if (chk){
            $('.result_bond').show();
        } else {
            $('.result_bond').hide();
        }
    });

    $('.des_ring').change(function (e) {
        e.preventDefault();
        var chk = $(this).is(':checked');
        if (chk){
            $('.result_ring').show();
        } else {
            $('.result_ring').hide();
        }
    });

    $('.des_logP').change(function (e) {
        e.preventDefault();
        var chk = $(this).is(':checked');
        if (chk){
            $('.result_logP').show();
        } else {
            $('.result_logP').hide();
        }
    });

    $('.des_hba').change(function (e) {
        e.preventDefault();
        var chk = $(this).is(':checked');
        if (chk){
            $('.result_hba').show();
        } else {
            $('.result_hba').hide();
        }
    });

    $('.des_hbd').change(function (e) {
        e.preventDefault();
        var chk = $(this).is(':checked');
        if (chk){
            $('.result_hbd').show();
        } else {
            $('.result_hbd').hide();
        }
    });

    $('.des_fc').change(function (e) {
        e.preventDefault();
        var chk = $(this).is(':checked');
        if (chk){
            $('.result_fc').show();
        } else {
            $('.result_fc').hide();
        }
    });

    $('.des_rotate').change(function (e) {
        e.preventDefault();
        var chk = $(this).is(':checked');
        if (chk){
            $('.result_rotate').show();
        } else {
            $('.result_rotate').hide();
        }
    });

    $('.des_mf').change(function (e) {
        e.preventDefault();
        var chk = $(this).is(':checked');
        if (chk){
            $('.result_mf').show();
        } else {
            $('.result_mf').hide();
        }
    });

    $('.des_pub').change(function (e) {
        e.preventDefault();
        var chk = $(this).is(':checked');
        if (chk){
            $('.result_pub').show();
        } else {
            $('.result_pub').hide();
        }
    });

    $('.des_qm').change(function (e) {
        e.preventDefault();
        var chk = $(this).is(':checked');
        if (chk){
            $('.result_qm').show();
        } else {
            $('.result_qm').hide();
        }
    });

}
