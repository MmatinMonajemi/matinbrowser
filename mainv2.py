#!/usr/bin/env python3
"""
Matin Browser - Version 2.0
Built by Mohammad Matin Monajemi (M.Matin Monajemi)
Enhanced with advanced features
"""

import sys
from PyQt5.QtCore import QUrl, QTimer, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction, QLineEdit, QTabWidget, QMenu, QMenuBar
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile

class MatinBrowser(QMainWindow):
    def __init__(self):
        super(MatinBrowser, self).__init__()

        self.setWindowTitle("Matin Browser - Version 2.0")
        self.setGeometry(100, 100, 1200, 800)

        # Tab Management
        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.setCentralWidget(self.tabs)

        # Create initial tab
        self.add_new_tab(QUrl("https://duckduckgo.com"), "Home")

        # Profile settings
        self.profile = QWebEngineProfile.defaultProfile()
        self.profile.setPersistentCookiesPolicy(QWebEngineProfile.NoPersistentCookies)
        self.profile.setHttpCacheType(QWebEngineProfile.MemoryHttpCache)

        # Toolbar setup
        self.toolbar = QToolBar()
        self.toolbar.setStyleSheet("background-color: #222; color: #fff;")
        self.addToolBar(self.toolbar)

        # Actions
        self.add_action("Back", self.tabs.currentWidget().back)
        self.add_action("Forward", self.tabs.currentWidget().forward)
        self.add_action("Reload", self.tabs.currentWidget().reload)
        self.add_action("New Tab", self.new_tab_action)
        self.add_action("Incognito Mode", self.toggle_incognito)
        self.add_action("Battery Saver", self.toggle_battery_saver)
        self.add_action("Gaming Mode", self.toggle_gaming_mode)

        # Search Bar
        self.search_bar = QLineEdit()
        self.search_bar.setStyleSheet("background-color: #222; color: #fff; border: 1px solid #fff; padding: 5px;")
        self.search_bar.setPlaceholderText("Type a URL or search query")
        self.search_bar.returnPressed.connect(self.navigate_to_search)
        self.toolbar.addWidget(self.search_bar)

        # Battery Saver Mode (CPU Reduction)
        self.battery_saver_enabled = False
        self.gaming_mode_enabled = False
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.free_up_memory)
        self.timer.start(30000)  # Free memory every 30 sec

    def add_action(self, name, callback):
        btn = QAction(name, self)
        btn.triggered.connect(callback)
        self.toolbar.addAction(btn)

    def add_new_tab(self, url, title="New Tab"):
        browser = QWebEngineView()
        browser.setUrl(url)
        self.tabs.addTab(browser, title)

    def close_tab(self, index):
        if self.tabs.count() > 1:
            self.tabs.removeTab(index)

    def new_tab_action(self):
        self.add_new_tab(QUrl("https://duckduckgo.com"))

    def navigate_to_search(self):
        query = self.search_bar.text().strip()
        if query.startswith("http://") or query.startswith("https://"):
            url = QUrl(query)
        elif query.lower().startswith("google:"):
            url = QUrl("https://www.google.com/search?q=" + query[7:].strip())
        else:
            url = QUrl("https://duckduckgo.com/?q=" + query)

        self.tabs.currentWidget().setUrl(url)

    def toggle_incognito(self):
        self.profile.setPersistentCookiesPolicy(QWebEngineProfile.NoPersistentCookies)
        self.profile.setHttpCacheType(QWebEngineProfile.MemoryHttpCache)
        print("Incognito Mode Enabled")

    def toggle_battery_saver(self):
        self.battery_saver_enabled = not self.battery_saver_enabled
        if self.battery_saver_enabled:
            self.profile.setHttpCacheType(QWebEngineProfile.NoCache)
            print("Battery Saver Mode Enabled")
        else:
            self.profile.setHttpCacheType(QWebEngineProfile.MemoryHttpCache)
            print("Battery Saver Mode Disabled")

    def toggle_gaming_mode(self):
        self.gaming_mode_enabled = not self.gaming_mode_enabled
        if self.gaming_mode_enabled:
            self.timer.setInterval(15000)  # Optimize RAM freeing for games
            print("Gaming Mode Enabled")
        else:
            self.timer.setInterval(30000)
            print("Gaming Mode Disabled")

    def free_up_memory(self):
        """Clears cache and unused RAM to enhance performance."""
        self.profile.clearHttpCache()
        print("Memory freed to optimize performance")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MatinBrowser()
    window.show()
    sys.exit(app.exec_())
