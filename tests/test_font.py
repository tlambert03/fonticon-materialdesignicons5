from qtpy.QtWidgets import QPushButton
from superqt.fonticon import icon

from fonticon_mdi6 import MDI6


def test_FA5S(qtbot):
    btn = QPushButton()
    qtbot.addWidget(btn)
    btn.setIcon(icon(MDI6.sail_boat))
    btn.show()
