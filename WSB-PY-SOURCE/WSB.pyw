from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.browser = QWebEngineView()

        self.browser.setUrl(QUrl("http://wispace.ru"))
        self.browser.urlChanged.connect(self.update_urlbar)
        self.browser.loadFinished.connect(self.update_title)
        self.setCentralWidget(self.browser)

        self.status = QStatusBar()
        self.setStatusBar(self.status)
        navtb = QToolBar("Навигация")
        self.addToolBar(navtb)
        back_btn = QAction("Назад", self)

        back_btn.setStatusTip("Вернуться назад")
        back_btn.triggered.connect(self.browser.back)
        navtb.addAction(back_btn)
        next_btn = QAction("Вперёд", self)
        next_btn.setStatusTip("Вернутся вперёд")
        next_btn.triggered.connect(self.browser.forward)
        navtb.addAction(next_btn)
        reload_btn = QAction("Перезагрузить", self)
        reload_btn.setStatusTip("Перезагрузка страницы")
        reload_btn.triggered.connect(self.browser.reload)
        navtb.addAction(reload_btn)
        home_btn = QAction("Домой", self)
        home_btn.setStatusTip("Домашняя страница")
        home_btn.triggered.connect(self.navigate_home)
        navtb.addAction(home_btn)
        navtb.addSeparator()
        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)

        navtb.addWidget(self.urlbar)

        stop_btn = QAction("Стоп", self)
        stop_btn.setStatusTip("Остановить загрузку текущей страницы")

        stop_btn.triggered.connect(self.browser.stop)
        navtb.addAction(stop_btn)

        self.show()

    def update_title(self):
        title = self.browser.page().title()
        self.setWindowTitle("% s - WSB" % title)

    def navigate_home(self):
        self.browser.setUrl(QUrl("http://wispace.ru"))
    def navigate_to_url(self):
        q = QUrl(self.urlbar.text())

        if q.scheme() == "":
            q.setScheme("http")
        self.browser.setUrl(q)

    def update_urlbar(self, q):
        # setting text to the url bar
        self.urlbar.setText(q.toString())

        # setting cursor position of the url bar
        self.urlbar.setCursorPosition(0)


app = QApplication(sys.argv)
app.setApplicationName("WSB")
window = MainWindow()

app.exec_()