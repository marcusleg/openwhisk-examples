var openwhisk = require('openwhisk');

function offset(timezone) {
    var ow = openwhisk();
    const name = 'timezonediff/offset';
    const blocking = true, result = true;
    const params = {timezone: timezone};

    ow.actions.invoke({name, blocking, result, params}).then(result => {
        this.offset = result.offset;
    }).catch(err => {
        console.error('failed to invoke action', err);
    })
    return this.offset;
}

function difference(a, b) {
    var ow = openwhisk();
    const name = 'timezonediff/difference';
    const blocking = true, result = true;
    const params = {a: a, b: b};

    ow.actions.invoke({name, blocking, result, params}).then(result => {
        this.difference = result.difference;
    }).catch(err => {
        console.error('failed to invoke action', err);
    })
    return this.difference;
}

function main(params) {
    offset1 = offset(params.timezone1);
    offset2 = offset(params.timezone2);
    result = difference(offset1, offset2)
    console.log('|', offset1, "-", offset2, '| =', result)
    return {difference: result};
}

exports.main = main;