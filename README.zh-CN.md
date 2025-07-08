# instaui-shiki

<div align="center">

简体中文| [English](./README.en.md)

</div>
 
## 📖 介绍
instaui-shiki 是一个使用 Shiki 在浏览器中高亮显示代码片段的 Python 库。


## ⚙️ 安装

```bash
pip install instaui-shiki
```

## 🖥️ 使用
```python
from instaui import ui

@ui.page("/")
def test_page():
    ui.code("print('foo')")


ui.server().run()
```