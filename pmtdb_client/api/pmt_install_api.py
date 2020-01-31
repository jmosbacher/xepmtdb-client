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


class PmtInstallApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def deletepmt_install_item(self, pmt_install_id, if_match, **kwargs):  # noqa: E501
        """Deletes a pmt_install document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deletepmt_install_item(pmt_install_id, if_match, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str pmt_install_id: (required)
        :param str if_match: Current value of the _etag field (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.deletepmt_install_item_with_http_info(pmt_install_id, if_match, **kwargs)  # noqa: E501
        else:
            (data) = self.deletepmt_install_item_with_http_info(pmt_install_id, if_match, **kwargs)  # noqa: E501
            return data

    def deletepmt_install_item_with_http_info(self, pmt_install_id, if_match, **kwargs):  # noqa: E501
        """Deletes a pmt_install document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deletepmt_install_item_with_http_info(pmt_install_id, if_match, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str pmt_install_id: (required)
        :param str if_match: Current value of the _etag field (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['pmt_install_id', 'if_match']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method deletepmt_install_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'pmt_install_id' is set
        if ('pmt_install_id' not in params or
                params['pmt_install_id'] is None):
            raise ValueError("Missing the required parameter `pmt_install_id` when calling `deletepmt_install_item`")  # noqa: E501
        # verify the required parameter 'if_match' is set
        if ('if_match' not in params or
                params['if_match'] is None):
            raise ValueError("Missing the required parameter `if_match` when calling `deletepmt_install_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'pmt_install_id' in params:
            path_params['pmt_installId'] = params['pmt_install_id']  # noqa: E501

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
            '/pmt_installs/{pmt_installId}', 'DELETE',
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

    def deletepmt_installs(self, **kwargs):  # noqa: E501
        """Deletes all pmt_installs  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deletepmt_installs(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.deletepmt_installs_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.deletepmt_installs_with_http_info(**kwargs)  # noqa: E501
            return data

    def deletepmt_installs_with_http_info(self, **kwargs):  # noqa: E501
        """Deletes all pmt_installs  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deletepmt_installs_with_http_info(async_req=True)
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
                    " to method deletepmt_installs" % key
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
            '/pmt_installs', 'DELETE',
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

    def getpmt_install_item(self, pmt_install_id, **kwargs):  # noqa: E501
        """Retrieves a pmt_install document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getpmt_install_item(pmt_install_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str pmt_install_id: (required)
        :return: PmtInstall
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.getpmt_install_item_with_http_info(pmt_install_id, **kwargs)  # noqa: E501
        else:
            (data) = self.getpmt_install_item_with_http_info(pmt_install_id, **kwargs)  # noqa: E501
            return data

    def getpmt_install_item_with_http_info(self, pmt_install_id, **kwargs):  # noqa: E501
        """Retrieves a pmt_install document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getpmt_install_item_with_http_info(pmt_install_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str pmt_install_id: (required)
        :return: PmtInstall
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['pmt_install_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method getpmt_install_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'pmt_install_id' is set
        if ('pmt_install_id' not in params or
                params['pmt_install_id'] is None):
            raise ValueError("Missing the required parameter `pmt_install_id` when calling `getpmt_install_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'pmt_install_id' in params:
            path_params['pmt_installId'] = params['pmt_install_id']  # noqa: E501

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
            '/pmt_installs/{pmt_installId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PmtInstall',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def getpmt_install_item_by_pmt_no(self, pmt_no, **kwargs):  # noqa: E501
        """Retrieves a pmt_install document by pmt_no  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getpmt_install_item_by_pmt_no(pmt_no, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str pmt_no: (required)
        :return: PmtInstall
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.getpmt_install_item_by_pmt_no_with_http_info(pmt_no, **kwargs)  # noqa: E501
        else:
            (data) = self.getpmt_install_item_by_pmt_no_with_http_info(pmt_no, **kwargs)  # noqa: E501
            return data

    def getpmt_install_item_by_pmt_no_with_http_info(self, pmt_no, **kwargs):  # noqa: E501
        """Retrieves a pmt_install document by pmt_no  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getpmt_install_item_by_pmt_no_with_http_info(pmt_no, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str pmt_no: (required)
        :return: PmtInstall
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
                    " to method getpmt_install_item_by_pmt_no" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'pmt_no' is set
        if ('pmt_no' not in params or
                params['pmt_no'] is None):
            raise ValueError("Missing the required parameter `pmt_no` when calling `getpmt_install_item_by_pmt_no`")  # noqa: E501

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
            '/pmt_installs/{Pmt_No}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PmtInstall',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def getpmt_installs(self, **kwargs):  # noqa: E501
        """Retrieves one or more pmt_installs  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getpmt_installs(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str where: the filters query parameter (ex.: {\"number\": 10})
        :param str sort: the sort query parameter (ex.: \"city,-lastname\")
        :param int page: the pages query parameter
        :param int max_results: the max results query parameter
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.getpmt_installs_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.getpmt_installs_with_http_info(**kwargs)  # noqa: E501
            return data

    def getpmt_installs_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieves one or more pmt_installs  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getpmt_installs_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str where: the filters query parameter (ex.: {\"number\": 10})
        :param str sort: the sort query parameter (ex.: \"city,-lastname\")
        :param int page: the pages query parameter
        :param int max_results: the max results query parameter
        :return: InlineResponse2002
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
                    " to method getpmt_installs" % key
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
            '/pmt_installs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2002',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def postpmt_installs(self, body, **kwargs):  # noqa: E501
        """Stores one or more pmt_installs.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.postpmt_installs(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PmtInstall body: A pmt_install or list of pmt_install documents (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.postpmt_installs_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.postpmt_installs_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def postpmt_installs_with_http_info(self, body, **kwargs):  # noqa: E501
        """Stores one or more pmt_installs.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.postpmt_installs_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PmtInstall body: A pmt_install or list of pmt_install documents (required)
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
                    " to method postpmt_installs" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `postpmt_installs`")  # noqa: E501

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
            '/pmt_installs', 'POST',
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

    def putpmt_install_item(self, body, if_match, pmt_install_id, **kwargs):  # noqa: E501
        """Replaces a pmt_install document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.putpmt_install_item(body, if_match, pmt_install_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PmtInstall body: A pmt_install or list of pmt_install documents (required)
        :param str if_match: Current value of the _etag field (required)
        :param str pmt_install_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.putpmt_install_item_with_http_info(body, if_match, pmt_install_id, **kwargs)  # noqa: E501
        else:
            (data) = self.putpmt_install_item_with_http_info(body, if_match, pmt_install_id, **kwargs)  # noqa: E501
            return data

    def putpmt_install_item_with_http_info(self, body, if_match, pmt_install_id, **kwargs):  # noqa: E501
        """Replaces a pmt_install document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.putpmt_install_item_with_http_info(body, if_match, pmt_install_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PmtInstall body: A pmt_install or list of pmt_install documents (required)
        :param str if_match: Current value of the _etag field (required)
        :param str pmt_install_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'if_match', 'pmt_install_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method putpmt_install_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `putpmt_install_item`")  # noqa: E501
        # verify the required parameter 'if_match' is set
        if ('if_match' not in params or
                params['if_match'] is None):
            raise ValueError("Missing the required parameter `if_match` when calling `putpmt_install_item`")  # noqa: E501
        # verify the required parameter 'pmt_install_id' is set
        if ('pmt_install_id' not in params or
                params['pmt_install_id'] is None):
            raise ValueError("Missing the required parameter `pmt_install_id` when calling `putpmt_install_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'pmt_install_id' in params:
            path_params['pmt_installId'] = params['pmt_install_id']  # noqa: E501

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
            '/pmt_installs/{pmt_installId}', 'PUT',
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
