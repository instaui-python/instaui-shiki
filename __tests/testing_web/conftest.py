import pytest
from playwright.sync_api import Browser
from __tests.testing_web.context import Context
from __tests.testing_web.server import TestServer


@pytest.fixture(scope="function")
def context(browser: Browser, start_server: TestServer):
    page = browser.new_page()
    start_server.start()
    start_server.wait_for_connection()
    context = Context(start_server, page)

    yield context

    page.close()


@pytest.fixture(scope="session", autouse=True)
def start_server():
    server = TestServer()
    yield server
    server.stop()
