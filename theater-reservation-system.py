import tkinter as tk
from tkinter import *

timeslots = ["8:00", "11:00", "14:00", "17:00", "20:00", "21:00"]

root = Tk()
root.title('Directory - ADMINS ONLY')
root.geometry("600x500")

def filmsel():
    root = Tk()
    root.title('Select Film - ADMIN ONLY')
    root.geometry("600x500")

    def hall1():
        class Hall1Reservation:
            def __init__(self, parent):
                self.parent = parent
                self.parent.title("Hall 1 Reservation")

                self.rows = 5
                self.columns = 6

                self.seating_frame = tk.Frame(parent)
                self.seating_frame.pack()

                self.create_seats()

            def create_seats(self):
                self.seat_buttons = []

                for row in range(self.rows):
                    seat_row = []
                    for col in range(self.columns):
                        seat_button = tk.Button(self.seating_frame, text=f"Seat {row+1}-{col+1}", width=8, height=2, command=lambda r=row, c=col: self.reserve_seat(r, c))
                        seat_button.grid(row=row, column=col, padx=5, pady=5)
                        seat_row.append(seat_button)
                    self.seat_buttons.append(seat_row)

            def reserve_seat(self, row, col):
                seat_button = self.seat_buttons[row][col]
                if seat_button['state'] == 'normal':
                    seat_button.configure(bg='lightgreen', state='disabled')
                    print(f"Reserved Seat {row+1}-{col+1}")
                else:
                    print(f"Seat {row+1}-{col+1} has already been reserved.")

        if __name__ == "__main__":
            parent = tk.Tk()
            app = Hall1Reservation(parent)
            parent.mainloop()

    def hall2():
        class Hall2Reservation:
            def __init__(self, parent):
                self.parent = parent
                self.parent.title("Hall 2 Reservation")

                self.rows = 7
                self.columns = 6

                self.seating_frame = tk.Frame(parent)
                self.seating_frame.pack()

                self.create_seats()

            def create_seats(self):
                self.seat_buttons = []

                for row in range(self.rows):
                    seat_row = []
                    for col in range(self.columns):
                        seat_button = tk.Button(self.seating_frame, text=f"Seat {row+1}-{col+1}", width=8, height=2, command=lambda r=row, c=col: self.reserve_seat(r, c))
                        seat_button.grid(row=row, column=col, padx=5, pady=5)
                        seat_row.append(seat_button)
                    self.seat_buttons.append(seat_row)

            def reserve_seat(self, row, col):
                seat_button = self.seat_buttons[row][col]
                if seat_button['state'] == 'normal':
                    seat_button.configure(bg='lightgreen', state='disabled')
                    print(f"Reserved Seat {row+1}-{col+1}")
                else:
                    print(f"Seat {row+1}-{col+1} has already been reserved.")

        if __name__ == "__main__":
            parent = tk.Tk()
            app = Hall2Reservation(parent)
            parent.mainloop()

    def hall3():
        class Hall3Reservation:
            def __init__(self, parent):
                self.parent = parent
                self.parent.title("Hall 3 Reservation")

                self.rows = 10
                self.columns = 8

                self.seating_frame = tk.Frame(parent)
                self.seating_frame.pack()

                self.create_seats()

            def create_seats(self):
                self.seat_buttons = []

                for row in range(self.rows):
                    seat_row = []
                    for col in range(self.columns):
                        seat_button = tk.Button(self.seating_frame, text=f"Seat {row+1}-{col+1}", width=8, height=2, command=lambda r=row, c=col: self.reserve_seat(r, c))
                        seat_button.grid(row=row, column=col, padx=5, pady=5)
                        seat_row.append(seat_button)
                    self.seat_buttons.append(seat_row)

            def reserve_seat(self, row, col):
                seat_button = self.seat_buttons[row][col]
                if seat_button['state'] == 'normal':
                    seat_button.configure(bg='lightgreen', state='disabled')
                    print(f"Reserved Seat {row+1}-{col+1}")
                else:
                    print(f"Seat {row+1}-{col+1} has already been reserved.")

        if __name__ == "__main__":
            parent = tk.Tk()
            app = Hall3Reservation(parent)
            parent.mainloop()


    Hall1_button = Button(root, text='Hall1', bg='lightgreen', command=hall1)
    Hall1_button.pack(pady=10)
    Hall2_button = Button(root, text='Hall2', bg='lightgreen', command=hall2)
    Hall2_button.pack(pady=10)
    Hall3_button = Button(root, text='Hall3', bg='lightgreen', command=hall3)
    Hall3_button.pack(pady=10)

def filmcheck():
    root = Tk()
    root.title('Add/Subtract Films - ADMIN ONLY')
    root.geometry("600x500")
    def open_txt():
        text_file = open("films.txt", 'r')
        showtxt = text_file.read()

        my_text.insert(END, showtxt)
        text_file.close()

    def save_txt():
        text_file = open("films.txt", 'w')
        text_file.write(my_text.get(1.0, END))

    def deltxt():
        open('films.txt', 'w').close()

    def eraser():
        my_text.delete("1.0", "end")

    def addfilm():
        text_file = open("films.txt", 'w')
        text_file.write(my_text.get(1.0, END))
        root = Tk()
        root.title('Add Film - ADMIN ONLY')
        root.geometry("600x500")


        timeslot1_button = Button (root, text='Time slot 1 - 8:00', command=print('Time slot 1 saved'))
        timeslot1_button.pack(pady=10)

        timeslot2_button = Button (root, text='Time slot 2 - 11:00', command=print('Time slot 2 saved'))
        timeslot2_button.pack(pady=10)

        timeslot3_button = Button (root, text='Time slot 3 - 14:00', command=print('Time slot 3 saved'))
        timeslot3_button.pack(pady=10)

        timeslot4_button = Button (root, text='Time slot 4 - 17:00', command=print('Time slot 4 saved'))
        timeslot4_button.pack(pady=10)

        timeslot5_button = Button (root, text='Time slot 5 - 20:00', command=print('Time slot 5 saved'))
        timeslot5_button.pack(pady=10)

        timeslot6_button = Button (root, text='Time slot 6 - 21:00', command=print('Time slot 6 saved'))
        timeslot6_button.pack(pady=10)


    my_text = Text(root, width=70, height=10)
    my_text.pack(pady=20)

    addfilm_button = Button(root, text='Add Film', bg='lightgreen', command=addfilm)
    addfilm_button.pack(pady=10)

    seefilm_button = Button(root, text="See Films", command=open_txt)
    seefilm_button.pack(pady=10)

    cleartxt_button = Button(root, text="Delete File", bg='red', command=deltxt)
    cleartxt_button.pack(pady=10)

    erasetxt_button = Button(root, text="Erase", bg ='red', command=eraser)
    erasetxt_button.pack(pady=10)

films_button = Button(root, text="Add/Subtract Film", bg='pink', command=filmcheck)
films_button.pack(pady=20)

seats_button = Button(root, text="Reserve Seats", bg='lightblue', command=filmsel)
seats_button.pack(padx=20)

root.mainloop()
