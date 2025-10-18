from __tests.testing_web.context import Context
from instaui import ui, html
from instaui_shiki import shiki


def test_base(context: Context):
    @context.register_page
    def index():
        code = ui.state("print('foo')")

        html.textarea(code)
        shiki(code)

    context.open()
    input = context.find(kind="textbox")

    context.expect(_utils.locator_code_span(context, text="foo")).to_be_visible()

    input.fill("print('bar')")

    context.expect(_utils.locator_code_span(context, text="bar")).to_be_visible()


def test_diff(context: Context):
    @context.register_page
    def index():
        code = ui.state("print('foo') # [!code --]")
        shiki(code, transformers=["notationDiff"])

    context.open()

    # make sure the code is visible
    context.expect(_utils.locator_code_span(context, text="foo")).to_be_visible()

    context.expect(
        _utils.locator_code_span(context, text="[!code --]", exact=False)
    ).to_have_count(0)


class _utils:
    @staticmethod
    def locator_code_span(
        context: Context, *, text: str, exact: bool = True, has_text: bool = True
    ):
        if exact:
            text = context.exact_text(text)  # type: ignore

        args = {"has_text": text} if has_text else {"has_not_text": text}

        return context.find_by_selector("code span").filter(**args)  # type: ignore
