class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        return self.RectangleIterator(self.length, self.width)

    class RectangleIterator:
        def __init__(self, length: int, width: int):
            self.attributes = [{'length': length}, {'width': width}]
            self.index = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.index < len(self.attributes):
                result = self.attributes[self.index]
                self.index += 1
                return result
            else:
                raise StopIteration


try:
    length = int(input("Enter the length of the rectangle: "))
    width = int(input("Enter the width of the rectangle: "))
except ValueError:
    print("Please enter valid integer values for length and width.")
    exit()

rect = Rectangle(length, width)

for attr in rect:
    print(attr)
