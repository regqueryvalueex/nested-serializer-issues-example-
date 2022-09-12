from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

from meetings.models import Meeting, Comment


class MeetingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meeting
        fields = (
            'pk',
            'title',
        )


class CommentSerializer(WritableNestedModelSerializer):
    meeting = MeetingSerializer()

    class Meta:
        model = Comment
        fields = (
            'pk',
            'description',
            'meeting',
        )
