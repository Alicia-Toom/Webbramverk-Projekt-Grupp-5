class Carousel:
    def __init__(self, items, max_rows=5, items_per_row=4):
        self.items = items
        self.max_rows = max_rows
        self.items_per_row = items_per_row

    def rows(self):
        rows = [self.items[i:i + self.items_per_row] for i in range(0, len(self.items), self.items_per_row)]
        return rows[0:self.max_rows]
