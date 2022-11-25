"""
Author: Yahia Mostafa
Date : 25/11/2022
"""


import sys  
from PyQt5 import QtCore 
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog , QApplication , QTableWidget , QHeaderView , QTableWidgetItem , QVBoxLayout
import math
import ipaddress

"""
Author : Yahia Mostafa

"""

class VLSM (QDialog):
    def __init__(self):
        super().__init__()
        
        # load the UI 
        loadUi('VLSM_interface.ui' , self)

        # Set title to the window
        self.setWindowTitle("VLSM Calculator")


        # init the UI Elements
        self.initGUI()


    def initGUI(self):

        # Set on ClickListener to the calculate Button
        self.calculateBtn.clicked.connect(self.calculate_vlsm)

        # Align text to the center
        self.networkAddressTxt.setAlignment(QtCore.Qt.AlignCenter)
        self.hostsTxt.setAlignment(QtCore.Qt.AlignCenter)


    def calculate_vlsm(self):
        # get network address and prefix
        networkAddress , prefix = self.networkAddressTxt.text().split("/")

        # network address as an ip Object
        networkIP = ipaddress.IPv4Address(networkAddress)

        # get the four octets in the network address
        ip = list(map(int ,networkAddress.split(".")))

        # get hosts 
        hosts = list(map(int ,self.hostsTxt.text().split(",")))

        # get the number of subnets required
        number_of_subents = len(hosts)

        # sort the number of hosts from the highest to the lowest 
        hosts.sort(reverse = True)

        # make a table to save values (the 4 well known ips)
        table = []

        for host in hosts:
            
            # get the number of bits required for this subnet
            number_of_bits = math.ceil(math.log2(host + 2))
            
            # get the first Usable IP Address
            first_usable_ip_add = networkIP + 1

            # get the broadcast ip Address
            broadcast_ip_add = networkIP + 2 ** number_of_bits  - 1

            # get the last Usable IP Address
            last_usable_ip_add = broadcast_ip_add - 1

            # wasted IP addresses
            wasted_addresses = 2 ** number_of_bits - host

            # create a list contains the 4 famous IPs
            IPs = [host , networkIP , first_usable_ip_add , last_usable_ip_add , broadcast_ip_add , 32 - number_of_bits , wasted_addresses]

            # add the IPs to the table
            table.append(IPs)

            # update the network IP
            networkIP += 2 ** number_of_bits

        self.create_table(table)


        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)



    def create_table(self , table):

        # get the number of col and the number of rows
        rows = len(table)
        cols = len(table[0])

        # create the table object
        self.tableWidget = QTableWidget()

        #set the number of rows
        self.tableWidget.setRowCount(rows) 
  
        #set the number ofColumns
        self.tableWidget.setColumnCount(cols)  

        # Identify the table Headers
        headers = ["Number of hosts" , "Network Address" , "First Usable IP" , "Last Usable IP" , "BroadCast Address" , "Slash" , "Wasted IPs" ]
  


        # iterate over the table 
        for row in range(rows):
            #iterate over each value in the row table
            for col in range(cols):
                self.tableWidget.setItem(row , col , QTableWidgetItem(str(table[row][col])))
        # self.tableWidget.setItem(0,0, QTableWidgetItem("Name"))
        # self.tableWidget.setItem(0,1, QTableWidgetItem("City"))
        # self.tableWidget.setItem(1,0, QTableWidgetItem("Aloysius"))
        # self.tableWidget.setItem(1,1, QTableWidgetItem("Indore"))
        # self.tableWidget.setItem(2,0, QTableWidgetItem("Alan"))
        # self.tableWidget.setItem(2,1, QTableWidgetItem("Bhopal"))
        # self.tableWidget.setItem(3,0, QTableWidgetItem("Arnavi"))
        # self.tableWidget.setItem(3,1, QTableWidgetItem("Mandsaur"))
   
        #Table will fit the screen horizontally
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        
        # set Headers
        self.tableWidget.setHorizontalHeaderLabels(headers)
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)








    

app = QApplication(sys.argv)
screen = VLSM()
screen.show()
sys.exit(app.exec_())
