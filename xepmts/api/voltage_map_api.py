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

from xepmts.api_client import ApiClient


class VoltageMapApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def deletevoltage_map_item(self, voltage_map_id, if_match, **kwargs):  # noqa: E501
        """Deletes a voltage_map document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deletevoltage_map_item(voltage_map_id, if_match, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str voltage_map_id: (required)
        :param str if_match: Current value of the _etag field (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.deletevoltage_map_item_with_http_info(voltage_map_id, if_match, **kwargs)  # noqa: E501
        else:
            (data) = self.deletevoltage_map_item_with_http_info(voltage_map_id, if_match, **kwargs)  # noqa: E501
            return data

    def deletevoltage_map_item_with_http_info(self, voltage_map_id, if_match, **kwargs):  # noqa: E501
        """Deletes a voltage_map document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deletevoltage_map_item_with_http_info(voltage_map_id, if_match, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str voltage_map_id: (required)
        :param str if_match: Current value of the _etag field (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['voltage_map_id', 'if_match']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method deletevoltage_map_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'voltage_map_id' is set
        if ('voltage_map_id' not in params or
                params['voltage_map_id'] is None):
            raise ValueError("Missing the required parameter `voltage_map_id` when calling `deletevoltage_map_item`")  # noqa: E501
        # verify the required parameter 'if_match' is set
        if ('if_match' not in params or
                params['if_match'] is None):
            raise ValueError("Missing the required parameter `if_match` when calling `deletevoltage_map_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'voltage_map_id' in params:
            path_params['voltage_mapId'] = params['voltage_map_id']  # noqa: E501

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
            '/voltage_maps/{voltage_mapId}', 'DELETE',
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

    def deletevoltage_maps(self, **kwargs):  # noqa: E501
        """Deletes all voltage_maps  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deletevoltage_maps(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.deletevoltage_maps_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.deletevoltage_maps_with_http_info(**kwargs)  # noqa: E501
            return data

    def deletevoltage_maps_with_http_info(self, **kwargs):  # noqa: E501
        """Deletes all voltage_maps  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deletevoltage_maps_with_http_info(async_req=True)
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
                    " to method deletevoltage_maps" % key
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
            '/voltage_maps', 'DELETE',
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

    def getvoltage_map_item(self, voltage_map_id, **kwargs):  # noqa: E501
        """Retrieves a voltage_map document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getvoltage_map_item(voltage_map_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str voltage_map_id: (required)
        :return: VoltageMap
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.getvoltage_map_item_with_http_info(voltage_map_id, **kwargs)  # noqa: E501
        else:
            (data) = self.getvoltage_map_item_with_http_info(voltage_map_id, **kwargs)  # noqa: E501
            return data

    def getvoltage_map_item_with_http_info(self, voltage_map_id, **kwargs):  # noqa: E501
        """Retrieves a voltage_map document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getvoltage_map_item_with_http_info(voltage_map_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str voltage_map_id: (required)
        :return: VoltageMap
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['voltage_map_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method getvoltage_map_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'voltage_map_id' is set
        if ('voltage_map_id' not in params or
                params['voltage_map_id'] is None):
            raise ValueError("Missing the required parameter `voltage_map_id` when calling `getvoltage_map_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'voltage_map_id' in params:
            path_params['voltage_mapId'] = params['voltage_map_id']  # noqa: E501

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
            '/voltage_maps/{voltage_mapId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VoltageMap',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def getvoltage_map_item_by_name(self, name, **kwargs):  # noqa: E501
        """Retrieves a voltage_map document by name  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getvoltage_map_item_by_name(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: (required)
        :return: VoltageMap
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.getvoltage_map_item_by_name_with_http_info(name, **kwargs)  # noqa: E501
        else:
            (data) = self.getvoltage_map_item_by_name_with_http_info(name, **kwargs)  # noqa: E501
            return data

    def getvoltage_map_item_by_name_with_http_info(self, name, **kwargs):  # noqa: E501
        """Retrieves a voltage_map document by name  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getvoltage_map_item_by_name_with_http_info(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: (required)
        :return: VoltageMap
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method getvoltage_map_item_by_name" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `getvoltage_map_item_by_name`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['Name'] = params['name']  # noqa: E501

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
            '/voltage_maps/{Name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VoltageMap',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def getvoltage_maps(self, **kwargs):  # noqa: E501
        """Retrieves one or more voltage_maps  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getvoltage_maps(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str where: the filters query parameter (ex.: {\"number\": 10})
        :param str sort: the sort query parameter (ex.: \"city,-lastname\")
        :param int page: the pages query parameter
        :param int max_results: the max results query parameter
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.getvoltage_maps_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.getvoltage_maps_with_http_info(**kwargs)  # noqa: E501
            return data

    def getvoltage_maps_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieves one or more voltage_maps  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getvoltage_maps_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str where: the filters query parameter (ex.: {\"number\": 10})
        :param str sort: the sort query parameter (ex.: \"city,-lastname\")
        :param int page: the pages query parameter
        :param int max_results: the max results query parameter
        :return: InlineResponse2001
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
                    " to method getvoltage_maps" % key
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
            '/voltage_maps', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2001',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def postvoltage_maps(self, body, **kwargs):  # noqa: E501
        """Stores one or more voltage_maps.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.postvoltage_maps(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param VoltageMap body: A voltage_map or list of voltage_map documents (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.postvoltage_maps_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.postvoltage_maps_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def postvoltage_maps_with_http_info(self, body, **kwargs):  # noqa: E501
        """Stores one or more voltage_maps.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.postvoltage_maps_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param VoltageMap body: A voltage_map or list of voltage_map documents (required)
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
                    " to method postvoltage_maps" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `postvoltage_maps`")  # noqa: E501

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
            '/voltage_maps', 'POST',
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

    def putvoltage_map_item(self, body, if_match, voltage_map_id, **kwargs):  # noqa: E501
        """Replaces a voltage_map document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.putvoltage_map_item(body, if_match, voltage_map_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param VoltageMap body: A voltage_map or list of voltage_map documents (required)
        :param str if_match: Current value of the _etag field (required)
        :param str voltage_map_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.putvoltage_map_item_with_http_info(body, if_match, voltage_map_id, **kwargs)  # noqa: E501
        else:
            (data) = self.putvoltage_map_item_with_http_info(body, if_match, voltage_map_id, **kwargs)  # noqa: E501
            return data

    def putvoltage_map_item_with_http_info(self, body, if_match, voltage_map_id, **kwargs):  # noqa: E501
        """Replaces a voltage_map document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.putvoltage_map_item_with_http_info(body, if_match, voltage_map_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param VoltageMap body: A voltage_map or list of voltage_map documents (required)
        :param str if_match: Current value of the _etag field (required)
        :param str voltage_map_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'if_match', 'voltage_map_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method putvoltage_map_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `putvoltage_map_item`")  # noqa: E501
        # verify the required parameter 'if_match' is set
        if ('if_match' not in params or
                params['if_match'] is None):
            raise ValueError("Missing the required parameter `if_match` when calling `putvoltage_map_item`")  # noqa: E501
        # verify the required parameter 'voltage_map_id' is set
        if ('voltage_map_id' not in params or
                params['voltage_map_id'] is None):
            raise ValueError("Missing the required parameter `voltage_map_id` when calling `putvoltage_map_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'voltage_map_id' in params:
            path_params['voltage_mapId'] = params['voltage_map_id']  # noqa: E501

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
            '/voltage_maps/{voltage_mapId}', 'PUT',
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