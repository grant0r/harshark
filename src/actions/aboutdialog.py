import os

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QPlainTextEdit
from PyQt5.QtWidgets import QWidget


class AboutDialog(QDialog):

    LICENSE_TEXT = """MIT License

Copyright (c) 2018 Mark Riddell

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

    INFO_TEXT = """Harshark: A simple offline HAR viewer.

---------------------------------------------------------------------
Release 2.3.1 (6-Apr-2018)
---------------------------------------------------------------------
NEW FEATURES:
N/A

BUG FIXES:
Fixed bug where query strings weren't included in the 'path' column
for requests.

NOTES:
N/A

---------------------------------------------------------------------
Release 2.3.0 (31-Mar-2018)
---------------------------------------------------------------------
NEW FEATURES:
* Hostname, Port and Path are now being extracted from the request URL
and can be now be displayed in their own columns.

BUG FIXES:
N/A

NOTES:
N/A

---------------------------------------------------------------------
Release 2.2.2 (22-Mar-2018)
---------------------------------------------------------------------
NEW FEATURES:
N/A

BUG FIXES:
* Fixed [Issue-5](https://github.com/MacroPolo/harshark/issues/5) so
that global search is no longer also searching in dict keys. Search corpus 
is now values only.
* Handle POST data found in parameter field rather than just looking for
raw text.
* Handle keyless query strings which are recorded as null is HAR files.
* Default styling changes.

NOTES:
N/A

---------------------------------------------------------------------
Release 2.2.1 (28-Feb-2018)
---------------------------------------------------------------------
NEW FEATURES:
N/A

BUG FIXES:
Fixed bug where SAML requests wouldn't be parsed because there was 
URI (precent) encoded characters in the Base64. Now we replace any
Base64 special character which has been URI encoded in both SAML
request and response ('/', '+', '=' and newline)

NOTES:
N/A

---------------------------------------------------------------------
Release 2.2.0 (24-Feb-2018)
---------------------------------------------------------------------
NEW FEATURES:
* Various styling updates including a new default UI font and colours.
* SAML parsing is now enabled by default and is no longer classed as
experimental.

BUG FIXES:
N/A

NOTES:
N/A

---------------------------------------------------------------------
Release 2.1.1 (16-Feb-2018)
---------------------------------------------------------------------
NEW FEATURES:
N/A

BUG FIXES:
* Using a new XML parser so SAML pretty printing should now be more
consistent.
* Fixed bug where program would crash when a HAR file had URLs with a
URI scheme other than HTTP/S. Now we support things like WS, WSS, FTP
etc. Also Added a few new default colours for WS, WSS and FTP schemes.
* Fixed a bug where null values in cache objects would cause the program
to crash. 
* Cache object parsing has now been disabled as it is not used at
present.

NOTES:
N/A

---------------------------------------------------------------------
Release 2.1.0 (15-Feb-2018)
---------------------------------------------------------------------
NEW FEATURES:
* SAML parsing is now a lot more robust and should be able to handle a 
wider variety of inputs. Feature is staying as experimental for now
until it has been tested further.
* SAML request and response content is now pretty printed.

BUG FIXES:
* SAML Response content now correctly shows in the Request tab group
rather than the response group.

NOTES:
N/A

---------------------------------------------------------------------
Release 2.0.2 (14-Feb-2018)
---------------------------------------------------------------------
NEW FEATURES:
N/A

BUG FIXES:
* Entries table no longer gets out of sync after sorting columns when importing a new HAR file.
* Previous search results are now cleared when opening a new HAR file.
* Un-truncating body content after a search has been applied no longer highlights all text.
* Statusbar now shows search result details even when the active row is not the first row.

NOTES:
N/A

---------------------------------------------------------------------
Release 2.0.1 (8-Feb-2018)
---------------------------------------------------------------------
NEW FEATURES:
N/A

BUG FIXES:
* SAML parsing failures should no longer crash the program. Instead, the SAML request/response 
tab will indicate that we weren't able to parse the SAML.

NOTES:
N/A

---------------------------------------------------------------------
Release 2.0.0 (4-Feb-2018)
---------------------------------------------------------------------
NEW FEATURES:
* Complete code rebuild from Harshark 1.
* Open, view and analyse HAR files complient with the v1.1 and v1.2 standard.
* Customise which columns you would like to view.
* Cell colourization for interesting information (status code, protocol etc).
* View detailed request and response information for each entry found in the HAR file.
* Sort request and response headers alphabetically.
* Ability to search for keywords across all entries and also within a single entry.
* [Experimental] SAML Request and Response parsing.

BUG FIXES:
N/A

NOTES:
N/A"""

    def __init__(self, app):
        super().__init__()
        self.app = app
        self.initWidget()

    def initWidget(self):

        with open(self.app.stylesheet_path, 'r') as f:
            self.setStyleSheet(f.read())

        button_ok = QPushButton('OK', self)
        button_ok.clicked.connect(self.okPressed)

        about_tabs = QTabWidget()
        info_tab = QWidget()
        license_tab = QWidget()

        about_tabs.addTab(info_tab, 'Release Notes')
        about_tabs.addTab(license_tab, 'License')

        info_tab_layout = QVBoxLayout()
        license_tab_layout = QVBoxLayout()

        info_tab_text = QPlainTextEdit(readOnly=True)
        license_tab_text = QPlainTextEdit(readOnly=True)

        info_tab_layout.addWidget(info_tab_text)
        info_tab.setLayout(info_tab_layout)

        license_tab_layout.addWidget(license_tab_text)
        license_tab.setLayout(license_tab_layout)

        info_tab_text.setPlainText(AboutDialog.INFO_TEXT)
        license_tab_text.setPlainText(AboutDialog.LICENSE_TEXT)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(about_tabs)
        main_layout.addWidget(button_ok)

        self.setLayout(main_layout)
        self.setWindowTitle("About Harshark")
        self.setWindowIcon(self.app.about_icon)
        self.setWindowModality(Qt.ApplicationModal)
        self.resize(700 , 400)
        self.exec_()

    def okPressed(self):
        self.close()
