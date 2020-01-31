# coding: utf-8

"""
    PMT API

    API for the XenonnT PMT database  # noqa: E501

    OpenAPI spec version: 0.1
    Contact: joe.mosbacher@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from pmtdb_client.api_client import ApiClient


class DatasheetApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_datasheet_item(self, datasheet_id, if_match, **kwargs):  # noqa: E501
        """Deletes a Datasheet document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_datasheet_item(datasheet_id, if_match, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str datasheet_id: (required)
        :param str if_match: Current value of the _etag field (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_datasheet_item_with_http_info(datasheet_id, if_match, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_datasheet_item_with_http_info(datasheet_id, if_match, **kwargs)  # noqa: E501
            return data

    def delete_datasheet_item_with_http_info(self, datasheet_id, if_match, **kwargs):  # noqa: E501
        """Deletes a Datasheet document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_datasheet_item_with_http_info(datasheet_id, if_match, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str datasheet_id: (required)
        :param str if_match: Current value of the _etag field (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['datasheet_id', 'if_match']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_datasheet_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'datasheet_id' is set
        if ('datasheet_id' not in params or
                params['datasheet_id'] is None):
            raise ValueError("Missing the required parameter `datasheet_id` when calling `delete_datasheet_item`")  # noqa: E501
        # verify the required parameter 'if_match' is set
        if ('if_match' not in params or
                params['if_match'] is None):
            raise ValueError("Missing the required parameter `if_match` when calling `delete_datasheet_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'datasheet_id' in params:
            path_params['datasheetId'] = params['datasheet_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'if_match' in params:
            header_params['If-Match'] = params['if_match']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/datasheets/{datasheetId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def deletedatasheets(self, **kwargs):  # noqa: E501
        """Deletes all datasheets  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deletedatasheets(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.deletedatasheets_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.deletedatasheets_with_http_info(**kwargs)  # noqa: E501
            return data

    def deletedatasheets_with_http_info(self, **kwargs):  # noqa: E501
        """Deletes all datasheets  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deletedatasheets_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method deletedatasheets" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/datasheets', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_datasheet_item(self, datasheet_id, **kwargs):  # noqa: E501
        """Retrieves a Datasheet document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_datasheet_item(datasheet_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str datasheet_id: (required)
        :return: Datasheet
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_datasheet_item_with_http_info(datasheet_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_datasheet_item_with_http_info(datasheet_id, **kwargs)  # noqa: E501
            return data

    def get_datasheet_item_with_http_info(self, datasheet_id, **kwargs):  # noqa: E501
        """Retrieves a Datasheet document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_datasheet_item_with_http_info(datasheet_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str datasheet_id: (required)
        :return: Datasheet
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['datasheet_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_datasheet_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'datasheet_id' is set
        if ('datasheet_id' not in params or
                params['datasheet_id'] is None):
            raise ValueError("Missing the required parameter `datasheet_id` when calling `get_datasheet_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'datasheet_id' in params:
            path_params['datasheetId'] = params['datasheet_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/datasheets/{datasheetId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Datasheet',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_datasheet_item_by_pmt_no(self, pmt_no, **kwargs):  # noqa: E501
        """Retrieves a Datasheet document by pmt_no  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_datasheet_item_by_pmt_no(pmt_no, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str pmt_no: (required)
        :return: Datasheet
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_datasheet_item_by_pmt_no_with_http_info(pmt_no, **kwargs)  # noqa: E501
        else:
            (data) = self.get_datasheet_item_by_pmt_no_with_http_info(pmt_no, **kwargs)  # noqa: E501
            return data

    def get_datasheet_item_by_pmt_no_with_http_info(self, pmt_no, **kwargs):  # noqa: E501
        """Retrieves a Datasheet document by pmt_no  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_datasheet_item_by_pmt_no_with_http_info(pmt_no, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str pmt_no: (required)
        :return: Datasheet
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['pmt_no']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_datasheet_item_by_pmt_no" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'pmt_no' is set
        if ('pmt_no' not in params or
                params['pmt_no'] is None):
            raise ValueError("Missing the required parameter `pmt_no` when calling `get_datasheet_item_by_pmt_no`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'pmt_no' in params:
            path_params['Pmt_No'] = params['pmt_no']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/datasheets/{Pmt_No}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Datasheet',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def getdatasheets(self, **kwargs):  # noqa: E501
        """Retrieves one or more datasheets  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getdatasheets(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str where: the filters query parameter (ex.: {\"number\": 10})
        :param str sort: the sort query parameter (ex.: \"city,-lastname\")
        :param int page: the pages query parameter
        :param int max_results: the max results query parameter
        :return: InlineResponse2003
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.getdatasheets_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.getdatasheets_with_http_info(**kwargs)  # noqa: E501
            return data

    def getdatasheets_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieves one or more datasheets  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getdatasheets_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str where: the filters query parameter (ex.: {\"number\": 10})
        :param str sort: the sort query parameter (ex.: \"city,-lastname\")
        :param int page: the pages query parameter
        :param int max_results: the max results query parameter
        :return: InlineResponse2003
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['where', 'sort', 'page', 'max_results']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method getdatasheets" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'where' in params:
            query_params.append(('where', params['where']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'max_results' in params:
            query_params.append(('max_results', params['max_results']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/datasheets', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2003',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def postdatasheets(self, body, **kwargs):  # noqa: E501
        """Stores one or more datasheets.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.postdatasheets(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Datasheet body: A Datasheet or list of Datasheet documents (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.postdatasheets_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.postdatasheets_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def postdatasheets_with_http_info(self, body, **kwargs):  # noqa: E501
        """Stores one or more datasheets.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.postdatasheets_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Datasheet body: A Datasheet or list of Datasheet documents (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method postdatasheets" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `postdatasheets`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/datasheets', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_datasheet_item(self, body, if_match, datasheet_id, **kwargs):  # noqa: E501
        """Replaces a Datasheet document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_datasheet_item(body, if_match, datasheet_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Datasheet body: A Datasheet or list of Datasheet documents (required)
        :param str if_match: Current value of the _etag field (required)
        :param str datasheet_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.put_datasheet_item_with_http_info(body, if_match, datasheet_id, **kwargs)  # noqa: E501
        else:
            (data) = self.put_datasheet_item_with_http_info(body, if_match, datasheet_id, **kwargs)  # noqa: E501
            return data

    def put_datasheet_item_with_http_info(self, body, if_match, datasheet_id, **kwargs):  # noqa: E501
        """Replaces a Datasheet document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_datasheet_item_with_http_info(body, if_match, datasheet_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Datasheet body: A Datasheet or list of Datasheet documents (required)
        :param str if_match: Current value of the _etag field (required)
        :param str datasheet_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'if_match', 'datasheet_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_datasheet_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_datasheet_item`")  # noqa: E501
        # verify the required parameter 'if_match' is set
        if ('if_match' not in params or
                params['if_match'] is None):
            raise ValueError("Missing the required parameter `if_match` when calling `put_datasheet_item`")  # noqa: E501
        # verify the required parameter 'datasheet_id' is set
        if ('datasheet_id' not in params or
                params['datasheet_id'] is None):
            raise ValueError("Missing the required parameter `datasheet_id` when calling `put_datasheet_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'datasheet_id' in params:
            path_params['datasheetId'] = params['datasheet_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'if_match' in params:
            header_params['If-Match'] = params['if_match']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/datasheets/{datasheetId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
