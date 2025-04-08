from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, 
                            QTableWidget, QTableWidgetItem, QHeaderView, QMessageBox,
                            QDialog, QLineEdit, QComboBox, QFormLayout, QScrollArea,
                            QFrame, QSizePolicy)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont

class ApartmentManagementPage(QWidget):
    def __init__(self):
        super().__init__()
        self.apartments = []  # Store apartment data
        self.setup_ui()
        
    def setup_ui(self):
        # Main layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)
        
        # Title
        title_label = QLabel("إدارة الشقق")
        title_label.setObjectName("pageTitle")
        title_label.setAlignment(Qt.AlignCenter)
        
        # Button container
        btn_container = QWidget()
        btn_layout = QHBoxLayout(btn_container)
        btn_layout.setContentsMargins(0, 0, 0, 0)
        btn_layout.setSpacing(10)
        
        # Add apartment button
        self.add_btn = QPushButton("إضافة شقة")
        self.add_btn.setObjectName("actionButton")
        self.add_btn.clicked.connect(self.show_add_form)
        
        # Edit apartment button
        self.edit_btn = QPushButton("تعديل شقة")
        self.edit_btn.setObjectName("actionButton")
        self.edit_btn.clicked.connect(self.show_edit_form)
        
        # Delete apartment button
        self.delete_btn = QPushButton("حذف شقة")
        self.delete_btn.setObjectName("actionButton")
        self.delete_btn.clicked.connect(self.delete_apartment)
        
        # Add buttons to layout
        btn_layout.addWidget(self.add_btn)
        btn_layout.addWidget(self.edit_btn)
        btn_layout.addWidget(self.delete_btn)
        
        # Table to display apartments
        self.table = QTableWidget()
        self.table.setObjectName("apartmentTable")
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["رقم الشقة", "الطابق", "عدد الغرف", "السعر", "الحالة"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setSelectionMode(QTableWidget.SingleSelection)
        
        # Load sample data
        self.load_sample_data()
        
        # Add widgets to main layout
        main_layout.addWidget(title_label)
        main_layout.addWidget(btn_container)
        main_layout.addWidget(self.table)
        
        # Apply styles
        self.setStyleSheet("""
            #pageTitle {
                font-size: 24px;
                font-weight: bold;
                color: #2c3e50;
                padding: 10px;
            }
            
            #actionButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 10px 15px;
                font-size: 14px;
                font-weight: bold;
                border-radius: 4px;
            }
            
            #actionButton:hover {
                background-color: #2980b9;
            }
            
            #actionButton:pressed {
                background-color: #1a6a9f;
            }
            
            #apartmentTable {
                background-color: white;
                border: 1px solid #e0e0e0;
                border-radius: 5px;
                gridline-color: #e0e0e0;
            }
            
            #apartmentTable QHeaderView::section {
                background-color: #2c3e50;
                color: white;
                padding: 8px;
                font-weight: bold;
                border: none;
            }
            
            #apartmentTable::item {
                padding: 8px;
                border-bottom: 1px solid #e0e0e0;
            }
            
            #apartmentTable::item:selected {
                background-color: #3498db;
                color: white;
            }
        """)
    
    def load_sample_data(self):
        # Sample data for display
        sample_apartments = [
            {"number": "101", "floor": "1", "rooms": "3", "price": "1500", "status": "متاحة"},
            {"number": "202", "floor": "2", "rooms": "2", "price": "1200", "status": "مؤجرة"},
            {"number": "303", "floor": "3", "rooms": "4", "price": "2000", "status": "متاحة"},
        ]
        for apt in sample_apartments:
            self.add_apartment_to_table(apt)
            self.apartments.append(apt)
    
    def show_add_form(self):
        self.form_dialog("إضافة شقة جديدة", self.save_apartment)
    
    def show_edit_form(self):
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "تحذير", "الرجاء اختيار شقة لتعديلها")
            return
            
        apartment_number = self.table.item(selected_row, 0).text()
        apartment = next((apt for apt in self.apartments if apt['number'] == apartment_number), None)
        
        if apartment:
            self.form_dialog("تعديل بيانات الشقة", self.update_apartment, apartment)
    
    def form_dialog(self, title, save_callback, apartment=None):
        dialog = QDialog(self)
        dialog.setWindowTitle(title)
        dialog.setFixedSize(500, 400)
        
        # Main layout
        layout = QVBoxLayout(dialog)
        
        # Scroll area for form
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.NoFrame)
        
        # Form container
        form_container = QWidget()
        form_layout = QFormLayout(form_container)
        form_layout.setContentsMargins(20, 20, 20, 20)
        form_layout.setSpacing(15)
        form_layout.setLabelAlignment(Qt.AlignRight)
        
        # Form fields
        fields = [
            ("رقم الشقة:", "number", QLineEdit()),
            ("الطابق:", "floor", QLineEdit()),
            ("عدد الغرف:", "rooms", QLineEdit()),
            ("السعر:", "price", QLineEdit()),
            ("الحالة:", "status", QComboBox())
        ]
        
        # Configure status combobox
        status_combo = fields[4][2]
        status_combo.addItems(["متاحة", "مؤجرة", "تحت الصيانة"])
        
        self.entries = {}
        
        for label, field_name, widget in fields:
            # Set current values if editing
            if apartment and field_name in apartment:
                if isinstance(widget, QLineEdit):
                    widget.setText(apartment[field_name])
                elif isinstance(widget, QComboBox):
                    widget.setCurrentText(apartment[field_name])
            
            # Add to form layout
            form_layout.addRow(label, widget)
            self.entries[field_name] = widget
        
        # Button container
        btn_container = QWidget()
        btn_layout = QHBoxLayout(btn_container)
        btn_layout.setContentsMargins(0, 0, 0, 0)
        btn_layout.setSpacing(10)
        
        # Save button
        save_text = "حفظ" if apartment else "إضافة"
        save_btn = QPushButton(save_text)
        save_btn.setObjectName("formButton")
        save_btn.clicked.connect(lambda: self.handle_save(save_callback, dialog, apartment))
        
        # Cancel button
        cancel_btn = QPushButton("إلغاء")
        cancel_btn.setObjectName("formButton")
        cancel_btn.clicked.connect(dialog.reject)
        
        # Add buttons to layout
        btn_layout.addWidget(save_btn)
        btn_layout.addWidget(cancel_btn)
        
        # Set scroll widget
        scroll.setWidget(form_container)
        
        # Add widgets to dialog layout
        layout.addWidget(scroll)
        layout.addWidget(btn_container)
        
        # Apply styles
        dialog.setStyleSheet("""
            QDialog {
                background-color: #f5f5f7;
            }
            
            QLabel {
                font-size: 14px;
                color: #333;
            }
            
            QLineEdit, QComboBox {
                font-size: 14px;
                padding: 8px;
                border: 1px solid #ddd;
                border-radius: 4px;
                background-color: white;
                min-width: 200px;
            }
            
            QLineEdit:focus, QComboBox:focus {
                border: 1px solid #3498db;
            }
            
            #formButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 10px 15px;
                font-size: 14px;
                font-weight: bold;
                border-radius: 4px;
            }
            
            #formButton:hover {
                background-color: #2980b9;
            }
            
            #formButton:pressed {
                background-color: #1a6a9f;
            }
        """)
        
        dialog.exec_()
    
    def handle_save(self, save_callback, dialog, apartment=None):
        data = {}
        for field_name, widget in self.entries.items():
            if isinstance(widget, QLineEdit):
                value = widget.text()
            elif isinstance(widget, QComboBox):
                value = widget.currentText()
            
            if not value:
                QMessageBox.critical(self, "خطأ", "الرجاء ملء جميع الحقول")
                return
                
            data[field_name] = value
        
        save_callback(data, apartment)
        dialog.accept()
    
    def save_apartment(self, data, _):
        apartment = data
        self.apartments.append(apartment)
        self.add_apartment_to_table(apartment)
        QMessageBox.information(self, "نجاح", "تمت إضافة الشقة بنجاح")
    
    def update_apartment(self, data, old_apartment):
        if not old_apartment:
            return
            
        # Update apartment data
        for key, value in data.items():
            old_apartment[key] = value
        
        # Update table display
        selected_row = self.table.currentRow()
        if selected_row != -1:
            self.table.setItem(selected_row, 0, QTableWidgetItem(old_apartment['number']))
            self.table.setItem(selected_row, 1, QTableWidgetItem(old_apartment['floor']))
            self.table.setItem(selected_row, 2, QTableWidgetItem(old_apartment['rooms']))
            self.table.setItem(selected_row, 3, QTableWidgetItem(old_apartment['price']))
            self.table.setItem(selected_row, 4, QTableWidgetItem(old_apartment['status']))
        
        QMessageBox.information(self, "نجاح", "تم تعديل بيانات الشقة بنجاح")
    
    def delete_apartment(self):
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "تحذير", "الرجاء اختيار شقة لحذفها")
            return
            
        apartment_number = self.table.item(selected_row, 0).text()
        
        reply = QMessageBox.question(
            self, "تأكيد", "هل أنت متأكد من حذف هذه الشقة؟",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            # Remove from list
            self.apartments = [apt for apt in self.apartments if apt['number'] != apartment_number]
            
            # Remove from table
            self.table.removeRow(selected_row)
            
            QMessageBox.information(self, "نجاح", "تم حذف الشقة بنجاح")
    
    def add_apartment_to_table(self, apartment):
        row = self.table.rowCount()
        self.table.insertRow(row)
        
        self.table.setItem(row, 0, QTableWidgetItem(apartment['number']))
        self.table.setItem(row, 1, QTableWidgetItem(apartment['floor']))
        self.table.setItem(row, 2, QTableWidgetItem(apartment['rooms']))
        self.table.setItem(row, 3, QTableWidgetItem(apartment['price']))
        self.table.setItem(row, 4, QTableWidgetItem(apartment['status']))

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys
    
    app = QApplication(sys.argv)
    window = ApartmentManagementPage()
    window.show()
    sys.exit(app.exec_())