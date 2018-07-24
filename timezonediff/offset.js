function offset(timezone) {
    // since this only an example only a few time zones are implemented
    if (timezone == "DST") return -12; // Dateline Standard Time
    if (timezone == "HST") return -10; // Hawaiian Standard Time
    if (timezone == "HST") return -8; // Alaskan Standard Time
    if (timezone == "PST") return -8; // Pacific Standard Time
    if (timezone == "MST") return -6; // Mountain Standard Time
    if (timezone == "CST") return -5; // Central Standard Time
    if (timezone == "EST") return -4; // Eastern Standard Time
    if (timezone == "CEST") return 1; // Central European Standard Time
    if (timezone == "MST") return 3; // Moscow Standard Time
    if (timezone == "GST") return 4; // Gulf Standard Time
    if (timezone == "JST") return 9; // Japan Standard Time

    return null;
}

function main(args) {
    return { 'offset': offset(args.timezone) };
}