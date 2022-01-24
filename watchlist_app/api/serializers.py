from rest_framework import serializers
from watchlist_app.models import StreamPlatform, WatchList

class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = '__all__'

class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    # watchlist = serializers.StringRelatedField(many=True)
    # watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # watchlist = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="movie-detail")

    class Meta:
        model = StreamPlatform
        fields = '__all__'