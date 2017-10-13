/* Created by JDW on 2017-08-18. */
function resultParserToScatter(result) {
    var data = [];

    for (var i = 0; i < result.length; ++i){
        var row = {};
        /*
        * 1: ssu_cid
        * 2: py_mw
        * 3: atom_num
        * 4: bond_num
        * 5: ring_num
        * 6: logP
        * 12: FC
        * 13: HBA
        * 14: HBD
        * 15: rotate_bond
        * 16: rdkit_mw */

        // append category values according db
        if (result[i][17] === 1){           // 1
            row['category'] = "pubchem"
        }
        //row['ssu_cid'] = result[i][1];      // 2
        row['py_mw'] = result[i][2];        // 3
        row['atom_num'] = result[i][3];     // 4
        row['bond_num'] = result[i][4];     // 5
        row['logP'] = result[i][5];         // 6
        row['FC'] = result[i][12];          // 7
        row['HBA'] = result[i][13];         // 8
        row['HBD'] = result[i][14];         // 9
        row['rotate_bond'] = result[i][15]; // 10
        row['rdkit_mw'] = result[i][16];    // 11

        data.push(row);
    }

    //console.log(data);
    return data;
}


