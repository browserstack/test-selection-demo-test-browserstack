import pytest

from tests.demo_app.helpers import DemoApp


@pytest.fixture
def demo(selenium):
    return DemoApp(selenium)
