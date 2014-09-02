var fs = require('fs');
var moment = require('moment');
var scriptName = "batchGen.sh";

function generate (start, end) {
    var startT = moment(start);
    var endT = moment(end);
    while (startT.isBefore(endT)) {
        var timeStr = startT.format("YYYY-MM-DD");
        fs.appendFileSync(scriptName, './extract.sh '+timeStr+' \n');
        startT.add(1,'days');
    }
}

generate('2012-10-27','2013-06-23');
generate('2013-10-27','2014-06-07');