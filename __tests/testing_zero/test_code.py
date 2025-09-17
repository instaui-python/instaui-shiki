from __tests.testing_zero.context import ZeroContext as Context
from instaui import ui, html, zero


def test_base(context: Context):
    def index():
        code = ui.state("print('foo')")

        html.textarea(code)
        ui.code(code)

    context.open(zero().to_html_str(index))

    context.expect(_utils.locator_code_span(context, text="foo")).to_be_visible()


class _utils:
    @staticmethod
    def locator_code_span(
        context: Context, *, text: str, exact: bool = True, has_text: bool = True
    ):
        if exact:
            text = context.exact_text(text)  # type: ignore

        args = {"has_text": text} if has_text else {"has_not_text": text}

        return context.find_by_selector("code span").filter(**args)  # type: ignore
