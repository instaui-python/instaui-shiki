import typing
from time import sleep
from playwright.sync_api import Page, Error
from .server import TestServer
from __tests.screen import BaseContext


class Context(BaseContext):
    num = 0

    def __init__(
        self,
        test_server: TestServer,
        page: Page,
    ) -> None:
        super().__init__(page)
        self.num = Context.num
        Context.num += 1

        self._test_server = test_server
        self._root_path = test_server.url
        self._path = f"/{self.num}"

    @typing.overload
    def register_page(self, fn: typing.Callable): ...

    @typing.overload
    def register_page(
        self,
        *,
        path: typing.Optional[str] = None,
        cache: bool = False,
    ): ...

    def register_page(
        self,
        fn: typing.Optional[typing.Callable] = None,
        *,
        path: typing.Optional[str] = None,
        cache: bool = False,
    ):
        if fn is None:

            def wrapper(fn: typing.Callable):
                self.register_page(
                    fn,
                    path=path,
                )  # type: ignore

            return wrapper

        self._test_server._server._runtime.backend.register_dynamic_page(
            self._path + (path or ""), fn, cache=cache
        )

    @property
    def path(self) -> str:
        return self._path

    def open(self) -> None:
        url = self._root_path + self._path
        goto_with_retry(self.page, url)

    def open_by_path(self, path: str) -> None:
        url = self._root_path + self._path + path
        goto_with_retry(self.page, url)


def goto_with_retry(page: Page, url: str, retries=5):
    for i in range(retries):
        try:
            return page.goto(url, wait_until="load")
        except Error:
            if i == retries - 1:
                raise
            sleep(1)
