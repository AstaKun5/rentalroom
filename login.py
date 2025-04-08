from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, 
                            QLineEdit, QPushButton, QMessageBox, QFrame)
from PyQt5.QtCore import Qt
import sys
import main_page  # استيراد صفحة الرئيسية

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("تسجيل الدخول")
        self.setFixedSize(400, 300)
        
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout
        layout = QVBoxLayout(central_widget)
        layout.setAlignment(Qt.AlignCenter)
        
        # Login frame
        login_frame = QFrame()
        login_frame.setObjectName("loginFrame")
        login_frame.setFixedWidth(300)
        frame_layout = QVBoxLayout(login_frame)
        frame_layout.setSpacing(15)
        
        # Username field
        self.username_label = QLabel("اسم المستخدم:")
        self.username_label.setAlignment(Qt.AlignCenter)  # Center alignment
        
        self.username_entry = QLineEdit()
        self.username_entry.setPlaceholderText("أدخل اسم المستخدم")
        self.username_entry.setAlignment(Qt.AlignLeft)  # Left alignment for LTR input
        self.username_entry.setStyleSheet("text-align: left;")  # Left alignment for LTR input
        self.username_entry.setLayoutDirection(Qt.LeftToRight)  # LTR input
        
        # Password field
        self.password_label = QLabel("كلمة المرور:")
        self.password_label.setAlignment(Qt.AlignCenter)  # Center alignment
        
        self.password_entry = QLineEdit()
        self.password_entry.setPlaceholderText("أدخل كلمة المرور")
        self.password_entry.setEchoMode(QLineEdit.Password)
        self.password_entry.setAlignment(Qt.AlignLeft)  # Left alignment for LTR input
        self.password_entry.setStyleSheet("text-align: left;")  # Left alignment for LTR input
        self.password_entry.setLayoutDirection(Qt.LeftToRight)  # LTR input
        
        # Login button
        self.login_button = QPushButton("تسجيل الدخول")
        self.login_button.clicked.connect(self.login)
        
        # Add widgets to frame
        frame_layout.addWidget(self.username_label)
        frame_layout.addWidget(self.username_entry)
        frame_layout.addWidget(self.password_label)
        frame_layout.addWidget(self.password_entry)
        frame_layout.addWidget(self.login_button)
        
        # Add frame to main layout
        layout.addWidget(login_frame)
        
        # Apply styles
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f5f5f5;
                font-family: Arial;
            }
            
            QFrame#loginFrame {
                background-color: white;
                border-radius: 10px;
                padding: 20px;
            }
            
            QLabel {
                font-size: 14px;
                color: #333;
            }
            
            QLineEdit {
                font-size: 14px;
                padding: 8px;
                border: 1px solid #ddd;
                border-radius: 4px;
                background-color: white;
            }
            
            QLineEdit:focus {
                border: 1px solid #3498db;
            }
            
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 10px;
                font-size: 14px;
                font-weight: bold;
                border-radius: 4px;
            }
            
            QPushButton:hover {
                background-color: #2980b9;
            }
            
            QPushButton:pressed {
                background-color: #1a6a9f;
            }
        """)
    
    def login(self):
        username = self.username_entry.text()
        password = self.password_entry.text()
        
        if username == "admin" and password == "admin":  # للاختبار فقط
            self.close()
            self.main_window = main_page.MainWindow()
            self.main_window.show()
        else:
            QMessageBox.critical(self, "خطأ", "اسم المستخدم أو كلمة المرور غير صحيحة")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # تعيين اتجاه التطبيق ككل من اليمين لليسار
    app.setLayoutDirection(Qt.RightToLeft)
    
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())