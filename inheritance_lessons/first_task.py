

class Editor:
    def view_documents(self):
        pass

    def edit_documents(self):
        display_view = f"Editing documents is not available for free version!"
        return display_view


class ProEditor(Editor):
    def edit_documents(self):
        display_view = f"Key is correctly!"
        return display_view


key = "kerfdswz"
check_key = input(f"Enter your key: ")
if key == check_key:
    test = ProEditor().edit_documents()
else:
    test = Editor().edit_documents()
print(test)
