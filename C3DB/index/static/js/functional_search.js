/**
 * Created by jamadeus on 2017. 6. 11..
 */
/* Functional groups image Live search */
(function(){
    var $imgs = $('img');
    var $search = $('#fc-search-query');
    var cache = [];

    $imgs.each(function(){
        cache.push({
            element: this,
            text: this.alt.trim().toLowerCase()
        });
    });

    function filter(){
        var query = this.value.trim().toLowerCase();
        cache.forEach(function(img){
            var index = 0;
            if (query) {
                index = img.text.indexOf(query);
            }

            img.element.style.display = index === -1 ? 'none' : '';
        });
    }

    if ('oninput' in $search[0]){
        $search.on('input', filter);
    } else {
        $search.on('keyup', filter);
    }
}());



/* SMARTS query write & remove */
$(function(){

    var query = $('#fc-smarts-query').val();

    /* Remove  */
    $("#smarts-reset").on('click', function(){
        $('#fc-smarts-query').val("");
        delete query
        query = $('#fc-smarts-query').val();
    });

    // Acyl Halide
    $("#acyl_halide").on("click", function(){
        if (query !== ""){
            query += '.[CX3](=[OX1])[F,Cl,Br,I]';
            $("#fc-smarts-query").val(query);
        } else {
            query += '[CX3](=[OX1])[F,Cl,Br,I]';
            $("#fc-smarts-query").val(query);
        }
    });

    // Aldehyde
    $('#aldehyde').on("click", function(){
        if (query !== ""){
            query += '.[CX3H1](=O)[#6]';
            $("#fc-smarts-query").val(query);
        } else {
            query += '[CX3H1](=O)[#6]';
            $("#fc-smarts-query").val(query);
        }
    });

    // Amide
    $('#amide').on("click", function(){
        if (query !== ""){
            query += '.[NX3][CX3](=[OX1])[#6]';
            $("#fc-smarts-query").val(query);
        } else {
            query += '[NX3][CX3](=[OX1])[#6]';
            $("#fc-smarts-query").val(query);
        }
    });

    // Carbamate
    $('#carbamate').on('click', function(){
        if (query !== ""){
            query += '.[NX3,NX4+][CX3](=[OX1])[OX2,OX1-]';
            $("#fc-smarts-query").val( query);
        } else {
            query += '[NX3,NX4+][CX3](=[OX1])[OX2,OX1-]';
            $("#fc-smarts-query").val(query);
        }
    });

    // Carbamic acid
    $('#carbamic_acid').on('click', function(){
        if (query !== ""){
            query += '.[NX3,NX4+][CX3](=[OX1])[OX2H,OX1-]';
            $("#fc-smarts-query").val(query);
        } else {
            query += '[NX3,NX4+][CX3](=[OX1])[OX2H,OX1-]';
            $("#fc-smarts-query").val(query);
        }
    });

    // Carbonic acid
    $('#carbonic_acid').on('click', function(){
        if (query !== ""){
            query += '.[CX3](=[OX1])(O)O';
            $("#fc-smarts-query").val(query);
        } else {
            query += '[CX3](=[OX1])(O)O';
            $("#fc-smarts-query").val(query);
        }
    });

    // Carboxylic acid
    $('#carboxylic_acid').on('click', function(){
        if (query !== ""){
            query += '.[CX3](=O)[OX2H1]';
            $("#fc-smarts-query").val( query);
        } else {
            query += '[CX3](=O)[OX2H1]';
            $("#fc-smarts-query").val(query);
        }
    });

    // Ether
    $('#ether').on('click', function(){
        if (query !== ""){
            query += '.[OD2]([#6])[#6]';
            $("#fc-smarts-query").val(query);
        } else {
            query += '[OD2]([#6])[#6]';
            $("#fc-smarts-query").val(query);
        }
    });

    // Ester
    $('#ester').on('click', function(){
        if (query !== ""){
            query += '.[#6][CX3](=O)[OX2H0][#6]';
            $("#fc-smarts-query").val(query);
        } else {
            query += '[#6][CX3](=O)[OX2H0][#6]';
            $("#fc-smarts-query").val(query);
        }
    });

    // Keton
    $('#keton').on('click', function(){
        if (query !== ""){
            query += '.[#6][CX3](=O)[#6]';
            $("#fc-smarts-query").val(query);
        } else {
            query += '[#6][CX3](=O)[#6]';
            $("#fc-smarts-query").val(query);
        }
    });

    // Amidine
    $('#amidine').on('click', function(){
        if (query !== ""){
            query += '.[#6][CX3](=O)[#6]';
            $("#fc-smarts-query").val(query);
        } else {
            query += '[#6][CX3](=O)[#6]';
            $("#fc-smarts-query").val(query);
        }
    });

    // Cyanamide
    $('#cyanamide').on('click', function(){
        if (query !== ""){
            query += '.[NX3][CX2]#[NX1]';
            $("#fc-smarts-query").val(query);
        } else {
            query += '[NX3][CX2]#[NX1]';
            $("#fc-smarts-query").val(query);
        }
    });

    // Amine
    $('#amine').on('click', function(){
        if (query !== ""){
            query += '.[NX3;H2,H1;!$(NC=O)]';
            $("#fc-smarts-query").val( query);
        } else {
            query += '[NX3;H2,H1;!$(NC=O)]';
            $("#fc-smarts-query").val(query);
        }
    });

    // Enamine
    $('#enamine').on('click', function(){
        if (query !== ""){
            query += '.[NX3][CX3]=[CX3]';
            $("#fc-smarts-query").val(query);
        } else {
            query += '[NX3][CX3]=[CX3]';
            $("#fc-smarts-query").val(query);
        }
    });

    // Amino acid
    $('#amino_acid').on('click', function(){
        if (query !== ""){
            query += '.[$([NX3H2,NX4H3+]),$([NX3H](C)(C))][CX4H]([*])[CX3](=[OX1])[OX2H,OX1-,N]';
            $("#fc-smarts-query").val(query);
        } else {
            query += '[$([NX3H2,NX4H3+]),$([NX3H](C)(C))][CX4H]([*])[CX3](=[OX1])[OX2H,OX1-,N]';
            $("#fc-smarts-query").val(query);
        }
    });

    // Azide
    $('#azide').on('click', function(){
        if (query !== ""){
            query += '.[$(*-[NX2-]-[NX2+]#[NX1]),$(*-[NX2]=[NX2+]=[NX1-])]';
            $("#fc-smarts-query").val(query);
        } else {
            query += '[$(*-[NX2-]-[NX2+]#[NX1]),$(*-[NX2]=[NX2+]=[NX1-])]';
            $("#fc-smarts-query").val(query);
        }
    });

    // Azo Nitrogen
    $('#azo_nitrogen').on('click', function(){
        if (query !== ""){
            query += '.[$([NX2]=[NX3+]([O-])[#6]),$([NX2]=[NX3+0](=[O])[#6])]';
            $("#fc-smarts-query").val(query);
        } else {
            query += '[$([NX2]=[NX3+]([O-])[#6]),$([NX2]=[NX3+0](=[O])[#6])]';
            $("#fc-smarts-query").val(query);
        }
    });

    // Azole
    $('#azole').on('click', function(){
        if (query !== ""){
            query += '.[$([nr5]:[nr5,or5,sr5]),$([nr5]:[cr5]:[nr5,or5,sr5])]';
            $("#fc-smarts-query").val(query);
        } else {
            query += '[$([nr5]:[nr5,or5,sr5]),$([nr5]:[cr5]:[nr5,or5,sr5])]';
            $("#fc-smarts-query").val(query);
        }
    });

    // Hydrazone
    $('#hydrazone').on('click', function(){
        if (query !== ""){
            query += '.[NX3][NX2]=[*]';
            $("#fc-smarts-query").val(query);
        } else {
            query += '[NX3][NX2]=[*]';
            $("#fc-smarts-query").val(query);
        }
    });

    // Imine
    $('#imine').on('click', function(){
        if (query !== ""){
            query += '.[CX3;$([C]([#6])[#6]),$([CH][#6])]=[NX2][#6]';
            $("#fc-smarts-query").val(query);
        } else {
            query += '[CX3;$([C]([#6])[#6]),$([CH][#6])]=[NX2][#6]';
            $("#fc-smarts-query").val(query);
        }
    });

    // Imide
    $('#imide').on('click', function(){
        if (query !== ""){
            query += '.[CX3](=[OX1])[NX3H0]([#6])[CX3](=[OX1])';
            $("#fc-smarts-query").val(query);
        } else {
            query += '[CX3](=[OX1])[NX3H0]([#6])[CX3](=[OX1])';
            $("#fc-smarts-query").val(query);
        }
    });

    // Nitrate
    $('#nitrate').on('click', function(){
        if (query !== ""){
            query += '.[$([NX3](=[OX1])(=[OX1])O),$([NX3+]([OX1-])(=[OX1])O)]';
            $("#fc-smarts-query").val(query);
        } else {
            query += '[$([NX3](=[OX1])(=[OX1])O),$([NX3+]([OX1-])(=[OX1])O)]';
            $("#fc-smarts-query").val(query);
        }
    });

    // Nitrile
    $('#nitrile').on('click', function(){
        if (query !== ""){
            query += '.[NX1]#[CX2]';
            $("#fc-smarts-query").val(query);
        } else {
            query += '[NX1]#[CX2]';
            $("#fc-smarts-query").val(query);
        }
    });

    // Nitro
    $('#nitro').on('click', function(){
        if (query !== ""){
            query += '.[$([NX3](=O)=O),$([NX3+](=O)[O-])][!#8]';
            $("#fc-smarts-query").val(query);
        } else {
            query += '[$([NX3](=O)=O),$([NX3+](=O)[O-])][!#8]';
            $("#fc-smarts-query").val(query);
        }
    });

    // Nitroso
    $('#nitroso').on('click', function(){
        if (query !== ""){
            query += '.[NX2]=[OX1]';
            $("#fc-smarts-query").val(query);
        } else {
            query += '[NX2]=[OX1]';
            $("#fc-smarts-query").val(query);
        }
    });

    // Hydroxyl
    $('#hydroxyl').on('click', function(){
        if (query !== ""){
            query += '.[OX2H]';
            $("#fc-smarts-query").val(query);
        } else {
            query += '[OX2H]';
            $("#fc-smarts-query").val(query);
        }
    });

    // Phenol
    $('#phenol').on('click', function(){
        if (query !== ""){
            query += '.[OX2H][cX3]:[c]';
            $("#fc-smarts-query").val(query);
        } else {
            query += '[OX2H][cX3]:[c]';
            $("#fc-smarts-query").val(query);
        }
    });

    // Peroxide
    $('#peroxide').on('click', function(){
        if (query !== ""){
            query += '.[OX2,OX1-][OX2,OX1-]';
            $("#fc-smarts-query").val(query);
        } else {
            query += '[OX2,OX1-][OX2,OX1-]';
            $("#fc-smarts-query").val(query);
        }
    });

    // Phosphoric Acid
    $('#phosphoric_acid').on('click', function(){
        if (query !== ""){
            query += '.[$(P(=[OX1])([$([OX2H]),$([OX1-]),$([OX2]P)])([$([OX2H]),$([OX1-]),$([OX2]P)])';
            $("#fc-smarts-query").val(query);
        } else {
            query += '[$(P(=[OX1])([$([OX2H]),$([OX1-]),$([OX2]P)])([$([OX2H]),$([OX1-]),$([OX2]P)])';
            $("#fc-smarts-query").val(query);
        }
    });

    // Phosphoric Ester
    $('#phosphoric_ester').on('click', function(){
        if (query !== ""){
            query += '.[$(P(=[OX1])([OX2][#6])([$([OX2H]),$([OX1-]),$([OX2][#6])])[$([OX2H]),$([OX1-]),$([OX2]';
            $("#fc-smarts-query").val(query);
        } else {
            query += '[$(P(=[OX1])([OX2][#6])([$([OX2H]),$([OX1-]),$([OX2][#6])])[$([OX2H]),$([OX1-]),$([OX2]';
            $("#fc-smarts-query").val(query);
        }
    });

    // Thioester
    $('#thioester').on('click', function(){
        if (query !== ""){
            query += '.[S-][CX3](=S)[#6]';
            $("#fc-smarts-query").val(query);
        } else {
            query += '[S-][CX3](=S)[#6]';
            $("#fc-smarts-query").val(query);
        }
    });

    // Thiocarboxyl acid
    $('#thiocarboxyl_acid').on('click', function(){
        if (query !== ""){
            query += '.[S-][CX3](=S)[#6]';
            $("#fc-smarts-query").val(query);
        } else {
            query += '[S-][CX3](=S)[#6]';
            $("#fc-smarts-query").val(query);
        }
    });

    // Thiol
    $('#thiol').on('click', function(){
        if (query !== ""){
            query += '.[SX2]';
            $("#fc-smarts-query").val(query);
        } else {
            query += '[SX2]';
            $("#fc-smarts-query").val(query);
        }
    });

    // Thioamide
    $('#thioamide').on('click', function(){
        if (query !== ""){
            query += '.[NX3][CX3]=[SX1]';
            $("#fc-smarts-query").val(query);
        } else {
            query += '[NX3][CX3]=[SX1]';
            $("#fc-smarts-query").val(query);
        }
    });

    // Sulfide
    $('#sulfide').on('click', function(){
        if (query !== ""){
            query += '.[#16X2H0]';
            $("#fc-smarts-query").val(query);
        } else {
            query += '[#16X2H0]';
            $("#fc-smarts-query").val(query);
        }
    });

    // Sulfinic acid
    $('#sulfinic_acid').on('click', function(){
        if (query !== ""){
            query += '.[$([#16X3](=[OX1])[OX2H,OX1H0-]),$([#16X3+]([OX1-])[OX2H,OX1H0-])]';
            $("#fc-smarts-query").val(query);
        } else {
            query += '[$([#16X3](=[OX1])[OX2H,OX1H0-]),$([#16X3+]([OX1-])[OX2H,OX1H0-])]';
            $("#fc-smarts-query").val(query);
        }
    });

    // Sulfone
    $('#sulfone').on('click', function(){
        if (query !== ""){
            query += '.[$([#16X4](=[OX1])(=[OX1])([#6])[#6]),$([#16X4+2]([OX1-])([OX1-])([#6])[#6])]';
            $("#fc-smarts-query").val(query);
        } else {
            query += '[$([#16X4](=[OX1])(=[OX1])([#6])[#6]),$([#16X4+2]([OX1-])([OX1-])([#6])[#6])]';
            $("#fc-smarts-query").val(query);
        }
    });

    // Sulfonic acid
    $('#sulfonic_acid').on('click', function(){
        if (query !== ""){
            query += '.[$([#16X4](=[OX1])(=[OX1])([#6])[OX2H,OX1H0-]),$([#16X4+2]([OX1-])([OX1-])([#6])';
            $("#fc-smarts-query").val(query);
        } else {
            query += '[$([#16X4](=[OX1])(=[OX1])([#6])[OX2H,OX1H0-]),$([#16X4+2]([OX1-])([OX1-])([#6])';
            $("#fc-smarts-query").val(query);
        }
    });

    // Sulfonamide
    $('#sulfonamide').on('click', function(){
        if (query !== ""){
            query += '.[$([#16X4]([NX3])(=[OX1])(=[OX1])[#6]),$([#16X4+2]([NX3])([OX1-])([OX1-])[#6])]';
            $("#fc-smarts-query").val(query);
        } else {
            query += '[$([#16X4]([NX3])(=[OX1])(=[OX1])[#6]),$([#16X4+2]([NX3])([OX1-])([OX1-])[#6])]';
            $("#fc-smarts-query").val(query);
        }
    });

    // Sulfuric acid ester
    $('#sulfuric_acid_ester').on('click', function(){
        if (query !== ""){
            query += '.[$([SX4](=O)(=O)(O)O),$([SX4+2]([O-])([O-])(O)O)]';
            $("#fc-smarts-query").val(query);
        } else {
            query += '[$([SX4](=O)(=O)(O)O),$([SX4+2]([O-])([O-])(O)O)]';
            $("#fc-smarts-query").val(query);
        }
    });

    // Sulfamate
    $('#sulfamate').on('click', function(){
        if (query !== ""){
            query += '.[$([#16X4]([NX3])(=[OX1])(=[OX1])[OX2][#6]),$([#16X4+2]([NX3])([OX1-])([OX1-])[OX2][#6])]';
            $("#fc-smarts-query").val(query);
        } else {
            query += '[$([#16X4]([NX3])(=[OX1])(=[OX1])[OX2][#6]),$([#16X4+2]([NX3])([OX1-])([OX1-])[OX2][#6])]';
            $("#fc-smarts-query").val(query);
        }
    });

    // Sulfamate acid
    $('#sulfamic_acid').on('click', function(){
        if (query !== ""){
            query += '.[$([#16X4]([NX3])(=[OX1])(=[OX1])[OX2H,OX1H0-]),$([#16X4+2]([NX3])([OX1-])([OX1-])';
            $("#fc-smarts-query").val(query);
        } else {
            query += '[$([#16X4]([NX3])(=[OX1])(=[OX1])[OX2H,OX1H0-]),$([#16X4+2]([NX3])([OX1-])([OX1-])';
            $("#fc-smarts-query").val(query);
        }
    });

    // Sulfenic acid
    $('#sulfenic_acid').on('click', function(){
        if (query !== ""){
            query += '.[#16X2][OX2H,OX1H0-]';
            $("#fc-smarts-query").val(query);
        } else {
            query += '[#16X2][OX2H,OX1H0-]';
            $("#fc-smarts-query").val(query);
        }
    });

    // Alkyl halide
    $('#halide').on('click', function(){
        if (query !== ""){
            query += '.[#6][F,Cl,Br,I]';
            $("#fc-smarts-query").val(query);
        } else {
            query += '[#6][F,Cl,Br,I]';
            $("#fc-smarts-query").val(query);
        }
    });

    // Acyl halide
    $('#acyl_halide').on('click', function(){
        if (query !== ""){
            query += '.[CX3](=[OX1])[F,Cl,Br,I]';
            $("#fc-smarts-query").val(query);
        } else {
            query += '[CX3](=[OX1])[F,Cl,Br,I]';
            $("#fc-smarts-query").val(query);
        }
    });
});