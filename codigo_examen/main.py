from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QHeaderView, QDialog,QMessageBox
from database import Database
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QAction, QKeySequence
import sys
import os

class UserApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestió d'Usuaris")
        self.setGeometry(100, 100, 600, 500)
        self.db = Database(db_name=os.path.join(os.path.dirname(__file__), 'users.db'))

        loader = QUiLoader()
        ui_path = os.path.join(os.path.dirname(__file__), "interfaz.ui")
        self.ui = loader.load(ui_path, None)

        barra_menus = self.menuBar()
        menu = barra_menus.addMenu("&Usuaris")
        accion = QAction("&Afegir", self)
        accion.triggered.connect(self.add_user)
        menu.addAction(accion)
        accion2 = QAction("&Modificar", self)
        accion2.triggered.connect(self.edit_user)
        menu.addAction(accion2)

        # Widget principal
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        self.layout = QVBoxLayout()
        main_widget.setLayout(self.layout)

        # Formulari (afegit directament a la finestra)
        # self.name_input = QLineEdit()
        # self.password_input = QLineEdit() 
        # self.role_input = QLineEdit() 

        # self.layout.addWidget(QLabel("Nom:"))
        # self.layout.addWidget(self.name_input)
        # self.layout.addWidget(QLabel("Contrasenya:"))  
        # self.layout.addWidget(self.password_input)
        # self.layout.addWidget(QLabel("Rol (Admin, Usuari, Convidat):")) 
        # self.layout.addWidget(self.role_input)

        # # Botons per afegir i modificar
        # self.add_button = QPushButton("Afegir Usuari")
        # self.add_button.clicked.connect(self.add_user)
        # self.layout.addWidget(self.add_button)

        # self.edit_button = QPushButton("Modificar Usuari")
        # self.edit_button.clicked.connect(self.edit_user)
        # self.layout.addWidget(self.edit_button)
        self.delete_button = QPushButton("Eliminar Usuari")
        self.delete_button.clicked.connect(self.delete_user)
        self.layout.addWidget(self.delete_button)


        # Taula d'usuaris
        self.table = self.create_table()
        self.layout.addWidget(self.table)

        self.load_users()

    def create_table(self):
        table = QTableWidget()
        table.setColumnCount(3)
        table.setHorizontalHeaderLabels(["Nom", "Contrasenya", "Rol"])  
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  
        table.setSelectionBehavior(QTableWidget.SelectRows)  
        return table

    def load_users(self):
        self.table.setRowCount(0)
        users = self.db.get_users()
        for row_index, (user_id, name, password, role) in enumerate(users):
            self.table.insertRow(row_index)
            self.table.setItem(row_index, 0, QTableWidgetItem(name))
            self.table.setItem(row_index, 1, QTableWidgetItem(password))  
            self.table.setItem(row_index, 2, QTableWidgetItem(role))

    def add_user(self):
        if self.ui.exec() == QDialog.Accepted:
            name = self.ui.lineEditNom.text()
            password = self.ui.lineEditContrasenya.text() 
            role = self.ui.ComboBoxRol.currentText() 

            if name and password and role:
                self.db.add_user(name, password, role)
                self.load_users()

    def edit_user(self):
        selected_row = self.table.currentRow()
        if selected_row == -1:
            return

        user_id = self.db.get_users()[selected_row][0]
        current_name=self.table.item(selected_row, 0).text()
        current_password=self.table.item(selected_row, 1).text()
        current_rol=self.table.item(selected_row, 2).text()

        self.ui.lineEditNom.setText(current_name)
        self.ui.lineEditContrasenya.setText(current_password)
        self.ui.ComboBoxRol.setCurrentText(current_rol)

        if self.ui.exec() == QDialog.Accepted:
            boton_pulsado = QMessageBox.warning(
            self,
            "Modificar",
            "Estas segur de que vols modificar?",
            buttons=QMessageBox.Yes | QMessageBox.No,
            defaultButton=QMessageBox.No
        )
        if boton_pulsado == QMessageBox.Yes:
            user_id = self.db.get_users()[selected_row][0]
            new_name = self.ui.lineEditNom.text()
            new_password = self.ui.lineEditContrasenya.text()
            new_role = self.ui.ComboBoxRol.currentText()  

            if new_name and new_password and new_role:
                self.db.update_user(user_id, new_name, new_password, new_role)
                self.load_users()


    def delete_user(self):
        selected_row = self.table.currentRow()
        if selected_row == -1:
            return
        
        boton_pulsado = QMessageBox.warning(
        self,
        "Eliminar",
        "Estas segur de que vols eliminar?",
        buttons=QMessageBox.Yes | QMessageBox.No,
        defaultButton=QMessageBox.No
    )

        if boton_pulsado == QMessageBox.Yes:
            user_id = self.db.get_users()[selected_row][0]
            self.db.delete_user(user_id)
            self.load_users()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UserApp()
    window.show()
    sys.exit(app.exec())