import sqlite3
import datetime


def process_order(customer_id, item_number, quantity_ordered):
    try:
        conn = sqlite3.connect('inventoryV2.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM BillOfMaterials WHERE ItemNo=?", (item_number,))
        data = cursor.fetchone()

        if data:
            if data[3] is None:
                key = data[1]
                value = data[2] * quantity_ordered
                cursor.execute("SELECT * FROM ManufacturedComponents WHERE ComponentDescription=?", (key,))
                exist_quantity = cursor.fetchone()[2]
                updated_quantity = exist_quantity - value
                cursor.execute("UPDATE ManufacturedComponents SET Quantity = ? WHERE ComponentDescription = ?", (updated_quantity, key))
                conn.commit()
            else:
                sub_assembly_table_name = data[3]
                value = data[2] * data[4] * quantity_ordered
                sub_assembly_data = cursor.execute(f"SELECT * FROM {sub_assembly_table_name}").fetchall()
                for row in sub_assembly_data:
                    key = row[1]
                    inner_value = row[2]
                    cursor.execute("SELECT * FROM ManufacturedComponents WHERE ComponentDescription=?", (key,))
                    exist_quantity = cursor.fetchone()[2]
                    updated_quantity = exist_quantity - (value * inner_value)
                    cursor.execute("UPDATE ManufacturedComponents SET Quantity = ? WHERE ComponentDescription = ?", (updated_quantity, key))
                    conn.commit()

            # Update the Manufactured Components table after processing the order
            cursor.execute("SELECT * FROM ManufacturedComponents")
            all_manufactured_components = cursor.fetchall()
            for component in all_manufactured_components:
                component_key = component[1]
                component_quantity = component[2]
                cursor.execute(f"SELECT SUM(QuantityOrdered * Quantity) FROM Orders WHERE ItemNo = ? GROUP BY ItemNo", (item_number,))
                total_ordered_quantity = cursor.fetchone()[0]
                updated_quantity = component_quantity - total_ordered_quantity
                cursor.execute("UPDATE ManufacturedComponents SET Quantity = ? WHERE ComponentDescription = ?", (updated_quantity, component_key))
                conn.commit()

            # Insert order details into the Orders table
            order_date = datetime.date.today()
            cursor.execute("INSERT INTO Orders (CustomerId, ItemNo, QuantityOrdered, OrderDate) VALUES (?, ?, ?, ?)", (customer_id, item_number, quantity_ordered, order_date))
            conn.commit()

            print("Order processed successfully.")
        else:
            print("Invalid item number.")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")

    conn.close()
