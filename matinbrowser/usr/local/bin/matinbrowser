#!/usr/bin/env python3
"""
Matin Browser
Built by Mohammad Matin Monajemi (M.Matin Monajemi)
"""

import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction, QLineEdit
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # Set window title and dimensions
        self.setWindowTitle("Matin Browser")
        self.setGeometry(100, 100, 1200, 800)
        
        # Create the browser widget
        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)
        
        # Configure profile to not store cookies or cache permanently
        profile = QWebEngineProfile.defaultProfile()
        profile.setPersistentCookiesPolicy(QWebEngineProfile.NoPersistentCookies)
        profile.setHttpCacheType(QWebEngineProfile.MemoryHttpCache)
        
        # Create a toolbar
        self.toolbar = QToolBar()
        # Set style of the toolbar: black background with yellow text
        self.toolbar.setStyleSheet("background-color: black; color: yellow;")
        self.addToolBar(self.toolbar)
        
        # Back button
        back_btn = QAction("Back", self)
        back_btn.triggered.connect(self.browser.back)
        self.toolbar.addAction(back_btn)

        # Forward button
        forward_btn = QAction("Forward", self)
        forward_btn.triggered.connect(self.browser.forward)
        self.toolbar.addAction(forward_btn)

        # Reload button
        reload_btn = QAction("Reload", self)
        reload_btn.triggered.connect(self.browser.reload)
        self.toolbar.addAction(reload_btn)

        # Create search bar for entering URL or search query
        self.search_bar = QLineEdit()
        self.search_bar.setStyleSheet("background-color: black; color: yellow; border: 1px solid yellow; padding: 5px;")
        self.search_bar.setPlaceholderText("Type a URL or search query (use 'google:' for Google search)")
        self.search_bar.returnPressed.connect(self.navigate_to_search)
        self.toolbar.addWidget(self.search_bar)
        
        # Set default page to DuckDuckGo for searches
        self.browser.setUrl(QUrl("https://duckduckgo.com"))

    def navigate_to_search(self):
        query = self.search_bar.text().strip()
        if not query:
            return
        # If query starts with http(s), treat it as a direct URL
        if query.startswith("http://") or query.startswith("https://"):
            url = QUrl(query)
        else:
            # If query starts with 'google:', perform a Google search
            if query.lower().startswith("google:"):
                q = query[7:].strip()
                url = QUrl("https://www.google.com/search?q=" + q)
            else:
                # Otherwise, perform a search on DuckDuckGo
                url = QUrl("https://duckduckgo.com/?q=" + query)
        self.browser.setUrl(url)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
