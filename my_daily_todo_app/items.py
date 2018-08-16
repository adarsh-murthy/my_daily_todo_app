"""Controller for the items resource."""
import falcon

import json


from .exceptions import NotAuthorizedException, ObjectDoesNotExist
from .models import Item, User


class Items(object):
    """
    Provide easy interface to interact with the items database table.
    """

    def _as_dict(self, item):
        """
        Convert a peevee item instance to a dictionary.
        """
        return {
            'id': item.id,
            'description': item.description,
            'is_complete': item.is_complete,
            'create_date': item.create_date,
        }

    def get_items_for_user(self, user):
        """
        Returns list of items for a given user.
        """
        items = Item.select().join(User).where(User.username == user.username)
        results = []
        for item in items:
            results.append(self._as_dict(item))
        return results

    def get_item_for_user(self, user, pk):
        """
        Returns item corresponding to the item ID requested.
        """
        try:
            item = Item.get_by_id(pk)
        except Exception:
            return {}
        if item.user.username != user.username:
            return {}
        return self._as_dict(item)

    def create_item_for_user(user, description):
        """
        Creates an item for a user and returns the ID of the created item.
        """
        pass

    def _update_item_description(self, item, description):
        """
        Helper method to update description of an item. This first checks
        if the description is not None before updating.
        """
        if description is None:
            return
        item.description = description
        item.save()

    def _update_item_is_complete(self, item, is_complete):
        """
        Helper method to update is_complete of an item. This first checks
        if the description is not None before updating.
        """
        if is_complete is None:
            return
        item.is_complete = is_complete
        item.save()

    def update_item_for_user(self, user, pk, **kwargs):
        """
        Update the item for the given user with the new values passed as
        key-word arguments.
        """
        try:
            item = Item.get_by_id(pk)
        except Exception:
            raise ObjectDoesNotExist('Could not find item for given id')
        if item.user.username != user.username:
            raise NotAuthorizedException('User does not own item')
        description = kwargs.get('description', None)
        self._update_item_description(item, description)
        is_complete = kwargs.get('is_complete', None)
        self._update_item_is_complete(item, is_complete)


class ItemsResource(object):

    def __init__(self):
        self.items = Items()

    def on_get(self, request, response):
        """GET method on items.
        Gets list of items for the user and returns them.
        """
        # Grab the user from the request.
        user = request.context['user']

        # Get all the items for the given user.
        items = self.items.get_items_for_user(user)

        # Return the list in JSON format.
        response.body = json.dumps(items)

    def on_post(self, request, response):
        """POST method on items.
        Create a new item for a given user.
        """
        # Grab the user from the request.
        user = request.context['user']

        # Read the request stream as JSON.
        body = json.load(request.stream)

        # Extract the description from the body.
        description = body.get('description', None)
        if not description:
            # If no description was provided, respond as BAD REQUEST.
            response.status = falcon.HTTP_400
            message = {'message': 'Could not find description in POST body'}
            response.body = json.dumps(message)
            return

        # Create the item for the user with given description.
        item_id = self.items.create_item_for_user(user, description)

        # Return the created ID as response.
        message = {'id': item_id}
        response.status = falcon.HTTP_201
        response.body = json.dumps(message)
