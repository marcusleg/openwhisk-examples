import socket


def dns_check(host, type, expected_ip):
    """returns True when the DNS record for host of the specified type resolves to ip"""
    if type.lower() == 'a':
        return dns_check_type_a(host, expected_ip)

    if type.lower() == 'aaaa':
        return dns_check_type_aaaa(host, expected_ip)

    raise ValueError('Unknown type')


def dns_check_type_a(host, expected_ip):
    resolved_ip = socket.gethostbyname(host)
    if resolved_ip == expected_ip:
        return {'passed': True}
    return {
        'passed': False,
        'errors': [host + ' resolved to ' + resolved_ip +
        ' (expected ' + expected_ip + ')']
    }


def dns_check_type_aaaa(host, expected_ip):
    resolved_ip = socket.getaddrinfo(host, None, family=socket.AF_INET6)[0][4][0]
    if resolved_ip == expected_ip:
        return {'passed': True, 'errors': []}
    return {
        'passed': False,
        'errors': [host + ' resolved to ' + resolved_ip +
        ' (expected ' + expected_ip + ')']
    }


def main(args):
    # validate args
    try:
        assert args['host']
        assert args['type'].lower() in ['a', 'aaaa']
        assert args['ip']
    except (AssertionError, KeyError):
        return 'Error: Bad Request', 400

    # run check
    try:
        result = dns_check(
            args['host'],
            args['type'],
            args['ip']
        )
        return {**args, **result}
    except ValueError:
        return {'Error': 'Unkown record type: ' + args['type']}
