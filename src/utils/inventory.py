class Inventory:
    def __init__(self):
        self.slots = [None] * 4  # Four inventory slots

    def add_item(self, item, slot):
        if 0 <= slot < len(self.slots):
            if self.slots[slot] is None:
                self.slots[slot] = item
                return True
            else:
                return False  # Slot is already occupied
        return False  # Invalid slot

    def remove_item(self, slot):
        if 0 <= slot < len(self.slots):
            item = self.slots[slot]
            self.slots[slot] = None
            return item
        return None  # Invalid slot

    def __str__(self):
        return f"Inventory: {self.slots}"