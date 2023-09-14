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
from ...common import search_resources_for_property_value_violations as srfpvv


LINT_ERROR_MESSAGE = "AWS::S3::Bucket must have versioning enabled."


class EBSVolumeEncryption(CloudFormationLintRule):
    """Check for EBS volumes without encryption at rest."""

    id = "ES3VersioningEnabled"
    shortdesc = "S3 Bucket missing versioning"
    description = "S3 Buckets should have versioning enabled."
    source_url = "https://github.com/aws-ia/cfn-ia-rules/blob/main/cfn_ia_rules/rules/security/s3_versioning.py"
    tags = ["s3", "versioning"]


    def match(self, cfn):
        """Basic Matching"""
        matches = []
        for ln in srfpvv(cfn, "AWS::EC2::Volume", "VersioningConfiguration.Status", "Enabled"):
            matches.append(RuleMatch(ln, LINT_ERROR_MESSAGE))
        return matches
