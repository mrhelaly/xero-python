# coding: utf-8

"""
    Xero Payroll AU

    This is the Xero Payroll API for orgs in Australia region.  # noqa: E501

    OpenAPI spec version: 2.3.3
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class SuperFundProducts(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {"super_fund_products": "list[SuperFundProduct]"}

    attribute_map = {"super_fund_products": "SuperFundProducts"}

    def __init__(self, super_fund_products=None):  # noqa: E501
        """SuperFundProducts - a model defined in OpenAPI"""  # noqa: E501

        self._super_fund_products = None
        self.discriminator = None

        if super_fund_products is not None:
            self.super_fund_products = super_fund_products

    @property
    def super_fund_products(self):
        """Gets the super_fund_products of this SuperFundProducts.  # noqa: E501


        :return: The super_fund_products of this SuperFundProducts.  # noqa: E501
        :rtype: list[SuperFundProduct]
        """
        return self._super_fund_products

    @super_fund_products.setter
    def super_fund_products(self, super_fund_products):
        """Sets the super_fund_products of this SuperFundProducts.


        :param super_fund_products: The super_fund_products of this SuperFundProducts.  # noqa: E501
        :type: list[SuperFundProduct]
        """

        self._super_fund_products = super_fund_products
