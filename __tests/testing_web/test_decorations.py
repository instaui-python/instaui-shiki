from __tests.testing_web.context import Context
from instaui_shiki import shiki, decorations


def test_base(context: Context):
    @context.register_page
    def index():
        code = r"""
const x = 10
console.log(x)
    """

        shiki(
            code,
            decorations=[
                decorations.decoration(
                    start=decorations.start(line=1, character=0),
                    end=decorations.end(line=1, character=11),
                    properties={"class": "my-mark"},
                )
            ],
        )

    context.open()
    context.expect(context.find_by_selector(".my-mark")).to_have_text("console.log")
