from coapthon.messages.response import Response
from coapthon import defines


class RequestLayer(object):
    def __init__(self, server):
        self._server = server

    def send_empty(self, transaction, message):
        """

        :type transaction: Transaction
        :param transaction:
        :type message: Message
        :param message:
        """
        pass

    def receive_response(self, response, transaction):
        """

        :type response: Response
        :param response:
        :type transaction: Transaction
        :param transaction:
        :rtype : Transaction
        """
        raise NotImplementedError

    def send_response(self, transaction, response):
        """

        :type transaction: Transaction
        :param transaction:
        :type response: Response
        :param response:
        """
        pass

    def receive_request(self, transaction):
        """

        :type transaction: Transaction
        :param transaction:
        :rtype : Transaction
        """
        method = transaction.request.code
        if method == defines.Codes.GET.number:
            transaction = self._handle_get(transaction)
        elif method == defines.Codes.POST.number:
            transaction = self._handle_post(transaction)
        elif method == defines.Codes.PUT.number:
            transaction = self._handle_put(transaction)
        elif method == defines.Codes.DELETE.number:
            transaction = self._handle_delete(transaction)
        else:
            transaction.response = None
        return transaction

    def receive_empty(self, empty, transaction):
        """

        :type empty: Message
        :param empty:
        :type transaction: Transaction
        :param transaction:
        :rtype : Transaction
        """
        raise NotImplementedError

    def send_request(self, request):
        """

        :type request: Request
        :param request:
        """
        return request

    def _handle_get(self, transaction):
        """

        :type transaction: Transaction
        :param transaction:
        :rtype : Transaction
        """
        path = str("/" + transaction.request.uri_path)
        transaction.response = Response()
        transaction.response.destination = transaction.request.source
        transaction.response.token = transaction.request.token
        if path == defines.DISCOVERY_URL:
            transaction = self._server.resourceLayer.discover(transaction)
        else:
            try:
                resource = self._server.root[path]
            except KeyError:
                resource = None
            if resource is None or path == '/':
                # Not Found
                transaction.response.code = defines.Codes.NOT_FOUND.number
            else:
                transaction.resource = resource
                transaction = self._server.resourceLayer.get_resource(transaction)
        return transaction

    def _handle_put(self, transaction):
        """

        :type transaction: Transaction
        :param transaction:
        :rtype : Transaction
        """
        path = str("/" + transaction.request.uri_path)
        transaction.response = Response()
        transaction.response.destination = transaction.request.source
        transaction.response.token = transaction.request.token
        try:
            resource = self._server.root[path]
        except KeyError:
            resource = None
        if resource is None:
            transaction.response.code = defines.Codes.NOT_FOUND.number
        else:
            transaction.resource = resource
            # Update request
            transaction = self._server.resourceLayer.update_resource(transaction)
        return transaction

    def _handle_post(self, transaction):
        """

        :type transaction: Transaction
        :param transaction:
        :rtype : Transaction
        """
        path = str("/" + transaction.request.uri_path)
        transaction.response = Response()
        transaction.response.destination = transaction.request.source
        transaction.response.token = transaction.request.token

        # Create request
        transaction = self._server.resourceLayer.create_resource(path, transaction)
        return transaction

    def _handle_delete(self, transaction):
        """

        :type transaction: Transaction
        :param transaction:
        :rtype : Transaction
        """
        path = str("/" + transaction.request.uri_path)
        transaction.response = Response()
        transaction.response.destination = transaction.request.source
        transaction.response.token = transaction.request.token
        try:
            resource = self._server.root[path]
        except KeyError:
            resource = None

        if resource is None:
            transaction.response.code = defines.Codes.NOT_FOUND.number
        else:
            # Delete
            transaction.resource = resource
            transaction = self._server.resourceLayer.delete_resource(transaction, path)
        return transaction

