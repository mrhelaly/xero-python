# coding: utf-8

"""
    Xero Payroll NZ

    This is the Xero Payroll API for orgs in the NZ region.  # noqa: E501

    OpenAPI spec version: 2.7.0
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from enum import Enum


class CalendarType(Enum):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    allowed enum values
    """

    WEEKLY = "Weekly"
    FORTNIGHTLY = "Fortnightly"
    FOURWEEKLY = "FourWeekly"
    MONTHLY = "Monthly"
    ANNUAL = "Annual"
    QUARTERLY = "Quarterly"
    TWICEMONTHLY = "TwiceMonthly"
