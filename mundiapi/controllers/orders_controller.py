# -*- coding: utf-8 -*-

"""
    mundiapi.controllers.orders_controller

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.basic_auth import BasicAuth
from ..models.get_order_response import GetOrderResponse
from ..models.list_order_response import ListOrderResponse

class OrdersController(BaseController):

    """A Controller to access Endpoints in the mundiapi API."""


    def get_order(self,
                  order_id):
        """Does a GET request to /orders/{order_id}.

        Gets an order

        Args:
            order_id (string): Order id

        Returns:
            GetOrderResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/orders/{order_id}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'order_id': order_id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GetOrderResponse.from_dictionary)

    def create_order(self,
                     body):
        """Does a POST request to /orders.

        Creates a new Order

        Args:
            body (CreateOrderRequest): Request for creating an order

        Returns:
            GetOrderResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/orders'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GetOrderResponse.from_dictionary)

    def update_order_metadata(self,
                              order_id,
                              request):
        """Does a PATCH request to /Orders/{order_id}/metadata.

        Updates the metadata from an order

        Args:
            order_id (string): The order id
            request (UpdateMetadataRequest): Request for updating the order
                metadata

        Returns:
            GetOrderResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/Orders/{order_id}/metadata'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'order_id': order_id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.patch(_query_url, headers=_headers, parameters=APIHelper.json_serialize(request))
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GetOrderResponse.from_dictionary)

    def get_orders(self,
                   page=None,
                   size=None,
                   code=None,
                   status=None,
                   created_since=None,
                   created_until=None,
                   customer_id=None):
        """Does a GET request to /orders.

        Gets all orders

        Args:
            page (int, optional): Page number
            size (int, optional): Page size
            code (string, optional): Filter for order's code
            status (string, optional): Filter for order's status
            created_since (datetime, optional): Filter for order's creation
                date start range
            created_until (datetime, optional): Filter for order's creation
                date end range
            customer_id (string, optional): Filter for order's customer id

        Returns:
            ListOrderResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/orders'
        _query_parameters = {
            'page': page,
            'size': size,
            'code': code,
            'status': status,
            'created_since': APIHelper.RFC3339DateTime(created_since),
            'created_until': APIHelper.RFC3339DateTime(created_until),
            'customer_id': customer_id
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, ListOrderResponse.from_dictionary)
