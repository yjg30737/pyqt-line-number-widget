from PyQt5.QtGui import QFont, QTextCursor
from PyQt5.QtWidgets import QTextBrowser
from PyQt5.QtCore import Qt


class LineNumberWidget(QTextBrowser):
    def __init__(self, widget):
        super().__init__()
        self.__lineCount = widget.document().lineCount()
        self.__initUi(widget)

    def __initUi(self, widget):
        size = widget.font().pointSize()

        self.setStyleSheet('QTextBrowser { background: transparent; border: none; color: #AAA }'
                           'QTextBrowser::hover { background: color: #DDD; }')

        self.__setFontSizeAsPrivate(size)

        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalScrollBar().setEnabled(False)

        widget.verticalScrollBar().valueChanged.connect(self.__changeLineWidgetScrollAsTargetedWidgetScrollChanged)

        self.__initLineCount()

    def __setFontSizeAsPrivate(self, size):
        self.setFontPointSize(size)
        self.setFixedWidth(size*5)

    def __setFontSizeAsRatePrivate(self, size: float):
        new_size = self.fontPointSize()*size

        # font we already had
        font = QFont(self.currentFont().family(), new_size)
        self.setFont(font)

        # font that would be added
        self.setFontPointSize(new_size)
        self.setFixedWidth(int(new_size)*5)

    def __changeLineWidgetScrollAsTargetedWidgetScrollChanged(self, v):
        self.verticalScrollBar().setValue(v)

    def __initLineCount(self):
        for n in range(1, self.__lineCount+1):
            self.append(str(n))

    def changeLineCount(self, n):
        max_one = max(self.__lineCount, n)
        diff = n-self.__lineCount
        if max_one == self.__lineCount:
            for i in range(self.__lineCount, self.__lineCount + diff, -1):
                self.moveCursor(QTextCursor.End, QTextCursor.MoveAnchor)
                self.moveCursor(QTextCursor.StartOfLine, QTextCursor.MoveAnchor)
                self.moveCursor(QTextCursor.End, QTextCursor.KeepAnchor)
                self.textCursor().removeSelectedText()
                self.textCursor().deletePreviousChar()
        else:
            for i in range(self.__lineCount, self.__lineCount + diff, 1):
                self.append(str(i + 1))

        self.__lineCount = n

    def setFontSizeAsRate(self, size: float):
        self.__setFontSizeAsRatePrivate(size)

    def setValue(self, v):
        self.verticalScrollBar().setValue(v)

