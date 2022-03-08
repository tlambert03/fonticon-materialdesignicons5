# fonticon-materialdesignicons6

[![License](https://img.shields.io/pypi/l/fonticon-materialdesignicons6.svg?color=green)](https://github.com/tlambert03/fonticon-materialdesignicons6/raw/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/fonticon-materialdesignicons6.svg?color=green)](https://pypi.org/project/fonticon-materialdesignicons6)
[![Python Version](https://img.shields.io/pypi/pyversions/fonticon-materialdesignicons6.svg?color=green)](https://python.org)


Material Design Icons extension for superqt font icons

https://github.com/templarian/MaterialDesign

```sh
pip install superqt fonticon-materialdesignicons6
```

```python
from fonticon_mdi6 import MDI6
from qtpy.QtCore import QSize
from qtpy.QtWidgets import QApplication, QPushButton
from superqt.fonticon import icon, pulse

app = QApplication([])

btn2 = QPushButton()
btn2.setIcon(icon(MDI6.fan, animation=pulse(btn2)))
btn2.setIconSize(QSize(225, 225))
btn2.show()

app.exec_()
```
