# -*- coding: utf-8 -*-

"""
    mundiapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from mundiapi.api_helper import APIHelper
from mundiapi.configuration import Configuration
from mundiapi.controllers.base_controller import BaseController
from mundiapi.http.auth.basic_auth import BasicAuth
from mundiapi.models.get_recipient_response import GetRecipientResponse
from mundiapi.models.get_anticipation_response import GetAnticipationResponse
from mundiapi.models.list_recipient_response import ListRecipientResponse
from mundiapi.models.get_balance_response import GetBalanceResponse
from mundiapi.models.list_anticipation_response import ListAnticipationResponse
from mundiapi.models.get_transfer_response import GetTransferResponse
from mundiapi.models.list_transfer_response import ListTransferResponse
from mundiapi.models.get_anticipation_limit_response import GetAnticipationLimitResponse

class RecipientsController(BaseController):

    """A Controller to access Endpoints in the mundiapi API."""


    def update_recipient_metadata(self,
                                  recipient_id,
                                  request,
                                  idempotency_key=None):
        """Does a PATCH request to /recipients/{recipient_id}/metadata.

        Updates recipient metadata

        Args:
            recipient_id (string): Recipient id
            request (UpdateMetadataRequest): Metadata
            idempotency_key (string, optional): TODO: type description here.
                Example: 

        Returns:
            GetRecipientResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/recipients/{recipient_id}/metadata'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'recipient_id': recipient_id
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8',
            'idempotency-key': idempotency_key
        }

        # Prepare and execute request
        _request = self.http_client.patch(_query_url, headers=_headers, parameters=APIHelper.json_serialize(request))
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GetRecipientResponse.from_dictionary)

    def update_recipient_transfer_settings(self,
                                           recipient_id,
                                           request,
                                           idempotency_key=None):
        """Does a PATCH request to /recipients/{recipient_id}/transfer-settings.

        TODO: type endpoint description here.

        Args:
            recipient_id (string): Recipient Identificator
            request (UpdateTransferSettingsRequest): TODO: type description
                here. Example: 
            idempotency_key (string, optional): TODO: type description here.
                Example: 

        Returns:
            GetRecipientResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/recipients/{recipient_id}/transfer-settings'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'recipient_id': recipient_id
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8',
            'idempotency-key': idempotency_key
        }

        # Prepare and execute request
        _request = self.http_client.patch(_query_url, headers=_headers, parameters=APIHelper.json_serialize(request))
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GetRecipientResponse.from_dictionary)

    def get_anticipation(self,
                         recipient_id,
                         anticipation_id):
        """Does a GET request to /recipients/{recipient_id}/anticipations/{anticipation_id}.

        Gets an anticipation

        Args:
            recipient_id (string): Recipient id
            anticipation_id (string): Anticipation id

        Returns:
            GetAnticipationResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/recipients/{recipient_id}/anticipations/{anticipation_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'recipient_id': recipient_id,
            'anticipation_id': anticipation_id
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
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
        return APIHelper.json_deserialize(_context.response.raw_body, GetAnticipationResponse.from_dictionary)

    def get_recipients(self,
                       page=None,
                       size=None):
        """Does a GET request to /recipients.

        Retrieves paginated recipients information

        Args:
            page (int, optional): Page number
            size (int, optional): Page size

        Returns:
            ListRecipientResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/recipients'
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_parameters = {
            'page': page,
            'size': size
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
        return APIHelper.json_deserialize(_context.response.raw_body, ListRecipientResponse.from_dictionary)

    def get_balance(self,
                    recipient_id):
        """Does a GET request to /recipients/{recipient_id}/balance.

        Get balance information for a recipient

        Args:
            recipient_id (string): Recipient id

        Returns:
            GetBalanceResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/recipients/{recipient_id}/balance'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'recipient_id': recipient_id
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
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
        return APIHelper.json_deserialize(_context.response.raw_body, GetBalanceResponse.from_dictionary)

    def get_anticipations(self,
                          recipient_id,
                          page=None,
                          size=None,
                          status=None,
                          timeframe=None,
                          payment_date_since=None,
                          payment_date_until=None,
                          created_since=None,
                          created_until=None):
        """Does a GET request to /recipients/{recipient_id}/anticipations.

        Retrieves a paginated list of anticipations from a recipient

        Args:
            recipient_id (string): Recipient id
            page (int, optional): Page number
            size (int, optional): Page size
            status (string, optional): Filter for anticipation status
            timeframe (string, optional): Filter for anticipation timeframe
            payment_date_since (datetime, optional): Filter for start range
                for anticipation payment date
            payment_date_until (datetime, optional): Filter for end range for
                anticipation payment date
            created_since (datetime, optional): Filter for start range for
                anticipation creation date
            created_until (datetime, optional): Filter for end range for
                anticipation creation date

        Returns:
            ListAnticipationResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/recipients/{recipient_id}/anticipations'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'recipient_id': recipient_id
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_parameters = {
            'page': page,
            'size': size,
            'status': status,
            'timeframe': timeframe,
            'payment_date_since': APIHelper.when_defined(APIHelper.RFC3339DateTime, payment_date_since),
            'payment_date_until': APIHelper.when_defined(APIHelper.RFC3339DateTime, payment_date_until),
            'created_since': APIHelper.when_defined(APIHelper.RFC3339DateTime, created_since),
            'created_until': APIHelper.when_defined(APIHelper.RFC3339DateTime, created_until)
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
        return APIHelper.json_deserialize(_context.response.raw_body, ListAnticipationResponse.from_dictionary)

    def create_anticipation(self,
                            recipient_id,
                            request,
                            idempotency_key=None):
        """Does a POST request to /recipients/{recipient_id}/anticipations.

        Creates an anticipation

        Args:
            recipient_id (string): Recipient id
            request (CreateAnticipationRequest): Anticipation data
            idempotency_key (string, optional): TODO: type description here.
                Example: 

        Returns:
            GetAnticipationResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/recipients/{recipient_id}/anticipations'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'recipient_id': recipient_id
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8',
            'idempotency-key': idempotency_key
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(request))
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GetAnticipationResponse.from_dictionary)

    def update_recipient_default_bank_account(self,
                                              recipient_id,
                                              request,
                                              idempotency_key=None):
        """Does a PATCH request to /recipients/{recipient_id}/default-bank-account.

        Updates the default bank account from a recipient

        Args:
            recipient_id (string): Recipient id
            request (UpdateRecipientBankAccountRequest): Bank account data
            idempotency_key (string, optional): TODO: type description here.
                Example: 

        Returns:
            GetRecipientResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/recipients/{recipient_id}/default-bank-account'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'recipient_id': recipient_id
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8',
            'idempotency-key': idempotency_key
        }

        # Prepare and execute request
        _request = self.http_client.patch(_query_url, headers=_headers, parameters=APIHelper.json_serialize(request))
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GetRecipientResponse.from_dictionary)

    def get_recipient(self,
                      recipient_id):
        """Does a GET request to /recipients/{recipient_id}.

        Retrieves recipient information

        Args:
            recipient_id (string): Recipiend id

        Returns:
            GetRecipientResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/recipients/{recipient_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'recipient_id': recipient_id
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
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
        return APIHelper.json_deserialize(_context.response.raw_body, GetRecipientResponse.from_dictionary)

    def get_transfer(self,
                     recipient_id,
                     transfer_id):
        """Does a GET request to /recipients/{recipient_id}/transfers/{transfer_id}.

        Gets a transfer

        Args:
            recipient_id (string): Recipient id
            transfer_id (string): Transfer id

        Returns:
            GetTransferResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/recipients/{recipient_id}/transfers/{transfer_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'recipient_id': recipient_id,
            'transfer_id': transfer_id
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
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
        return APIHelper.json_deserialize(_context.response.raw_body, GetTransferResponse.from_dictionary)

    def get_transfers(self,
                      recipient_id,
                      page=None,
                      size=None,
                      status=None,
                      created_since=None,
                      created_until=None):
        """Does a GET request to /recipients/{recipient_id}/transfers.

        Gets a paginated list of transfers for the recipient

        Args:
            recipient_id (string): Recipient id
            page (int, optional): Page number
            size (int, optional): Page size
            status (string, optional): Filter for transfer status
            created_since (datetime, optional): Filter for start range of
                transfer creation date
            created_until (datetime, optional): Filter for end range of
                transfer creation date

        Returns:
            ListTransferResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/recipients/{recipient_id}/transfers'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'recipient_id': recipient_id
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_parameters = {
            'page': page,
            'size': size,
            'status': status,
            'created_since': APIHelper.when_defined(APIHelper.RFC3339DateTime, created_since),
            'created_until': APIHelper.when_defined(APIHelper.RFC3339DateTime, created_until)
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
        return APIHelper.json_deserialize(_context.response.raw_body, ListTransferResponse.from_dictionary)

    def update_recipient(self,
                         recipient_id,
                         request,
                         idempotency_key=None):
        """Does a PUT request to /recipients/{recipient_id}.

        Updates a recipient

        Args:
            recipient_id (string): Recipient id
            request (UpdateRecipientRequest): Recipient data
            idempotency_key (string, optional): TODO: type description here.
                Example: 

        Returns:
            GetRecipientResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/recipients/{recipient_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'recipient_id': recipient_id
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8',
            'idempotency-key': idempotency_key
        }

        # Prepare and execute request
        _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(request))
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GetRecipientResponse.from_dictionary)

    def create_recipient(self,
                         request,
                         idempotency_key=None):
        """Does a POST request to /recipients.

        Creates a new recipient

        Args:
            request (CreateRecipientRequest): Recipient data
            idempotency_key (string, optional): TODO: type description here.
                Example: 

        Returns:
            GetRecipientResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/recipients'
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8',
            'idempotency-key': idempotency_key
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(request))
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GetRecipientResponse.from_dictionary)

    def create_transfer(self,
                        recipient_id,
                        request,
                        idempotency_key=None):
        """Does a POST request to /recipients/{recipient_id}/transfers.

        Creates a transfer for a recipient

        Args:
            recipient_id (string): Recipient Id
            request (CreateTransferRequest): Transfer data
            idempotency_key (string, optional): TODO: type description here.
                Example: 

        Returns:
            GetTransferResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/recipients/{recipient_id}/transfers'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'recipient_id': recipient_id
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8',
            'idempotency-key': idempotency_key
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(request))
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GetTransferResponse.from_dictionary)

    def get_anticipation_limits(self,
                                recipient_id,
                                timeframe,
                                payment_date):
        """Does a GET request to /recipients/{recipient_id}/anticipation_limits.

        Gets the anticipation limits for a recipient

        Args:
            recipient_id (string): Recipient id
            timeframe (string): Timeframe
            payment_date (datetime): Anticipation payment date

        Returns:
            GetAnticipationLimitResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/recipients/{recipient_id}/anticipation_limits'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'recipient_id': recipient_id
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_parameters = {
            'timeframe': timeframe,
            'payment_date': APIHelper.when_defined(APIHelper.RFC3339DateTime, payment_date)
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
        return APIHelper.json_deserialize(_context.response.raw_body, GetAnticipationLimitResponse.from_dictionary)
