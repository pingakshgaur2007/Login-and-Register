from tkinter import *
import os


# =========================================
# Other Functions


def saved():
    global root8

    root8 = Toplevel(root7)
    root8.geometry("100x100+100+100")
    root8.title("Saved!")

    Label(root8, text='Saved!').pack()
    Label(root8, text='').pack()
    Button(root8, text='Close', width=5, height=1, command=close8).pack()

    root8.mainloop()


def save():
    filename = raw_filename.get()
    notes = raw_notes.get()

    data = open(filename + '.txt', 'w')
    data.write(notes)
    data.close()

    saved()


def view_notes1():
    global root10

    root10 = Toplevel(root6)
    root10.geometry("400x400+100+100")
    root10.title("View Notes")

    filename1 = raw_filename1.get()

    data = open(filename1 + '.txt', 'r')
    data1 = data.read()

    Label(root10, text='').pack()
    Label(root10, text=data1).pack()
    Label(root10, text='').pack()
    Button(root10, text='Close', width=5, height=1, command=close10).pack()

    data.close()


def delete_notes1():
    global root12

    root12 = Toplevel(root6)
    root12.geometry("150x100+100+100")
    root12.title("Deleted!")

    filename2 = raw_filename2.get()

    os.remove(filename2 + '.txt')

    Label(root12, text=filename2 + " is removed!").pack()
    Label(root12, text='').pack()
    Button(root12, text='Close', width=5, height=1, command=close12).pack()


# =========================================
# Create, View & Delete notes options


def create_notes():
    global root7

    root7 = Toplevel(root6)
    root7.geometry("400x400+100+100")
    root7.title("Create Notes")

    global raw_filename
    global raw_notes

    raw_filename = StringVar()
    raw_notes = StringVar()

    Label(root7, text='').pack()
    Label(root7, text='').pack()

    Label(root7, text='Please Enter the Filename below *').pack()
    Entry(root7, textvariable=raw_filename).pack()

    Label(root7, text='').pack()

    Label(root7, text='Please Enter the Notes below *').pack()
    Entry(root7, textvariable=raw_notes).pack()

    Label(root7, text='').pack()

    Button(root7, text='Save', command=save).pack()
    Label(root7, text='').pack()
    Button(root7, text='Close', width=5, height=1, command=close7).pack()


def view_notes():
    global root9

    root9 = Toplevel(root6)
    root9.geometry("400x400+100+100")
    root9.title("View Notes")

    global raw_filename1

    raw_filename1 = StringVar()

    all_files = os.listdir()

    Label(root9, text='Please select one of these notes *').pack()
    Label(root9, text=all_files).pack()
    Entry(root9, textvariable=raw_filename1).pack()

    Label(root9, text='').pack()

    Button(root9, text='Ok', command=view_notes1).pack()

    Label(root9, text='').pack()
    Button(root9, text='Close', width=5, height=1, command=close9).pack()


def delete_notes():
    global root11

    root11 = Toplevel(root6)
    root11.geometry("400x400+100+100")
    root11.title("Delete Notes")

    global raw_filename2

    raw_filename2 = StringVar()

    delete_files = os.listdir()

    Label(root11, text='Please select one of these notes to delete them *').pack()
    Label(root11, text=delete_files).pack()
    Entry(root11, textvariable=raw_filename2).pack()

    Label(root11, text='').pack()
    Button(root11, text='Ok', command=delete_notes1).pack()
    Label(root11, text='').pack()
    Button(root11, text='Close', width=5, height=1, command=close11).pack()


# =========================================
# Main Session - Dashboard


def session():
    global root6

    root6 = Toplevel(root3)
    root6.geometry("400x400+100+100")
    root6.title("Dashboard")

    Label(root6, text='Welcome to Dashboard!', bg='grey',
          width=300, height=2, font='Calibri 13').pack()

    Label(root6, text='').pack()
    Button(root6, text='Create Notes', command=create_notes).pack()

    Label(root6, text='').pack()
    Button(root6, text='View Notes', command=view_notes).pack()

    Label(root6, text='').pack()
    Button(root6, text='Delete Notes', command=delete_notes).pack()

    Label(root6, text='').pack()
    Button(root6, text='Close', width=5, height=1, command=close6).pack()

    root6.mainloop()


# =========================================
# Different Possibilities in Login System


def login_sucessful():
    session()


def password_not_found():
    global root4

    root4 = Toplevel(root3)
    root4.geometry("100x100+100+100")
    root4.title("Password not Found!")

    Label(root4, text='Password not Found...').pack()
    Label(root4, text='').pack()
    Button(root4, text='Close', width=5, height=1, command=close3).pack()

    root4.mainloop()


def user_not_found():
    global root5

    root5 = Toplevel(root3)
    root5.geometry("100x100+100+100")
    root5.title("User not Found!")

    Label(root5, text='User not Found...').pack()
    Label(root5, text='').pack()
    Button(root5, text='Close', width=5, height=1, command=close4).pack()

    root5.mainloop()


# =========================================
# Window Destroyers


def close1():
    root1.destroy()


def close2():
    root2.destroy()


def close3():
    root4.destroy()


def close4():
    root5.destroy()


def close5():
    root3.destroy()


def close6():
    root6.destroy()


def close7():
    root7.destroy()


def close8():
    root8.destroy()


def close9():
    root9.destroy()


def close10():
    root10.destroy()


def close11():
    root11.destroy()


def close12():
    root12.destroy()


# =========================================
# User Verification & User Registration


def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, 'w')
    file.write(username_info + '\n')
    file.write(password_info + '\n')
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(root2, text='Registration Sucessful!',
          fg='green').pack()
    Button(root2, text='Close', command=close2).pack()


def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()

    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir()

    if username1 in list_of_files:
        file1 = open(username1, 'r')
        verify = file1.read().splitlines()

        if password1 in verify:
            login_sucessful()

        else:
            password_not_found()

    else:
        user_not_found()


# =========================================
# Login & Register Function


def register():
    global root2

    root2 = Toplevel(root1)
    root2.geometry("300x250+100+100")
    root2.title("Register")

    global username_entry
    global password_entry
    global username
    global password

    username = StringVar()
    password = StringVar()

    Label(root2, text='Please enter the details below *').pack()
    Label(root2, text='').pack()

    Label(root2, text='Username *').pack()

    username_entry = Entry(root2, bd=2, textvariable=username)
    username_entry.pack()

    Label(root2, text='Password *').pack()

    password_entry = Entry(root2, bd=2, textvariable=password)
    password_entry.pack()
    Label(root2, text='').pack()

    Button(root2, text='Register', command=register_user).pack()

    root2.mainloop()


def login():
    global root3

    root3 = Toplevel(root1)
    root3.geometry("300x250+100+100")
    root3.title("Login")

    global username_verify
    global password_verify
    global username_entry1
    global password_entry1

    username_verify = StringVar()
    password_verify = StringVar()

    Label(root3, text='Please enter the details below *').pack()
    Label(root3, text='').pack()

    Label(root3, text='Username *').pack()

    username_entry1 = Entry(root3, bd=2, textvariable=username_verify)
    username_entry1.pack()

    Label(root3, text='Password *').pack()

    password_entry1 = Entry(root3, bd=2, textvariable=password_verify)
    password_entry1.pack()
    Label(root3, text='').pack()

    Button(root3, text='Login', command=login_verify).pack()
    Label(root3, text='').pack()
    Button(root3, text='Close', width=5, height=1, command=close5).pack()

    root3.mainloop()


# =========================================
# Main Function

def my_window():
    global root1

    root1 = Tk()
    root1.geometry("300x250+100+100")
    root1.title("Notes")

    Label(root1, text='Notes', width=300, height=2,
          bg='grey', font='Calibri 18').pack()
    Label(root1, text='').pack()

    Button(root1, text='Login', width=20, height=1,
           font='Calirbi 13', command=login).pack()
    Label(root1, text='').pack()

    Button(root1, text='Register', width=20, height=1,
           command=register, font='Calirbi 13').pack()
    Label(root1, text='').pack()

    Button(root1, text='Close', width=5, height=1, command=close1).pack()

    root1.mainloop()


my_window()
