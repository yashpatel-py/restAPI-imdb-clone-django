from rest_framework import serializers
from watchlist_app.models import StreamPlatform, WatchList

class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = '__all__'

class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    # watchlist = serializers.HyperlinkedIdentityField(view_name='platform-list')
    class Meta:
        model = StreamPlatform
        fields = '__all__'