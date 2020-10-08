# coding: utf-8

"""
    Xero Payroll UK

    This is the Xero Payroll API for orgs in the UK region.  # noqa: E501

    OpenAPI spec version: 2.3.3
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class EmployeeStatutorySickLeaves(BaseModel):
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
    openapi_types = {
        "pagination": "Pagination",
        "problem": "Problem",
        "statutory_sick_leave": "list[EmployeeStatutorySickLeave]",
    }

    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "statutory_sick_leave": "statutorySickLeave",
    }

    def __init__(
        self, pagination=None, problem=None, statutory_sick_leave=None
    ):  # noqa: E501
        """EmployeeStatutorySickLeaves - a model defined in OpenAPI"""  # noqa: E501

        self._pagination = None
        self._problem = None
        self._statutory_sick_leave = None
        self.discriminator = None

        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if statutory_sick_leave is not None:
            self.statutory_sick_leave = statutory_sick_leave

    @property
    def pagination(self):
        """Gets the pagination of this EmployeeStatutorySickLeaves.  # noqa: E501


        :return: The pagination of this EmployeeStatutorySickLeaves.  # noqa: E501
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this EmployeeStatutorySickLeaves.


        :param pagination: The pagination of this EmployeeStatutorySickLeaves.  # noqa: E501
        :type: Pagination
        """

        self._pagination = pagination

    @property
    def problem(self):
        """Gets the problem of this EmployeeStatutorySickLeaves.  # noqa: E501


        :return: The problem of this EmployeeStatutorySickLeaves.  # noqa: E501
        :rtype: Problem
        """
        return self._problem

    @problem.setter
    def problem(self, problem):
        """Sets the problem of this EmployeeStatutorySickLeaves.


        :param problem: The problem of this EmployeeStatutorySickLeaves.  # noqa: E501
        :type: Problem
        """

        self._problem = problem

    @property
    def statutory_sick_leave(self):
        """Gets the statutory_sick_leave of this EmployeeStatutorySickLeaves.  # noqa: E501


        :return: The statutory_sick_leave of this EmployeeStatutorySickLeaves.  # noqa: E501
        :rtype: list[EmployeeStatutorySickLeave]
        """
        return self._statutory_sick_leave

    @statutory_sick_leave.setter
    def statutory_sick_leave(self, statutory_sick_leave):
        """Sets the statutory_sick_leave of this EmployeeStatutorySickLeaves.


        :param statutory_sick_leave: The statutory_sick_leave of this EmployeeStatutorySickLeaves.  # noqa: E501
        :type: list[EmployeeStatutorySickLeave]
        """

        self._statutory_sick_leave = statutory_sick_leave
