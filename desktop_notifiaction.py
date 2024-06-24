from tkinter import *
from plyer import notification
from tkinter import messagebox
import time

# Function to get details and set notification
def get_details():
    get_title = title.get()
    get_msg = msg.get()
    get_time = time1.get()
    
    if not get_title or not get_msg or not get_time:
        messagebox.showerror("Alert", "All fields are required!")
        return
    
    try:
        int_time = int(float(get_time))
    except ValueError:
        messagebox.showerror("Alert", "Time must be a number!")
        return
    
    min_to_sec = int_time * 60
    messagebox.showinfo("Notifier Set", f"Notification will be displayed in {get_time} minutes.")
    t.destroy()
    time.sleep(min_to_sec)

    notification.notify(
        title=get_title,
        message=get_msg,
        app_name="Notifier",
        app_icon="ico.ico",  # Ensure 'ico.ico' exists or provide a valid path
        toast=True,
        timeout=10,
    )

def round_rectangle(canvas, x1, y1, x2, y2, radius=25, **kwargs):
    points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y2-radius,
              x1, y1+radius,
              x1, y1+radius,
              x1, y1]

    return canvas.create_polygon(points, **kwargs, smooth=True)

# Initialize the main window
t = Tk()
t.title("Notifier")
t.geometry("600x500")  # Adjusted window size
t.configure(bg='#2C3E50')

# Create a canvas for rounded corners
canvas = Canvas(t, bg='#2C3E50', bd=0, highlightthickness=0)
canvas.place(relwidth=1, relheight=1)

# Create a longer rounded rectangle for the main frame
round_rectangle(canvas, 10, 10, 590, 490, radius=20, fill='#34495E', outline='')

# Add a heading
heading = Label(t, text="NOTIFICATION", font=("Helvetica", 18, "bold"), bg='#34495E', fg='white')
heading.place(relx=0.5, rely=0.1, anchor='center')

# Title Label and Entry
t_label = Label(t, text="Title to Notify", font=("Helvetica", 10), bg='#34495E', fg='white')
t_label.place(relx=0.15, rely=0.3, anchor='e')
title = Entry(t, width=30, font=("Helvetica", 13), bg='#2C3E50', fg='white', insertbackground='white', bd=0)
title.place(relx=0.55, rely=0.3, anchor='w', x=10, y=5)

# Message Label and Entry
m_label = Label(t, text="Message", font=("Helvetica", 10), bg='#34495E', fg='white')
m_label.place(relx=0.15, rely=0.4, anchor='e')
msg = Entry(t, width=30, font=("Helvetica", 13), bg='#2C3E50', fg='white', insertbackground='white', bd=0)
msg.place(relx=0.55, rely=0.4, anchor='w', x=10, y=5)

# Time Label and Entry
time_label = Label(t, text=" Set Time (min)", font=("Helvetica", 10), bg='#34495E', fg='white')
time_label.place(relx=0.15, rely=0.5, anchor='e')
time1 = Entry(t, width=10, font=("Helvetica", 13), bg='#2C3E50', fg='white', insertbackground='white', bd=0)
time1.place(relx=0.55, rely=0.5, anchor='w', x=10, y=5)
time_min_label = Label(t, text="min", font=("Helvetica", 10), bg='#34495E', fg='white')
time_min_label.place(relx=0.75, rely=0.5, anchor='w', y=5)

# Text widget outside the notification box
info_text = Text(t, width=50, height=6, font=("Helvetica", 12), wrap=WORD, bg='#34495E', fg='white', bd=0)
info_text.insert(END, "Additional Information or Instructions...\n")
info_text.place(relx=0.5, rely=0.85, anchor='center')

# Set Notification Button
but = Button(
    t,
    text="SET NOTIFICATION",
    font=("Helvetica", 10, "bold"),
    fg="#ffffff",
    bg="#2980B9",
    width=20,
    relief="raised",
    command=get_details,
    activebackground="#3498DB",
    activeforeground="white",
    bd=0
)
but.place(relx=0.5, rely=0.65, anchor='center', y=10)

# Prevent resizing
t.resizable(0, 0)
# Start the main loop
t.mainloop()
