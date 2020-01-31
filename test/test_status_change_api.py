# coding: utf-8

"""
    PMT API

    API for the XenonnT PMT database  # noqa: E501

    OpenAPI spec version: 0.1
    Contact: joe.mosbacher@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import pmtdb_client
from api.status_change_api import StatusChangeApi  # noqa: E501
from pmtdb_client.rest import ApiException


class TestStatusChangeApi(unittest.TestCase):
    """StatusChangeApi unit test stubs"""

    def setUp(self):
        self.api = api.status_change_api.StatusChangeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_deletestatus_change_item(self):
        """Test case for deletestatus_change_item

        Deletes a status_change document  # noqa: E501
        """
        pass

    def test_deletestatus_changes(self):
        """Test case for deletestatus_changes

        Deletes all status_changes  # noqa: E501
        """
        pass

    def test_getstatus_change_item(self):
        """Test case for getstatus_change_item

        Retrieves a status_change document  # noqa: E501
        """
        pass

    def test_getstatus_change_item_by_pmt_no(self):
        """Test case for getstatus_change_item_by_pmt_no

        Retrieves a status_change document by pmt_no  # noqa: E501
        """
        pass

    def test_getstatus_changes(self):
        """Test case for getstatus_changes

        Retrieves one or more status_changes  # noqa: E501
        """
        pass

    def test_poststatus_changes(self):
        """Test case for poststatus_changes

        Stores one or more status_changes.  # noqa: E501
        """
        pass

    def test_putstatus_change_item(self):
        """Test case for putstatus_change_item

        Replaces a status_change document  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()