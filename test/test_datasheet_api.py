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
from api.datasheet_api import DatasheetApi  # noqa: E501
from pmtdb_client.rest import ApiException


class TestDatasheetApi(unittest.TestCase):
    """DatasheetApi unit test stubs"""

    def setUp(self):
        self.api = api.datasheet_api.DatasheetApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_datasheet_item(self):
        """Test case for delete_datasheet_item

        Deletes a Datasheet document  # noqa: E501
        """
        pass

    def test_deletedatasheets(self):
        """Test case for deletedatasheets

        Deletes all datasheets  # noqa: E501
        """
        pass

    def test_get_datasheet_item(self):
        """Test case for get_datasheet_item

        Retrieves a Datasheet document  # noqa: E501
        """
        pass

    def test_get_datasheet_item_by_pmt_no(self):
        """Test case for get_datasheet_item_by_pmt_no

        Retrieves a Datasheet document by pmt_no  # noqa: E501
        """
        pass

    def test_getdatasheets(self):
        """Test case for getdatasheets

        Retrieves one or more datasheets  # noqa: E501
        """
        pass

    def test_postdatasheets(self):
        """Test case for postdatasheets

        Stores one or more datasheets.  # noqa: E501
        """
        pass

    def test_put_datasheet_item(self):
        """Test case for put_datasheet_item

        Replaces a Datasheet document  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()