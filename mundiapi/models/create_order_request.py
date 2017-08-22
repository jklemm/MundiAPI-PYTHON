# -*- coding: utf-8 -*-

"""
    mundiapi.models.create_order_request

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io )
"""
import mundiapi.models.create_order_item_request
import mundiapi.models.create_customer_request
import mundiapi.models.create_payment_request
import mundiapi.models.create_shipping_request

class CreateOrderRequest(object):

    """Implementation of the 'CreateOrderRequest' model.

    Request for creating an order

    Attributes:
        items (list of CreateOrderItemRequest): Items
        customer (CreateCustomerRequest): Customer
        payments (list of CreatePaymentRequest): Payment data
        code (string): The order code
        customer_id (string): The customer id
        shipping (CreateShippingRequest): Shipping data
        metadata (dict<object, string>): Metadata

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "items" : "items",
        "customer" : "customer",
        "payments" : "payments",
        "code" : "code",
        "customer_id" : "customer_id",
        "shipping" : "shipping",
        "metadata" : "metadata"
    }

    def __init__(self,
                 items=None,
                 customer=None,
                 payments=None,
                 code=None,
                 customer_id=None,
                 shipping=None,
                 metadata=None):
        """Constructor for the CreateOrderRequest class"""

        # Initialize members of the class
        self.items = items
        self.customer = customer
        self.payments = payments
        self.code = code
        self.customer_id = customer_id
        self.shipping = shipping
        self.metadata = metadata


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
        items = None
        if dictionary.get("items") != None:
            items = list()
            for structure in dictionary.get("items"):
                items.append(mundiapi.models.create_order_item_request.CreateOrderItemRequest.from_dictionary(structure))
        customer = mundiapi.models.create_customer_request.CreateCustomerRequest.from_dictionary(dictionary.get("customer")) if dictionary.get("customer") else None
        payments = None
        if dictionary.get("payments") != None:
            payments = list()
            for structure in dictionary.get("payments"):
                payments.append(mundiapi.models.create_payment_request.CreatePaymentRequest.from_dictionary(structure))
        code = dictionary.get("code")
        customer_id = dictionary.get("customer_id")
        shipping = mundiapi.models.create_shipping_request.CreateShippingRequest.from_dictionary(dictionary.get("shipping")) if dictionary.get("shipping") else None
        metadata = dictionary.get("metadata")

        # Return an object of this model
        return cls(items,
                   customer,
                   payments,
                   code,
                   customer_id,
                   shipping,
                   metadata)


