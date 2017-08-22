# -*- coding: utf-8 -*-

"""
    mundiapi.models.get_address_response

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io )
"""
from mundiapi.api_helper import APIHelper
import mundiapi.models.get_customer_response

class GetAddressResponse(object):

    """Implementation of the 'GetAddressResponse' model.

    Response object for getting an Address

    Attributes:
        id (string): TODO: type description here.
        street (string): TODO: type description here.
        number (string): TODO: type description here.
        complement (string): TODO: type description here.
        zip_code (string): TODO: type description here.
        neighborhood (string): TODO: type description here.
        city (string): TODO: type description here.
        state (string): TODO: type description here.
        country (string): TODO: type description here.
        status (string): TODO: type description here.
        created_at (datetime): TODO: type description here.
        updated_at (datetime): TODO: type description here.
        customer (GetCustomerResponse): TODO: type description here.
        metadata (dict<object, string>): TODO: type description here.
        deleted_at (datetime): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id" : "id",
        "street" : "street",
        "number" : "number",
        "complement" : "complement",
        "zip_code" : "zip_code",
        "neighborhood" : "neighborhood",
        "city" : "city",
        "state" : "state",
        "country" : "country",
        "status" : "status",
        "created_at" : "created_at",
        "updated_at" : "updated_at",
        "customer" : "customer",
        "metadata" : "metadata",
        "deleted_at" : "deleted_at"
    }

    def __init__(self,
                 id=None,
                 street=None,
                 number=None,
                 complement=None,
                 zip_code=None,
                 neighborhood=None,
                 city=None,
                 state=None,
                 country=None,
                 status=None,
                 created_at=None,
                 updated_at=None,
                 customer=None,
                 metadata=None,
                 deleted_at=None):
        """Constructor for the GetAddressResponse class"""

        # Initialize members of the class
        self.id = id
        self.street = street
        self.number = number
        self.complement = complement
        self.zip_code = zip_code
        self.neighborhood = neighborhood
        self.city = city
        self.state = state
        self.country = country
        self.status = status
        self.created_at = APIHelper.RFC3339DateTime(created_at) if created_at else None
        self.updated_at = APIHelper.RFC3339DateTime(updated_at) if updated_at else None
        self.customer = customer
        self.metadata = metadata
        self.deleted_at = APIHelper.RFC3339DateTime(deleted_at) if deleted_at else None


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        id = dictionary.get("id")
        street = dictionary.get("street")
        number = dictionary.get("number")
        complement = dictionary.get("complement")
        zip_code = dictionary.get("zip_code")
        neighborhood = dictionary.get("neighborhood")
        city = dictionary.get("city")
        state = dictionary.get("state")
        country = dictionary.get("country")
        status = dictionary.get("status")
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else None
        updated_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("updated_at")).datetime if dictionary.get("updated_at") else None
        customer = mundiapi.models.get_customer_response.GetCustomerResponse.from_dictionary(dictionary.get("customer")) if dictionary.get("customer") else None
        metadata = dictionary.get("metadata")
        deleted_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("deleted_at")).datetime if dictionary.get("deleted_at") else None

        # Return an object of this model
        return cls(id,
                   street,
                   number,
                   complement,
                   zip_code,
                   neighborhood,
                   city,
                   state,
                   country,
                   status,
                   created_at,
                   updated_at,
                   customer,
                   metadata,
                   deleted_at)


