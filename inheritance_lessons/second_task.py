

class Rectangle:
    length = 10
    width = 5

    def __str__(self):
        return f"Rectangle with {self.width} cm width and {self.length} cm length!"

    @staticmethod
    def mouse_was_clicked():
        return f"Mouse was clicked!"


class Button(Rectangle):
    button_color = "Red"
    font_text_on_button = "TimesNewRoman"
    border_radius = 2
    border_radius_color = "Black"

    def __str__(self):
        return f"{self.button_color} button;\n" \
               f"{self.font_text_on_button} font;\n" \
               f"{self.border_radius} edging;\n" \
               f"{self.border_radius_color} edging color.\n"


button = Button().__str__()
click = Rectangle.mouse_was_clicked()
print(button)
print(click)




