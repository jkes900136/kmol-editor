# -*- coding: utf-8 -*-

"""Text editor of kmol editor."""

__author__ = "Yuan Chang"
__copyright__ = "Copyright (C) 2018"
__license__ = "AGPL"
__email__ = "pyslvs@gmail.com"

import platform
from typing import Tuple
from re import escape
from core.QtModules import (
    pyqtSignal,
    pyqtSlot,
    Qt,
    QApplication,
    QWidget,
    QFont,
    QFontMetrics,
    QColor,
    #QScintilla widget
    QsciScintilla,
    #Other highlighters
    QSCIHIGHLIGHTERS,
)


_parentheses = (
    (Qt.Key_ParenLeft, '(', ')'),
    (Qt.Key_BracketLeft, '[', ']'),
    (Qt.Key_BraceLeft, '{', '}'),
    (Qt.Key_QuoteDbl, '"', '"'),
    (Qt.Key_Apostrophe, "'", "'"),
)
_parentheses_html = (
    (Qt.Key_Less, '<', '>'),
)
_parentheses_markdown = (
    (Qt.Key_Dollar, '$', '$'),
    (Qt.Key_Asterisk, '*', '*'),
    (Qt.Key_Underscore, '_', '_'),
    _parentheses_html[0],
)
_commas = (
    Qt.Key_Comma,
)
_commas_markdown = (
    Qt.Key_Semicolon,
    Qt.Key_Colon,
    Qt.Key_Period,
)


class TextEditor(QsciScintilla):
    
    """QScintilla text editor."""
    
    currentWordChanged = pyqtSignal(str)
    
    def __init__(self, parent: QWidget):
        """UI settings."""
        super(TextEditor, self).__init__(parent)
        
        #Set the default font.
        if platform.system().lower() == "windows":
            font_name = "Courier New"
        else:
            font_name = "Mono"
        self.font = QFont(font_name)
        self.font.setFixedPitch(True)
        self.font.setPointSize(14)
        self.setFont(self.font)
        self.setMarginsFont(self.font)
        self.setUtf8(True)
        
        #Margin 0 is used for line numbers.
        fontmetrics = QFontMetrics(self.font)
        self.setMarginsFont(self.font)
        self.setMarginWidth(0, fontmetrics.width("0000") + 4)
        self.setMarginLineNumbers(0, True)
        self.setMarginsBackgroundColor(QColor("#cccccc"))
        
        #Brace matching.
        self.setBraceMatching(QsciScintilla.SloppyBraceMatch)
        
        #Current line visible with special background color.
        self.setCaretLineVisible(True)
        self.setCaretLineBackgroundColor(QColor("#ffe4e4"))
        
        #Set lexer.
        self.setHighlighter("Markdown")
        self.SendScintilla(
            QsciScintilla.SCI_STYLESETFONT,
            1,
            font_name.encode('utf-8')
        )
        
        #Don't want to see the horizontal scrollbar at all.
        self.setWrapMode(QsciScintilla.WrapWord)
        self.SendScintilla(QsciScintilla.SCI_SETHSCROLLBAR, 0)
        
        #Auto completion.
        self.setAutoCompletionCaseSensitivity(True)
        self.setAutoCompletionSource(QsciScintilla.AcsDocument)
        self.setAutoCompletionThreshold(1)
        
        #Edge mode.
        self.setEdgeMode(QsciScintilla.EdgeNone)
        self.setEdgeColumn(80)
        self.setEdgeColor(Qt.blue)
        
        #Indentations.
        self.setAutoIndent(True)
        self.setIndentationsUseTabs(False)
        self.setTabWidth(4)
        self.setTabIndents(True)
        self.setBackspaceUnindents(True)
        self.setIndentationGuides(True)
        
        #Indicator.
        self.indicatorDefine(QsciScintilla.BoxIndicator, 0)
        self.SendScintilla(QsciScintilla.SCI_SETINDICATORCURRENT, 0)
        self.cursorPositionChanged.connect(self.__catchWord)
        
        #Widget size.
        self.setMinimumSize(400, 450)
    
    @pyqtSlot(str)
    def setHighlighter(self, option: str):
        """Set highlighter by list."""
        self.lexer_option = option
        lexer = QSCIHIGHLIGHTERS[option]()
        lexer.setDefaultFont(self.font)
        self.setLexer(lexer)
    
    @pyqtSlot(bool)
    def setEdgeMode(self, option: bool):
        """Set edge mode option."""
        super(TextEditor, self).setEdgeMode(
            QsciScintilla.EdgeLine if option else QsciScintilla.EdgeNone
        )
    
    def __clearAllIndicator(self):
        """Clear all indicator."""
        self.clearIndicatorRange(0, 0, *self.lineIndexFromPosition(self.length()), 0)
    
    def __currentWordPosition(self) -> Tuple[int, int, str]:
        """Return pos of current word."""
        pos = self.positionFromLineIndex(*self.getCursorPosition())
        wpos_start = self.SendScintilla(QsciScintilla.SCI_WORDSTARTPOSITION, pos, True)
        wpos_end = self.SendScintilla(QsciScintilla.SCI_WORDENDPOSITION, pos, True)
        return wpos_start, wpos_end, self.text()[wpos_start:wpos_end]
    
    def __catchAllWords(self, text: str):
        """Catch all of words that is same with current word."""
        t_len = len(text)
        if not t_len:
            return
        doc = self.text()
        pos = 0
        while True:
            new_pos = doc[pos:].find(text)
            if new_pos == -1:
                break
            pos += new_pos
            
            #Boundle check
            start = doc[pos - 1] if pos else " "
            end = doc[pos + t_len] if (pos + t_len) != len(doc) else " "
            if len(escape(start)) != len(start) and len(escape(end)) != len(end):
                self.fillIndicatorRange(
                    *self.lineIndexFromPosition(pos),
                    *self.lineIndexFromPosition(pos + t_len),
                    0
                )
            
            pos += t_len
    
    @pyqtSlot(int, int)
    def __catchWord(self, line: int, index: int):
        """Catch and indicate current word."""
        self.__clearAllIndicator()
        wpos_start, wpos_end, text = self.__currentWordPosition()
        self.currentWordChanged.emit(text)
        self.fillIndicatorRange(
            *self.lineIndexFromPosition(wpos_start),
            *self.lineIndexFromPosition(wpos_end),
            0
        )
        self.__catchAllWords(text)
    
    def wheelEvent(self, event):
        """Mouse wheel event."""
        if QApplication.keyboardModifiers() != Qt.ControlModifier:
            super(TextEditor, self).wheelEvent(event)
            return
        if event.angleDelta().y() >= 0:
            self.zoomIn()
        else:
            self.zoomOut()
    
    def keyPressEvent(self, event):
        """Input key event."""
        key = event.key()
        text = self.selectedText()
        
        #Commas and parentheses.
        parentheses = list(_parentheses)
        commas = list(_commas)
        if self.lexer_option == "Markdown":
            parentheses.extend(_parentheses_markdown)
            commas.extend(_commas_markdown)
        elif self.lexer_option == "HTML":
            parentheses.extend(_parentheses_html)
            commas.extend(_commas_markdown)
        
        #Wrap the selected text.
        if text:
            for match_key, t0, t1 in parentheses:
                if key == match_key:
                    self.replaceSelectedText(t0 + text + t1)
                    return
        
        super(TextEditor, self).keyPressEvent(event)
        
        #Auto close of parentheses.
        for match_key, t0, t1 in parentheses:
            if key == match_key:
                self.insert(t1)
                return
        
        #Add space for commas.
        for co in commas:
            if key == co:
                self.insert(" ")
                line, index = self.getCursorPosition()
                self.setCursorPosition(line, index + 1)
                return
