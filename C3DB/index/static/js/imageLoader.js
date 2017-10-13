/* Change ssu_cid format
* eg. ssu_cid = '1'
* ===> ssu_cid = '000000001'
* ===> ssu_cid = '00034561' */

function addZero(ssu_cid){
    var final_num = "";
    var num = ssu_cid.toString();
    var num_len = ssu_cid.toString().length;

    if (num_len === 1){
        for (var a = 0; final_num.length < 8; a++ ) {
            final_num += "0";
        }
        final_num += num;
    } else if (num_len === 2) {
        for (var b = 0; final_num.length < 7; b++){
            final_num += "0";
        }
        final_num += num;
    } else if (num_len === 3) {
        for (var c = 0; final_num.length < 6; c++){
            final_num += "0";
        }
        final_num += num;
    } else if (num_len === 4) {
        for (var d = 0; final_num.length < 5; d++) {
            final_num += "0";
        }
        final_num += num;
    } else if (num_len === 5) {
        for (var e = 0; final_num.length < 4; e++) {
            final_num += "0";
        }
        final_num += num;
    } else if (num_len === 6) {
        for (var f = 0; final_num.length < 3; f++) {
            final_num += "0";
        }
        final_num += num;
    } else if (num_len === 7) {
        for (var g = 0; final_num.length < 2; g++) {
            final_num += "0";
        }
        final_num += num;
    } else if (num_len === 8) {
        for (var h = 0; final_num.length < 1; h++) {
            final_num += "0";
        }
        final_num += num;
    }

    return final_num;
}