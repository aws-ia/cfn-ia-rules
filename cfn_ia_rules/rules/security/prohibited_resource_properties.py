from cfnlint.rules import CloudFormationLintRule
from ...common import ProhibitedResourceProperty, inherit_doc_string


@inherit_doc_string
class WAFV2NoDefaultAllow(
    ProhibitedResourceProperty, CloudFormationLintRule
):  # pylint: disable=C0115
    resource_type = "AWS::WAFv2::WebACL"
    property_name = "DefaultAction.Allow"
