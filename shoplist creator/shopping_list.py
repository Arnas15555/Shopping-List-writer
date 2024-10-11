from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog


def add_to_list():
    item = item_entry.get().strip().capitalize()
    if item:
        with open("shoplist.txt", "a") as data:
            data.write(item + "\n")
        item_entry.delete(0, END)
        update_listbox()
    else:
        messagebox.showwarning("Input Error", "Please enter an item")


def update_listbox():
    with open("shoplist.txt", "r") as data:
        items = data.readlines()
    listbox.delete(0, END)
    for index, item in enumerate(sorted(items), start=1):
        listbox.insert(END, f"{index}. {item.strip()}")


def remove_selected():
    selected_items = listbox.curselection()
    if not selected_items:
        return
    with open("shoplist.txt", "r") as data:
        items = data.readlines()

    remaining_items = [item for i, item in enumerate(items) if i not in selected_items]

    with open("shoplist.txt", "w") as data:
        data.writelines(remaining_items)

    update_listbox()


def clear_all():
    with open("shoplist.txt", "w") as data:
        data.truncate(0)
    update_listbox()


def edit_item():
    selected_item_index = listbox.curselection()
    if not selected_item_index:
        return
    selected_item = listbox.get(selected_item_index)
    edited_item = simpledialog.askstring("Edit Item", "Enter the edited item:",
                                         initialvalue=selected_item.split(". ")[1])
    if edited_item:
        with open("shoplist.txt", "r") as data:
            items = data.readlines()
        items[selected_item_index[0]] = f"{edited_item.capitalize()}\n"
        with open("shoplist.txt", "w") as data:
            data.writelines(items)
        update_listbox()


window = Tk()
window.title("Shopping List")
window.configure(bg="lightgray")

list_frame = Frame(window, bg="lightgray")
list_frame.pack(padx=20, pady=20)

listbox = Listbox(window, width=50, height=15, font=("Helvetica", 12))
listbox.pack(side=LEFT, fill=BOTH, expand=True)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side=RIGHT, fill=Y)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry_frame = Frame(window, bg="lightgray")
entry_frame.pack(padx=20, pady=10)

item_entry = Entry(entry_frame, width=40, font=("Helvetica", 12))
item_entry.pack(side=LEFT, padx=5)

add_button = Button(entry_frame, text="Add item", command=add_to_list, font=("Helvetica", 12))
add_button.pack(side=LEFT, padx=5)

remove_button = Button(window, text="Remove Selected", command=remove_selected, font=("Helvetica", 12))
remove_button.pack(pady=10)

clear_button = Button(window, text="Clear All", command=clear_all, font=("Helvetica", 12))
clear_button.pack(pady=5)

edit_button = Button(window, text="Edit Item", command=edit_item, font=("Helvetica", 12))
edit_button.pack(pady=5)

update_listbox()

window.mainloop()
