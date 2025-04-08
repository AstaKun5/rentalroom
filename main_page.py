from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                            QPushButton, QFrame, QStackedWidget, QSizePolicy)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
import apartment_management
import tenant_management

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
        self.sidebar.setFixedWidth(300)
        sidebar_layout = QVBoxLayout(self.sidebar)
        sidebar_layout.setContentsMargins(0, 0, 0, 0)
        sidebar_layout.setSpacing(0)
        
        # Sidebar header
        sidebar_header = QLabel("إدارة العمارات")
        sidebar_header.setObjectName("sidebarHeader")
        sidebar_header.setAlignment(Qt.AlignCenter)
        sidebar_header.setFixedHeight(100)
        
        # Stacked widget
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.setObjectName("contentArea")
        
        main_layout.addWidget(self.sidebar)
        main_layout.addWidget(self.stacked_widget)
        
        # Create pages
        self.create_home_page()
        self.apartment_page = apartment_management.ApartmentManagementPage()
        self.tenant_page = tenant_management.TenantManagementPage()
        self.stacked_widget.addWidget(self.apartment_page)
        self.stacked_widget.addWidget(self.tenant_page)
        
        # Create sidebar items
        self.create_sidebar_items(sidebar_header, sidebar_layout)
        
        # Apply styles
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f5f5f7;
                font-family: 'Arial';
            }
            
            #sidebar {
                background-color: #2c3e50;
            }
            
            #sidebarHeader {
                background-color: #2c3e50;
                color: white;
                font-size: 24px;
                font-weight: bold;
                border-bottom: 2px solid #34495e;
            }
            
            #contentArea {
                background-color: #ffffff;
            }
            
            QPushButton#sidebarButton {
                background-color: transparent;
                color: #ecf0f1;
                font-size: 18px;
                padding: 25px 10px;
                border: none;
                border-radius: 0;
                min-height: 60px;
                text-align: center;
            }
            
            QPushButton#sidebarButton:hover {
                background-color: #34495e;
                color: white;
            }
            
            QPushButton#sidebarButton:pressed {
                background-color: #1a252f;
            }
            
            /* Card styles */
            .card {
                background-color: white;
                border: 1px solid #e0e0e0;
                border-radius: 8px;
                padding: 25px;
            }
            
            .card-title {
                font-size: 16px;
                color: #2c3e50;
                text-align: center;
            }
            
            .card-value {
                font-size: 28px;
                font-weight: bold;
                color: #3498db;
                text-align: center;
            }
            
            .page-title {
                font-size: 28px;
                font-weight: bold;
                color: #2c3e50;
                padding: 25px;
                text-align: center;
            }
        """)
    
    def create_home_page(self):
        home_page = QWidget()
        home_page.setObjectName("homePage")
        layout = QVBoxLayout(home_page)
        layout.setContentsMargins(30, 30, 30, 30)
        
        title = QLabel("نظام إدارة العقارات والأملاك")
        title.setObjectName("page-title")
        
        cards_container = QWidget()
        cards_layout = QHBoxLayout(cards_container)
        cards_layout.setSpacing(20)
        
        card1 = self.create_card("إجمالي العقارات", "125")
        card2 = self.create_card("العقارات المؤجرة", "87")
        card3 = self.create_card("إجمالي المستأجرين", "94")
        
        cards_layout.addWidget(card1)
        cards_layout.addWidget(card2)
        cards_layout.addWidget(card3)
        
        layout.addWidget(title)
        layout.addWidget(cards_container)
        layout.addStretch()
        
        self.stacked_widget.addWidget(home_page)
    
    def create_card(self, title, value):
        card = QFrame()
        card.setObjectName("card")
        card.setProperty("class", "card")
        card.setMinimumHeight(150)
        card.setMinimumWidth(250)
        
        layout = QVBoxLayout(card)
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(15)
        
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
        home_btn = QPushButton("الرئيسية")
        home_btn.setObjectName("sidebarButton")
        home_btn.setIcon(QIcon.fromTheme("home"))
        home_btn.setIconSize(QSize(32, 32))
        home_btn.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        layout.addWidget(home_btn)
        
        # Apartment button
        apartment_btn = QPushButton("إدارة الشقق")
        apartment_btn.setObjectName("sidebarButton")
        apartment_btn.setIcon(QIcon.fromTheme("building"))
        apartment_btn.setIconSize(QSize(32, 32))
        apartment_btn.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))
        layout.addWidget(apartment_btn)
        
        # Tenant button
        tenant_btn = QPushButton("إدارة المستأجرين")
        tenant_btn.setObjectName("sidebarButton")
        tenant_btn.setIcon(QIcon.fromTheme("user"))
        tenant_btn.setIconSize(QSize(32, 32))
        tenant_btn.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))
        layout.addWidget(tenant_btn)
        
        layout.addStretch()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())