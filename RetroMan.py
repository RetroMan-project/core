# This code creates a MainWindow class with three buttons to call the scan, scan_device, and scrape functions,
# as well as three text fields for the user to enter the roms path, device name, and friendly name.
# When the buttons are clicked, the corresponding function is called with the user-specified parameters,
# and a message is shown to the user when the function is complete.

# To use this code, you will need to create a mainwindow.ui file using Qt Designer, which should contain the three buttons, three text fields, and any other UI elements that you want to include in the main window. Once you have created the mainwindow.ui file, you can run this code to create the main window and use the buttons to call the scan, scan_device, and scrape functions with the user-specified parameters.

from PyQt5 import QtWidgets, uic
from func/load_device import load_device

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('mainwindow.ui', self)

        # connect the buttons to their respective functions
        self.scanButton.clicked.connect(self.scan)
        self.scanDeviceButton.clicked.connect(self.scan_device)
        self.scrapeButton.clicked.connect(self.scrape)

    def scan(self):
        # get the roms path from the text field
        roms_path = self.romsPathTextField.text()
        # call the scan function to generate the gamelist.xml files
        scan('library', roms_path)
        # show a message to the user
        QtWidgets.QMessageBox.information(self, 'Scan', 'Scan complete!')

    def scan_device(self):
        # get the roms path, device name, and friendly name from the text fields
        roms_path = self.romsPathTextField.text()
        device_name = self.deviceNameTextField.text()
        friendly_name = self.friendlyNameTextField.text()
        # call the scan_device function to generate the gamelist.xml files for the device
        scan_device(roms_path, device_name, friendly_name)
        # show a message to the user
        QtWidgets.QMessageBox.information(self, 'Scan Device', 'Scan complete!')

    def scrape(self):
        # get the roms path from the text field
        roms_path = self.romsPathTextField.text()
        # call the scrape function to scrape the missing data for each system's roms
        scrape(roms_path)
        # show a message to the user
        QtWidgets.QMessageBox.information(self, 'Scrape', 'Scrape complete!')

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()


# Here are the steps to create the UI file and integrate it with the Python code:

# 1. Open Qt Designer and create a new main window with three buttons (Scan, Scan Device, and Scrape),
#   three text fields (Roms Path, Device Name, and Friendly Name), and any other UI elements that you want to include
#   in the main window.

# 2. Save the main window as mainwindow.ui in the same directory as the Python code that we defined earlier.

# 3. In the Python code, import the uic module from PyQt5 and use the uic.loadUi method to load the mainwindow.ui file into the
#   MainWindow class.

# 4. Use the clicked.connect method to connect the buttons in the main window to their respective functions
#   (scan, scan_device, and scrape) in the MainWindow class.

# 5. In the scan, scan_device, and scrape functions, use the text() method to get the values from the text fields in the main window,
#   and call the scan, scan_device, and scrape functions with these values as parameters.

# 6. Show a message to the user using the QtWidgets.QMessageBox.information method when the scan, scan_device,
#   and scrape functions are complete.

# Here is an example of how this could be implemented in the Python code:

# from PyQt5 import QtWidgets, uic
