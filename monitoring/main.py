def main(args):
    step = args['step'] if 'step' in args else 0

    # perform check
    if step == 0 and 'check' not in args.keys():
        return {'Error': 'Check type not found'}
    elif step == 0 and args['check'] == 'dns':
        return {
            'action': 'monitoring/checkDNS',
            'params': args,
            'state': { 'step': step + 1 }
        }
    elif step == 0 and args['check'] == 'http':
        return {
            'action': 'monitoring/checkHTTP',
            'params': args,
            'state': { 'step': step + 1 }
        }
    elif step == 0:
        return {'Error': 'Unkown check type: ' + args['check']}

    # send alert via email if check failed
    if step == 1 and args['passed'] == False:
        return {
            'action': 'monitoring/sendmail',
            'params': {
                **args,
                'subject': args['check'].upper() + ' check failed',
                'body': '\n'.join(args['errors']),
            },
            'state': { 'step': step + 1 }
        }
    
    # terminate
    del args['step']
    return args
