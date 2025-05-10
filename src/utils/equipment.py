class Equipment:
    def __init__(self):
        self.slots = {
            "head": None,
            "arms": None,
            "chest": None,
            "leg": None,
            "foot": None,
            "left_hand": None,
            "right_hand": None,
            "collar": None,
            "ring1": None,
            "ring2": None,
            "ring3": None,
            "ring4": None
        }

    def equip(self, slot, item):
        if slot in self.slots:
            self.slots[slot] = item
            return f"Equipped {item} to {slot}."
        else:
            return "Invalid slot."

    def unequip(self, slot):
        if slot in self.slots and self.slots[slot] is not None:
            item = self.slots[slot]
            self.slots[slot] = None
            return f"Unequipped {item} from {slot}."
        else:
            return "No item to unequip from this slot."

    def get_equipment(self):
        return {slot: item for slot, item in self.slots.items() if item is not None}