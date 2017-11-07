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
        $('.des_qm').prop('checked', true);
    } else {
        $('.des_qm').prop('checked', false);
        $('.result_qm').hide();
    }

    if (setting['TPSA'] == 1){
        $('.des_tpsa').prop('checked', true);
    } else {
        $('.des_tpsa').prop('checked', false);
        $('.result_tpsa').hide();
    }

    if (setting['Heat'] == 1){
        $('.des_heat').prop('checked', true);
    } else {
        $('.des_heat').prop('checked', false);
        $('.result_heat').hide();
    }

    if (setting['Total_Energy'] == 1){
        $('.des_tt_energy').prop('checked', true);
    } else {
        $('.des_tt_energy').prop('checked', false);
        $('.result_tt_energy').hide();
    }

    if (setting['Elec_Energy'] == 1){
        $('.des_elc_energy').prop('checked', true);
    } else {
        $('.des_elc_energy').prop('checked', false);
        $('.result_elc_energy').hide();
    }

    if (setting['Point_Group'] == 1){
        $('.des_point_group').prop('checked', true);
    } else {
        $('.des_point_group').prop('checked', false);
        $('.result_point_group').hide();
    }

    if (setting['COSMO_Area'] == 1){
        $('.des_COSMO_Area').prop('checked', true);
    } else {
        $('.des_COSMO_Area').prop('checked', false);
        $('.result_COSMO_Area').hide();
    }

    if (setting['COSMO_Volume'] == 1){
        $('.des_COSMO_Volume').prop('checked', true);
    } else {
        $('.des_COSMO_Volume').prop('checked', false);
        $('.result_COSMO_Volume').hide();
    }

    if (setting['Ion_Potential'] == 1){
        $('.des_Ion_Potential').prop('checked', true);
    } else {
        $('.des_Ion_Potential').prop('checked', false);
        $('.result_Ion_Potential').hide();
    }

    if (setting['HOMO'] == 1){
        $('.des_HOMO').prop('checked', true);
    } else {
        $('.des_HOMO').prop('checked', false);
        $('.result_HOMO').hide();
    }

    if (setting['LUMO'] == 1){
        $('.des_LUMO').prop('checked', true);
    } else {
        $('.des_LUMO').prop('checked', false);
        $('.result_LUMO').hide();
    }

    if (setting['Dimension'] == 1){
        $('.des_dimensions').prop('checked', true);
    } else {
        $('.des_dimensions').prop('checked', false);
        $('.result_dimensions').hide();
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

    if ($('.des_atom').is(':checked')){
        $('.result_atom').show();
    } else {
        $('.result_atom').hide();
    }

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

    $('.des_tpsa').change(function (e) {
        e.preventDefault();
        var chk = $(this).is(':checked');
        if (chk){
            $('.result_tpsa').show();
        } else {
            $('.result_tpsa').hide();
        }
    });

    $('.des_heat').change(function (e) {
        e.preventDefault();
        var chk = $(this).is(':checked');
        if (chk){
            $('.result_heat').show();
        } else {
            $('.result_heat').hide();
        }
    });

    $('.des_tt_energy').change(function (e) {
        e.preventDefault();
        var chk = $(this).is(':checked');
        if (chk){
            $('.result_tt_energy').show();
        } else {
            $('.result_tt_energy').hide();
        }
    });

    $('.des_elc_energy').change(function (e) {
        e.preventDefault();
        var chk = $(this).is(':checked');
        if (chk){
            $('.result_elc_energy').show();
        } else {
            $('.result_elc_energy').hide();
        }
    });

    $('.des_point_group').change(function (e) {
        e.preventDefault();
        var chk = $(this).is(':checked');
        if (chk){
            $('.result_point_group').show();
        } else {
            $('.result_point_group').hide();
        }
    });

    $('.des_COSMO_Area').change(function (e) {
        e.preventDefault();
        var chk = $(this).is(':checked');
        if (chk){
            $('.result_COSMO_Area').show();
        } else {
            $('.result_COSMO_Area').hide();
        }
    });
    /*
    $('.des_COSMO_Volume').change(function (e) {
        e.preventDefault();
        var chk = $(this).is(':checked');
        if (chk){
            $('.result_COSMO_Volume').show();
        } else {
            $('.result_COSMO_Volume').hide();
        }
    });
    */
    if ($('.des_COSMO_Volume').is(':checked')){
        $('.result_COSMO_Volume').show();
    } else {
        $('.result_COSMO_Volume').hide();
    }

    $('.des_Ion_Potential').change(function (e) {
        e.preventDefault();
        var chk = $(this).is(':checked');
        if (chk){
            $('.result_Ion_Potential').show();
        } else {
            $('.result_Ion_Potential').hide();
        }
    });

    $('.des_HOMO').change(function (e) {
        e.preventDefault();
        var chk = $(this).is(':checked');
        if (chk){
            $('.result_HOMO').show();
        } else {
            $('.result_HOMO').hide();
        }
    });

    $('.des_LUMO').change(function (e) {
        e.preventDefault();
        var chk = $(this).is(':checked');
        if (chk){
            $('.result_LUMO').show();
        } else {
            $('.result_LUMO').hide();
        }
    });

    $('.des_dimensions').change(function (e) {
        e.preventDefault();
        var chk = $(this).is(':checked');
        if (chk){
            $('.result_dimensions').show();
        } else {
            $('.result_dimensions').hide();
        }
    });

}
