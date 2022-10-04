import pkg_resources
import sys
import argparse

EXIT_CODES = {
    4:0,
    8:0,
    12:0
}


def prescriptive():
    _with_rules([
        'test_ia_lint_rules.prescriptive',
        'test_ia_lint_rules.security'
    ])

def main():
    _with_rules([
        'test_ia_lint_rules.security'
    ])


def _with_rules(rule_locations):
    entrypoint_func = pkg_resources.get_entry_map('cfn-lint', 'console_scripts')['cfn-lint'].load()
    sys.argv[1:] = [f"-a={r}" for r in rule_locations] + sys.argv[1:]
    ec = entrypoint_func()
    sys.exit(EXIT_CODES.get(ec, ec))

