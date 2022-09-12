import pytest

from api.meetings.reversed_relation_serializers import MeetingSerializer

pytestmark = [pytest.mark.django_db]


def test_add_meeting():
    serializer = MeetingSerializer(
        data={
            'title': 'Hello',
            'comments': [
                {
                    'description': 'got bored',
                },
            ]
        }
    )
    assert serializer.is_valid()
    meeting = serializer.save()
    comment = meeting.comments.get()
    assert meeting.title == 'Hello'
    assert meeting.comments.count() == 1
    assert comment.description == 'got bored'


def test_edit_meeting(populated_meeting):

    comment = populated_meeting.comments.get()
    s = MeetingSerializer(
        instance=populated_meeting,
        data={
            'title': 'Hello again',
            'comments': [
                {
                    'pk': comment.pk,
                    'description': 'got very bored',
                }
            ]
        }
    )
    assert s.is_valid()
    meeting = s.save()
    comment = meeting.comments.get()
    assert meeting.title == 'Hello again'
    assert meeting.comments.count() == 1
    assert comment.description == 'got very bored'
