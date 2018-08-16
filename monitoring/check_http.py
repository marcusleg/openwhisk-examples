import requests


class HTTPCheck:
    def __init__(self, config):
        self.config = config
        self.errors = []
        self.passed = True
        self.validate_config()
        
        try:
            # make request
            self.request = requests.get(
                self.config['url'],
                allow_redirects=False
            )
            # perform checks
            self.check_status_code()
            self.check_blank_page()
        except requests.exceptions.ConnectionError:
            self.add_error('Connection Error')

    def check_status_code(self):
        """checks whether website returns the expected status code"""
        if self.request.status_code == self.config['expected_status_code']:
            return

        self.add_error(
            'Status Code mismatch. ' +
            str(self.request.status_code) + ' != ' +
            str(self.config['expected_status_code'])
        )

    def check_blank_page(self):
        """checks whether the website is blank"""
        if len(self.request.text) > 0:
            return

        self.add_error('Page is blank. Size == 0')

    def add_error(self, message):
        self.passed = False
        self.errors.append(message)

    def result(self):
        return {
            'passed': self.passed,
            'errors': self.errors
        }

    def validate_config(self):
        assert self.config['url']
        assert self.config['expected_status_code']


def main(args):
    # validate args
    try:
        assert args['url']
        assert args['expected_status_code'] > 0
        assert args['expected_status_code'] < 600
    except (AssertionError, KeyError):
        return {'Error': 'Argument validation failed!'}

    # run checks
    check = HTTPCheck(args)
    return {**args, **check.result()}
