from .models import List, Item
from rest_framework import serializers 



class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'list', 'done', 'url']

class ListSerializer(serializers.HyperlinkedModelSerializer):
    item_set = ItemSerializer(many=True)
    class Meta:
        model = List
        fields = ['id', 'name', 'Usuario', 'done',  'url', 'item_set']