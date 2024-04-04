from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import os

class UpdateClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1300x800")
        self.root.title("INVENTORY MANAGEMENT SYSTEM")
        self.root.config(bg="white")

        title = Label(self.root, text="Update Inventory", font=("Helvetica", 18), bg="#010c48", fg="white")
        title.place(x=0, y=0, relwidth=1)

        self.create_product_section()
        self.create_components_section()
        self.create_subassemblies_section()
        self.create_buttons()
        upd_frame=Frame(self.root,bd=3,relief=RIDGE)
        upd_frame.place(x=0,y=350,relwidth=1,height=150)

        #self.ProductsTable=ttk.Treeview(upd_frame,columns=("prod_id","prod_name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)

        #scrolly=Scrollbar(upd_frame,orient=VERTICAL)
        #scrollx=Scrollbar(upd_frame,orient=HORIZONTAL)
        
       # scrolly.pack(side=RIGHT,fill=Y)
        
        #scrollx.config(command=self.ProductsTable.xview)
        #scrolly.config(command=self.ProductsTable.yview)

    def create_product_section(self):
        lbl_name = Label(self.root, text="Product Name:", font=("Helvetica", 12), bg="white")
        lbl_name.place(x=50, y=60)
        self.entry_name = Entry(self.root, font=("Helvetica", 12))
        self.entry_name.place(x=200, y=60, width=250)

        lbl_id = Label(self.root, text="Product ID:", font=("Helvetica", 12), bg="white")
        lbl_id.place(x=50, y=100)
        self.entry_id = Entry(self.root, font=("Helvetica", 12))
        self.entry_id.place(x=200, y=100, width=250)

    def create_components_section(self):
        lbl_components = Label(self.root, text="Components:", font=("Helvetica", 15), bg="white")
        lbl_components.place(x=0, y=160, relwidth=1)

        self.component_entries_left = []
        self.component_entries_right = []
        components = [
            ("Component 1:", 0),
            ("Component 2:", 0),
            ("Component 3:", 0),
            ("Component 4:", 0),
            ("Component 5:", 0),
            ("Component 6:", 0),
            ("Component 7:", 0),
            ("Component 8:", 0),
            ("Component 9:", 0),
            ("Component 10:", 0),
            ("Component 11:", 0),
            ("Component 12:", 0),
            ("Component 13:", 0),
            ("Component 14:", 0)
        ]

        for i, (component_name, component_quantity) in enumerate(components, start=1):
            if i <= 7:
                lbl_component = Label(self.root, text=component_name, font=("Helvetica", 12), bg="white")
                lbl_component.place(x=50, y=200 + i * 30)
                entry_component = Entry(self.root, font=("Helvetica", 12))
                entry_component.place(x=200, y=200 + i * 30, width=250)
                entry_component.insert(0, str(component_quantity))
                self.component_entries_left.append(entry_component)
            else:
                lbl_component = Label(self.root, text=component_name, font=("Helvetica", 12), bg="white")
                lbl_component.place(x=500, y=200 + (i-7) * 30)
                entry_component = Entry(self.root, font=("Helvetica", 12))
                entry_component.place(x=650, y=200 + (i-7) * 30, width=250)
                entry_component.insert(0, str(component_quantity))
                self.component_entries_right.append(entry_component)

    def create_subassemblies_section(self):
        lbl_subassemblies = Label(self.root, text="Subassemblies:", font=("Helvetica", 15), bg="white")
        lbl_subassemblies.place(x=0, y=440, relwidth=1)

        self.subassembly_entries_left = []
        self.subassembly_entries_right = []
        subassemblies = [
            ("Subassembly 1:", 0),
            ("Subassembly 2:", 0),
            ("Subassembly 3:", 0),
            ("Subassembly 4:", 0)
        ]

        for i, (subassembly_name, subassembly_quantity) in enumerate(subassemblies, start=1):
            if i<=2:
                lbl_subassembly = Label(self.root, text=subassembly_name, font=("Helvetica", 12), bg="white")
                lbl_subassembly.place(x=50, y=490 + i * 30)
                entry_subassembly = Entry(self.root, font=("Helvetica", 12))
                entry_subassembly.place(x=200, y=490 + i* 30, width=250)
                entry_subassembly.insert(0, str(subassembly_quantity))
                self.subassembly_entries_left.append(entry_subassembly)
            else:
                lbl_subassembly = Label(self.root, text=subassembly_name, font=("Helvetica", 12), bg="white")
                lbl_subassembly.place(x=500, y=490 + (i-2) * 30)
                entry_subassembly = Entry(self.root, font=("Helvetica", 12))
                entry_subassembly.place(x=650, y=490 + (i-2) * 30, width=250)
                entry_subassembly.insert(0, str(subassembly_quantity))
                self.subassembly_entries_right.append(entry_subassembly)

    def create_buttons(self):
        btn_save = Button(self.root, text="Save", font=("Helvetica", 14), bg="green", fg="white", command=self.save_data)
        btn_save.place(x=400, y=600, width=100)

        btn_delete = Button(self.root, text="Delete", font=("Helvetica", 14), bg="red", fg="white", command=self.delete_data)
        btn_delete.place(x=550, y=600, width=100)

    def save_data(self):
        product_name = self.entry_name.get()
        product_id = self.entry_id.get()
        components = []

        for entry in self.component_entries_left + self.component_entries_right:
            component_quantity = entry.get()
            components.append(component_quantity)

        subassemblies = []

        for entry in self.subassembly_entries_left + self.subassembly_entries_right:
            subassembly_quantity = entry.get()
            subassemblies.append(subassembly_quantity)

        print("Saved Data:")
        print("Product Name:", product_name)
        print("Product ID:", product_id)
        print("Components:", components)
        print("Subassemblies:", subassemblies)

    def delete_data(self):
        product_name = self.entry_name.get()
        product_id = self.entry_id.get()

        print("Deleted Data:")
        print("Product Name:", product_name)
        print("Product ID:", product_id)

if __name__ == "__main__":
    root = Tk()
    obj = UpdateClass(root)
    root.mainloop()
