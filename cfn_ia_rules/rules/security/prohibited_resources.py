from cfnlint.rules import CloudFormationLintRule
from ...common import ProhibitedResource, inherit_doc_string


@inherit_doc_string
class NoSimpleDBDomain(
    ProhibitedResource, CloudFormationLintRule
):  # pylint: disable=C0115
    resource_type = "AWS::SimpleDB::Domain"
    CFN_NAG_RULES = ["F77"]
