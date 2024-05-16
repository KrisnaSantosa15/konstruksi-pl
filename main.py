# KRISNA SANTOSA
# 2209092
# RPL - 4B
"""
Sistem Manajemen Inventaris

ASSERTIONS, DEFENSIVE PROGRAMMING, DAN DESIGN BY CONTRACT

Program yang saya buat ini menyediakan kelas dan fungsi untuk mengelola sistem inventaris. Modul ini mencakup
fitur CRUD inventaris. Setiap item
memiliki ID, nama, dan qty.
"""


class InventoryItem:
    _id_counter = 1

    def __init__(self, name: str, quantity: int):
        """Inisialisasi item inventaris dengan nama dan jumlah.

        Argumen:
            name (str): Nama item.
            quantity (int): Jumlah item.

        Menghasilkan:
            AssertionError: Jika nama bukan string atau jumlah bukan integer non-negatif.
        """
        # Assertion
        assert isinstance(name, str), "Nama harus berupa string"
        assert isinstance(
            quantity, int) and quantity >= 0, "Jumlah harus berupa integer non-negatif"

        self.id = InventoryItem._id_counter
        InventoryItem._id_counter += 1
        self.name = name
        self.quantity = quantity


class Inventory:
    def __init__(self):
        """Inisialisasi inventaris kosong."""
        self.items = {}

    def add_item(self, item: InventoryItem):
        """Tambahkan item ke dalam inventaris.

        Argumen:
            item (InventoryItem): Item yang akan ditambahkan ke inventaris.

        Menghasilkan:
            AssertionError: Jika item bukan instance dari InventoryItem.
        """
        # Precondition (DbC)
        assert isinstance(
            item, InventoryItem), "item harus berupa instance dari InventoryItem"

        self.items[item.id] = item

        # Postcondition (DbC)
        assert self.items[item.id] == item, "item tidak ditambahkan dengan benar"

    def remove_item(self, item_id: int):
        """Hapus item dari inventaris berdasarkan ID-nya.

        Argumen:
            item_id (int): ID dari item yang akan dihapus.

        Menghasilkan:
            AssertionError: Jika item_id bukan integer atau item tidak ada dalam inventaris.
        """
        # Precondition (DbC)
        assert isinstance(item_id, int), "item_id harus berupa integer"
        assert item_id in self.items, "item tidak ada dalam inventaris"

        del self.items[item_id]

        # Postcondition (DbC)
        assert item_id not in self.items, "item tidak dihapus dengan benar"

    def update_quantity(self, item_id: int, quantity: int):
        """Perbarui jumlah item dalam inventaris.

        Argumen:
            item_id (int): ID dari item yang akan diperbarui.
            quantity (int): Jumlah baru dari item.

        Menghasilkan:
            AssertionError: Jika item_id bukan integer, jumlah bukan integer non-negatif,
                            atau item tidak ada dalam inventaris.
        """
        # Precondition (DbC)
        assert isinstance(item_id, int), "item_id harus berupa integer"
        assert isinstance(
            quantity, int) and quantity >= 0, "jumlah harus berupa integer non-negatif"
        assert item_id in self.items, "item tidak ada dalam inventaris"

        self.items[item_id].quantity = quantity

        # Postcondition (DbC)
        assert self.items[item_id].quantity == quantity, "jumlah tidak diperbarui dengan benar"

    def get_item(self, item_id: int) -> InventoryItem:
        """Dapatkan item dari inventaris berdasarkan ID-nya.

        Argumen:
            item_id (int): ID dari item yang akan diambil.

        Menghasilkan:
            TypeError: Jika item_id bukan integer.
            ValueError: Jika item tidak ada dalam inventaris.

        Mengembalikan:
            InventoryItem: Item dengan ID yang ditentukan.
        """
        # Defensive Programming
        if not isinstance(item_id, int):
            raise TypeError("item_id harus berupa integer")
        if item_id not in self.items:
            raise ValueError("item tidak ada dalam inventaris")

        return self.items[item_id]


def main():
    """Fungsi utama untuk menjalankan sistem manajemen inventaris."""
    inventory = Inventory()

    while True:
        print("\nSistem Manajemen Inventaris")
        print("1. Tambah Item")
        print("2. Hapus Item")
        print("3. Perbarui Jumlah")
        print("4. Lihat Item")
        print("5. Keluar")

        choice = input("Masukkan pilihan Anda: ")

        if choice == '1':
            name = input("Masukkan nama item: ")
            # Defensive Programming
            try:
                quantity = int(input("Masukkan jumlah item: "))
                item = InventoryItem(name, quantity)
                inventory.add_item(item)
                print(
                    f"Item '{name}' ditambahkan dengan jumlah {quantity}. ID adalah {item.id}.")
            except ValueError:
                print("Jumlah tidak valid. Harap masukkan integer non-negatif.")
            except AssertionError as e:
                print(f"Error: {e}")
        elif choice == '2':
            # Defensive Programming
            try:
                item_id = int(input("Masukkan ID item yang akan dihapus: "))
                inventory.remove_item(item_id)
                print(f"Item dengan ID '{item_id}' dihapus dari inventaris.")
            except ValueError:
                print("ID tidak valid. Harap masukkan integer yang valid.")
            except AssertionError as e:
                print(f"Error: {e}")
        elif choice == '3':
            # Defensive Programming
            try:
                item_id = int(input("Masukkan ID item yang akan diperbarui: "))
                quantity = int(input("Masukkan jumlah item baru: "))
                inventory.update_quantity(item_id, quantity)
                print(
                    f"Jumlah item dengan ID '{item_id}' diperbarui menjadi {quantity}.")
            except ValueError:
                print(
                    "Jumlah atau ID tidak valid. Harap masukkan integer non-negatif untuk jumlah dan integer yang valid untuk ID.")
            except AssertionError as e:
                print(f"Error: {e}")
        elif choice == '4':
            print("\nItem Inventaris:")
            for item_id, item in inventory.items.items():
                print(
                    f"ID: {item.id}, Nama: {item.name}, Jumlah: {item.quantity}")
        elif choice == '5':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Harap masukkan angka antara 1 dan 5.")


if __name__ == "__main__":
    main()
