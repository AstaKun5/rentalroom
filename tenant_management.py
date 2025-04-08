from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, 
                            QTableWidget, QTableWidgetItem, QHeaderView, QMessageBox,
                            QDialog, QLineEdit, QFormLayout, QScrollArea, QFrame)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class TenantManagementPage(QWidget):
    def __init__(self):
        super().__init__()
        self.tenants = []  # تخزين بيانات المستأجرين
        self.setup_ui()
        self.contracts = []
        
    def setup_ui(self):
        # التخطيط الرئيسي
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)
        
        # العنوان
        title_label = QLabel("إدارة المستأجرين")
        title_label.setObjectName("pageTitle")
        title_label.setAlignment(Qt.AlignCenter)
        
        # حاوية الأزرار
        btn_container = QWidget()
        btn_layout = QHBoxLayout(btn_container)
        btn_layout.setContentsMargins(0, 0, 0, 0)
        btn_layout.setSpacing(10)
        
        # زر إضافة مستأجر
        self.add_btn = QPushButton("إضافة مستأجر")
        self.add_btn.setObjectName("actionButton")
        self.add_btn.clicked.connect(self.show_add_form)
        
        # زر تعديل مستأجر
        self.edit_btn = QPushButton("تعديل مستأجر")
        self.edit_btn.setObjectName("actionButton")
        self.edit_btn.clicked.connect(self.show_edit_form)
        
        # زر حذف مستأجر
        self.delete_btn = QPushButton("حذف مستأجر")
        self.delete_btn.setObjectName("actionButton")
        self.delete_btn.clicked.connect(self.delete_tenant)
        
        # إضافة الأزرار إلى التخطيط
        btn_layout.addWidget(self.add_btn)
        btn_layout.addWidget(self.edit_btn)
        btn_layout.addWidget(self.delete_btn)
        
        # جدول لعرض المستأجرين
        self.table = QTableWidget()
        self.table.setObjectName("tenantTable")
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["الاسم", "رقم الجوال", "رقم الهوية", "رقم الشقة"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setSelectionMode(QTableWidget.SingleSelection)
        
        # تحميل بيانات تجريبية
        self.load_sample_data()
        
        # إضافة العناصر إلى التخطيط الرئيسي
        main_layout.addWidget(title_label)
        main_layout.addWidget(btn_container)
        main_layout.addWidget(self.table)
        
        # تطبيق الأنماط
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
            
            #tenantTable {
                background-color: white;
                border: 1px solid #e0e0e0;
                border-radius: 5px;
                gridline-color: #e0e0e0;
            }
            
            #tenantTable QHeaderView::section {
                background-color: #2c3e50;
                color: white;
                padding: 8px;
                font-weight: bold;
                border: none;
            }
            
            #tenantTable::item {
                padding: 8px;
                border-bottom: 1px solid #e0e0e0;
            }
            
            #tenantTable::item:selected {
                background-color: #3498db;
                color: white;
            }
        """)
    
    def load_sample_data(self):
        # بيانات تجريبية للعرض
        sample_tenants = [
            {"name": "أحمد محمد", "phone": "0501234567", "id": "1234567890", "apartment": "101"},
            
        ]
        for tenant in sample_tenants:
            self.add_tenant_to_table(tenant)
            self.tenants.append(tenant)
    
    def show_add_form(self):
        self.form_dialog("إضافة مستأجر جديد", self.save_tenant)
    
    def show_edit_form(self):
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "تحذير", "الرجاء اختيار مستأجر لتعديل بياناته")
            return
            
        tenant_name = self.table.item(selected_row, 0).text()
        tenant = next((t for t in self.tenants if t['name'] == tenant_name), None)
        
        if tenant:
            self.form_dialog("تعديل بيانات المستأجر", self.update_tenant, tenant)
    
    def form_dialog(self, title, save_callback, tenant=None):
        dialog = QDialog(self)
        dialog.setWindowTitle(title)
        dialog.setFixedSize(500, 400)
        
        # التخطيط الرئيسي
        layout = QVBoxLayout(dialog)
        
        # منطقة التمرير للنموذج
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.NoFrame)
        
        # حاوية النموذج
        form_container = QWidget()
        form_layout = QFormLayout(form_container)
        form_layout.setContentsMargins(20, 20, 20, 20)
        form_layout.setSpacing(15)
        form_layout.setLabelAlignment(Qt.AlignRight)
        
        # حقول النموذج
        fields = [
            ("الاسم:", "name", QLineEdit()),
            ("رقم الجوال:", "phone", QLineEdit()),
            ("رقم الهوية:", "id", QLineEdit()),
            ("رقم الشقة:", "apartment", QLineEdit()),
        ]
        
        self.entries = {}
        
        for label, field_name, widget in fields:
            # تعيين القيم الحالية إذا كان التعديل
            if tenant and field_name in tenant:
                widget.setText(tenant[field_name])
            
            # إضافة إلى تخطيط النموذج
            form_layout.addRow(label, widget)
            self.entries[field_name] = widget
        
        # حاوية الأزرار
        btn_container = QWidget()
        btn_layout = QHBoxLayout(btn_container)
        btn_layout.setContentsMargins(0, 0, 0, 0)
        btn_layout.setSpacing(10)
        
        # زر الحفظ
        save_text = "حفظ" if tenant else "إضافة"
        save_btn = QPushButton(save_text)
        save_btn.setObjectName("formButton")
        save_btn.clicked.connect(lambda: self.handle_save(save_callback, dialog, tenant))
        
        # زر الإلغاء
        cancel_btn = QPushButton("إلغاء")
        cancel_btn.setObjectName("formButton")
        cancel_btn.clicked.connect(dialog.reject)
        
        # إضافة الأزرار إلى التخطيط
        btn_layout.addWidget(save_btn)
        btn_layout.addWidget(cancel_btn)
        
        # تعيين عنصر التمرير
        scroll.setWidget(form_container)
        
        # إضافة العناصر إلى تخطيط الحوار
        layout.addWidget(scroll)
        layout.addWidget(btn_container)
        
        # تطبيق الأنماط
        dialog.setStyleSheet("""
            QDialog {
                background-color: #f5f5f7;
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
                min-width: 200px;
            }
            
            QLineEdit:focus {
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
    
    def handle_save(self, save_callback, dialog, tenant=None):
        data = {}
        for field_name, widget in self.entries.items():
            value = widget.text()
            
            if not value:
                QMessageBox.critical(self, "خطأ", "الرجاء ملء جميع الحقول")
                return
                
            data[field_name] = value
        
        save_callback(data, tenant)
        dialog.accept()
    
    def save_tenant(self, data, _):
        tenant = data
        self.tenants.append(tenant)
        self.add_tenant_to_table(tenant)
        QMessageBox.information(self, "نجاح", "تمت إضافة المستأجر بنجاح")
    
    def update_tenant(self, data, old_tenant):
        if not old_tenant:
            return
            
        # تحديث بيانات المستأجر
        for key, value in data.items():
            old_tenant[key] = value
        
        # تحديث عرض الجدول
        selected_row = self.table.currentRow()
        if selected_row != -1:
            self.table.setItem(selected_row, 0, QTableWidgetItem(old_tenant['name']))
            self.table.setItem(selected_row, 1, QTableWidgetItem(old_tenant['phone']))
            self.table.setItem(selected_row, 2, QTableWidgetItem(old_tenant['id']))
            self.table.setItem(selected_row, 3, QTableWidgetItem(old_tenant['apartment']))
        
        QMessageBox.information(self, "نجاح", "تم تعديل بيانات المستأجر بنجاح")
    
    def delete_tenant(self):
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "تحذير", "الرجاء اختيار مستأجر لحذفه")
            return
            
        tenant_name = self.table.item(selected_row, 0).text()
        
        reply = QMessageBox.question(
            self, "تأكيد", "هل أنت متأكد من حذف هذا المستأجر؟",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            # إزالة من القائمة
            self.tenants = [t for t in self.tenants if t['name'] != tenant_name]
            
            # إزالة من الجدول
            self.table.removeRow(selected_row)
            
            QMessageBox.information(self, "نجاح", "تم حذف المستأجر بنجاح")
    
    def add_tenant_to_table(self, tenant):
        row = self.table.rowCount()
        self.table.insertRow(row)
        
        self.table.setItem(row, 0, QTableWidgetItem(tenant['name']))
        self.table.setItem(row, 1, QTableWidgetItem(tenant['phone']))
        self.table.setItem(row, 2, QTableWidgetItem(tenant['id']))
        self.table.setItem(row, 3, QTableWidgetItem(tenant['apartment']))

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys
    
    app = QApplication(sys.argv)
    window = TenantManagementPage()
    window.show()
    sys.exit(app.exec_())