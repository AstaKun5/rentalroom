from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                            QPushButton, QFrame, QStackedWidget, QSizePolicy)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont
import apartment_management  # Import apartment management module

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("نظام إدارة العقارات والأملاك")
        self.setGeometry(100, 100, 1400, 800)
        
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Sidebar
        self.sidebar = QFrame()
        self.sidebar.setObjectName("sidebar")
        self.sidebar.setFixedWidth(280)
        sidebar_layout = QVBoxLayout(self.sidebar)
        sidebar_layout.setContentsMargins(0, 0, 0, 0)
        sidebar_layout.setSpacing(0)
        
        # Sidebar header
        sidebar_header = QLabel("إدارة العقارات")
        sidebar_header.setObjectName("sidebarHeader")
        sidebar_header.setAlignment(Qt.AlignCenter)
        sidebar_header.setFixedHeight(80)
        
        # Stacked widget for content
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.setObjectName("contentArea")
        
        # Add widgets to main layout
        main_layout.addWidget(self.stacked_widget)
        main_layout.addWidget(self.sidebar)
        
        # Create pages
        self.create_home_page()
        self.apartment_page = apartment_management.ApartmentManagementPage()
        self.stacked_widget.addWidget(self.apartment_page)
        
        # Create sidebar items
        self.create_sidebar_items(sidebar_header, sidebar_layout)
        
        # Apply styles
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f5f5f7;
            }
            
            #sidebar {
                background-color: #2c3e50;
            }
            
            #sidebarHeader {
                background-color: #2c3e50;
                color: white;
                font-size: 18px;
                font-weight: bold;
                border-bottom: 1px solid #34495e;
            }
            
            #contentArea {
                background-color: #ffffff;
            }
            
            QPushButton#sidebarButton {
                background-color: transparent;
                color: #ecf0f1;
                font-size: 14px;
                text-align: right;
                padding: 15px 20px;
                border: none;
                border-radius: 0;
            }
            
            QPushButton#sidebarButton:hover {
                background-color: #34495e;
                color: white;
            }
            
            QPushButton#sidebarButton:pressed {
                background-color: #1a252f;
            }
            
            QLabel#sectionLabel {
                color: #bdc3c7;
                font-size: 12px;
                font-weight: bold;
                padding: 20px 20px 10px 20px;
                border-bottom: 1px solid #34495e;
            }
            
            /* Card styles */
            .card {
                background-color: white;
                border: 1px solid #e0e0e0;
                border-radius: 5px;
                padding: 20px;
            }
            
            .card:hover {
                background-color: #f8f9fa;
                border-color: #3498db;
            }
            
            .card-title {
                font-size: 14px;
                color: #2c3e50;
            }
            
            .card-value {
                font-size: 24px;
                font-weight: bold;
                color: #3498db;
            }
            
            .page-title {
                font-size: 24px;
                font-weight: bold;
                color: #2c3e50;
                padding: 20px;
            }
        """)
    
    def create_home_page(self):
        home_page = QWidget()
        home_page.setObjectName("homePage")
        layout = QVBoxLayout(home_page)
        layout.setContentsMargins(20, 20, 20, 20)
        
        # Title
        title = QLabel("نظام إدارة العقارات والأملاك")
        title.setObjectName("page-title")
        
        # Cards container
        cards_container = QWidget()
        cards_layout = QHBoxLayout(cards_container)
        cards_layout.setSpacing(15)
        
        # Card 1
        card1 = self.create_card("إجمالي العقارات", "125")
        # Card 2
        card2 = self.create_card("العقارات المؤجرة", "87")
        # Card 3
        card3 = self.create_card("إجمالي المستأجرين", "94")
        
        # Add cards to layout
        cards_layout.addWidget(card1)
        cards_layout.addWidget(card2)
        cards_layout.addWidget(card3)
        
        # Add widgets to main layout
        layout.addWidget(title)
        layout.addWidget(cards_container)
        layout.addStretch()
        
        self.stacked_widget.addWidget(home_page)
    
    def create_card(self, title, value):
        card = QFrame()
        card.setObjectName("card")
        card.setProperty("class", "card")
        card.setMinimumHeight(120)
        
        layout = QVBoxLayout(card)
        layout.setAlignment(Qt.AlignCenter)
        
        title_label = QLabel(title)
        title_label.setObjectName("card-title")
        
        value_label = QLabel(value)
        value_label.setObjectName("card-value")
        
        layout.addWidget(title_label)
        layout.addWidget(value_label)
        
        return card
    
    def create_sidebar_items(self, header, layout):
        layout.addWidget(header)
        
        
        # Home button
        home_btn = QPushButton("🏠 الرئيسية")
        home_btn.setObjectName("sidebarButton")
        home_btn.setIconSize(QSize(24, 24))
        home_btn.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        layout.addWidget(home_btn)
        
        # Apartment management button
        apartment_btn = QPushButton("🏢 إدارة الشقق")
        apartment_btn.setObjectName("sidebarButton")
        apartment_btn.setIconSize(QSize(24, 24))
        apartment_btn.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))
        layout.addWidget(apartment_btn)
        
        # Add stretch to push items to top
        layout.addStretch()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())