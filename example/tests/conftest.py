import pytest
from model_bakery import baker

pytestmark = [pytest.mark.django_db]


@pytest.fixture
def populated_meeting():
    meeting = baker.make('meetings.Meeting')
    baker.make(
        'meetings.Comment',
        meeting=meeting
    )
    return meeting
