import pytest
from flower_data.models import (
    Goal, Timeline, Task
)
from datetime import datetime, timedelta


@pytest.mark.django_db
def test_hello():
    print("found it")


@pytest.fixture
def goal_fixture(
    description="this is a goal!"
):
    return Goal.objects.create(description=description)


@pytest.fixture
def timeline_fixture(
    starts_at=None,
    ends_at=None,
    description="some timeline idk"
):
    return Timeline.objects.create(
        starts_at=starts_at,
        ends_at=ends_at,
        description=description
    )


@pytest.fixture
def task_fixture(
    timeline=None,
    parent_goal=None,
    description="some description idk"
):
    return Task.objects.create(
        timeline=timeline,
        parent_goal=parent_goal,
        description=description
    )


@pytest.mark.django_db
def test_task_simple():

    goal = Goal.objects.create(description="some description")

    timeline = Timeline.objects.create(
        starts_at=datetime.today(),
        ends_at=datetime.today() - timedelta(days=1)

    )

    Task.objects.create(
        timeline=timeline,
        parent_goal=goal,
        description="hail drugs do satan"
    )

    tasks = Task.objects.all()
    assert 1 == tasks.count()

    created_task = tasks.first()
    assert created_task.parent_goal.id == goal.id
    assert created_task.timeline.id == timeline.id
