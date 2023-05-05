"""
  Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

  Permission is hereby granted, free of charge, to any person obtaining a copy of this
  software and associated documentation files (the "Software"), to deal in the Software
  without restriction, including without limitation the rights to use, copy, modify,
  merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
  permit persons to whom the Software is furnished to do so.

  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
  INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
  PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
  HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
  OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
  SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


from cfnlint.rules import CloudFormationLintRule, RuleMatch
from ...common import deep_get

LINT_ERROR_MESSAGE = "Combining Action and NotResource is a bad idea."
CFN_NAG_RULES = [
    "W21",
    "W15",
]


def determine_action_notaction_violation(cfn, policy_path):
    policy = deep_get(cfn.template, policy_path, [])
    return all(x in policy.keys() for x in ["Resource", "NotResource"])


class IAMNotResource(CloudFormationLintRule):
    """Check for IAM policies with both Resource and NotResource."""

    id = "EIAMPolicyActionNotResource"
    shortdesc = "Combining Resource and NotResource is a bad idea."
    description = "Making sure Resource and NotResource are not used in an IAM statement together."
    source_url = "https://github.com/aws-ia/cfn-ia-rules/blob/main/cfn_ia_rules/rules/security/iam_not_resource.py"
    tags = ["iam"]
    SEARCH_PROPS = ["Resource"]

    def match(self, cfn):
        """Basic Matching"""
        violation_matches = []
        term_matches = []
        for prop in self.SEARCH_PROPS:
            term_matches += cfn.search_deep_keys(prop)
        for tm in term_matches:
            violating_policy = determine_action_notaction_violation(cfn, tm[:-2])
            if violating_policy:
                violation_matches.append(
                    RuleMatch(tm[:-2] + ["NotResource"], LINT_ERROR_MESSAGE)
                )
        return violation_matches
