from tkinter import *
from datetime import *
from random import *
class HoverButton(Button):
    def __init__(self, master, **kw):
        Button.__init__(self,master=master,**kw)
        self.defaultbackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
    def on_enter(self, e):
        self["background"] = self['activebackground']
    def on_leave(self, e):
        self["background"] = self.defaultbackground
def vidj1():
    def check_time():
        vremya = datetime.now().time()
        ent1.insert(0, vremya.strftime('%H:%M:%S '))
    
    root1= Tk()
    root1.title("Время сейчас")
    ent1= Entry(root1, width=50)
    ent1.pack()
    now_time=Button(root1, text="Нажмите чтобы узнать время", command=check_time)
    now_time.pack()
    window_width = 200
    window_height = 200
    x_menu = 600
    y_menu = 350
    root1.geometry(f"{window_width}x{window_height}+{x_menu}+{y_menu}")
    root1.mainloop()

def vidj2():
    root2 = Tk()
    window_width = 200
    window_height = 150
    x_menu = 600
    y_menu = 590
    root2.geometry(f"{window_width}x{window_height}+{x_menu}+{y_menu}")
    f_top = Frame(root2)
    f_bot = Frame(root2)
    l1 = Label(f_top, width=7, height=4,
bg='yellow', text="1")
    l2 = Label(f_top, width=7, height=4,
bg='orange', text="2")
    l3 = Label(f_bot, width=7, height=4,
bg='lightgreen', text="3")
    l4 = Label(f_bot, width=7, height=4,
bg='lightblue', text="4")
    f_top.pack(padx=10, pady=5)
    f_bot.pack(padx=10, pady=5)
    l1.pack(side=LEFT)
    l2.pack(side=LEFT)
    l3.pack(side=LEFT)
    l4.pack(side=LEFT)
    root2.mainloop()

def dismiss(window):
    window.destroy()

def daycycle_check():
    daycycle = Toplevel()
    x_offset = root.winfo_x() - 210
    y_offset = root.winfo_y() - 280
    daycycle.geometry("+{}+{}".format(x_offset, y_offset))
    daycycle.title("Переключение дня/ночи")
    daycycle.geometry("200x250")
    daycycle.protocol("DELETE", lambda: dismiss(daycycle))
    def change_bg():
        value = check_var.get()
        if value==1:
            daycycle.config(bg="black")
        elif value==0:
            daycycle.config(bg="white")
    check_var = IntVar()
    
    check_button = Checkbutton(daycycle, text="День/Ночь", variable=check_var, offvalue=0, onvalue=1, command=change_bg)
    check_button.pack()
    close_button = Button(daycycle, text="Закрыть окно", command=lambda: dismiss(daycycle))
    close_button.pack()

def canvas():
    paint= Toplevel()
    x_offset = root.winfo_x() + 310
    y_offset = root.winfo_y() - 53
    paint.geometry("+{}+{}".format(x_offset, y_offset))
    paint.title("paint?")
    brush_color = 'Black'
    brush_size = 1
    def col1(event):
        nonlocal brush_color 
        brush_color='blue'
    def col2(event):
        nonlocal brush_color
        brush_color='red'
    def col3(event):
        nonlocal brush_color
        brush_color='black'
    def painter(event):
        nonlocal brush_color, brush_size
        x1=event.x+brush_size
        y1=event.y+brush_size
        x2=event.x-brush_size
        y2=event.y-brush_size
        cvs1.create_oval(x1,y1,x2,y2,fill=brush_color, outline=brush_color)
    def clear():
        cvs1.delete("all")
        blue_color= cvs1.create_oval(10,10,30,30,fill='blue')
        red_color= cvs1.create_oval(70,10,90,30,fill='red')
        black_color= cvs1.create_oval(40,10,60,30, fill='black')
        cvs1.tag_bind(blue_color, '<Button-1>', col1)
        cvs1.tag_bind(red_color, '<Button-1>', col2)
        cvs1.tag_bind(black_color, '<Button-1>', col3)
    def check_if_negative():
        nonlocal brush_size
        if brush_size<=1:
            brush_size=1
            paint.update_idletasks()
    def size_change(event):
        nonlocal brush_size
        check_if_negative()
        brush_size += 1
        size=Label(paint,text="{}".format(brush_size))
        size.place(x=225, y=0, width=50, height=50)
    def size_change_(event):
        nonlocal brush_size
        check_if_negative()
        brush_size -= 1
        size=Label(paint,text="{}".format(brush_size))
        size.place(x=225, y=0, width=50, height=50)
    size=Label(paint,text="{}".format(brush_size))
    size.place(x=225, y=0, width=50, height=50)    
    cvs1=Canvas(paint, width=500, height=448, bg="white")
    cvs1.pack()
    clean=Button(paint,text=("Очистить экран"), command=clear)
    clean.place(x=400, y=0, width=100, height=50)
    blue_color= cvs1.create_oval(10,10,30,30,fill='blue')
    red_color= cvs1.create_oval(70,10,90,30,fill='red')
    black_color= cvs1.create_oval(40,10,60,30, fill='black')
    cvs1.tag_bind(blue_color, '<Button-1>', col1)
    cvs1.tag_bind(red_color, '<Button-1>', col2)
    cvs1.tag_bind(black_color, '<Button-1>', col3)
    cvs1.bind('<Button1-Motion>', painter)
    cvs1.bind('<MouseWheel>', size_change_)
    cvs1.bind('<Shift-MouseWheel>', size_change)

def listbox():
    box = Toplevel()
    x_offset = root.winfo_x() - 0
    y_offset = root.winfo_y() - 280
    box.geometry("+{}+{}".format(x_offset, y_offset))
    box.title("listbox adder")
    def add_item():
        text= entry.get().strip()
        if text:
            lbox.insert(END, entry.get())
            entry.delete(0, END)
    def add_random():
        for _ in range(3):
            randnum = randint(-100,100)
            lbox.insert(END, randnum)
        entry.delete(0, END)
    def del_list():
        select = list(lbox.curselection())
        select.reverse()
        for i in select:
            lbox.delete(i)
    def calculate():
        numbers = []
        for i in range(lbox.size()):
            try:
                num = int(lbox.get(i))
                numbers.append(num)
            except ValueError:
                print(f"Ошибка: Значение в индексе {i} не число")
                return
        if len(numbers) <= 99:
            if numbers:
                result = min(numbers)
                result_label.config(text=f"Мин число: {result}")
            else:
                result_label.config(text="Список пуст.")
        else:
            result_label.config(text="ошибка: слишком много чисел")

    def print_list():
        text = lbox.get(0, END)
        if text:
            print(lbox.get(0, END))

    lbox = Listbox(box, width=22, height=15)
    lbox.pack(side=LEFT)
    scroll = Scrollbar(box, command=lbox.yview)
    scroll.pack(side=LEFT, fill=Y)
    lbox.config(yscrollcommand=scroll.set)

    result_label = Label(box, text="Мин число: ")
    result_label.place(x=185, y=200)
    f = Frame(box)
    f.pack(side=RIGHT, padx=10)
    entry = Entry(f)
    entry.pack(anchor=N)
    Button(f, text="Добавить", command=add_item).pack(fill=X)
    Button(f, text="Удалить", command=del_list).pack(fill=X)
    Button(f, text="Вывод", command=print_list).pack(fill=X)
    Button(f, text="Сгенерировать", command=add_random).pack(fill=X)
    Button(f, text="Найти минимальное", command=calculate).pack(fill=X)

def scalar():
    scaler = Toplevel()
    x_offset = root.winfo_x() + 310
    y_offset = root.winfo_y() - 280
    scaler.geometry("+{}+{}".format(x_offset, y_offset))
    scaler.title("custom color")
    def bg_upd(_):
        color_c = '#%02x%02x%02x' % (scale1.get(), scale2.get(), scale3.get())
        col_button.config(bg=color_c)
        col_button.config(text="Цвет:{}".format(color_c))
    def copy_col():
        color_c = '#%02x%02x%02x' % (scale1.get(), scale2.get(), scale3.get())
        scaler.clipboard_clear()
        scaler.clipboard_append(color_c)
    scale1 = Scale(scaler, orient=HORIZONTAL, length=393, from_=0, to=255, bg="red",resolution=1, command=bg_upd)
    scale1.grid(row=0, column=0, padx=5, pady=10)
    scale2 = Scale(scaler, orient=HORIZONTAL, length=393, from_=0, to=255, bg="green",resolution=1, command=bg_upd)
    scale2.grid(row=1, column=0, padx=5, pady=10)
    scale3 = Scale(scaler, orient=HORIZONTAL, length=393, from_=0, to=255, bg="blue",resolution=1, command=bg_upd)
    scale3.grid(row=2, column=0, padx=5, pady=10)

    col_button=Button(scaler, text="Цвет", width=10, command=copy_col)
    col_button.grid(row=1, column=1, padx=7)
    
root = Tk()
root.title("Vidgets")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 300
window_height = 400
x = (screen_width//2) - (window_width//2)
y = (screen_height//2) - (window_height//2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
label = Label(root, text = "Меню виджетов")
label.pack()
vidj_ONE = HoverButton(root, text="Виджет Entry", width=10, height=5, activebackground='#555555', command=vidj1)
vidj_ONE.place(x=20,y=50)
vidj_TWO = HoverButton(root, text="Виджет Label", width=10, height=5, activebackground='#555555', command=vidj2)
vidj_TWO.place(x=110,y=50)
vidj_THREE = HoverButton(root, text="Виджет Check", width=10, height=5, activebackground='#555555', command=daycycle_check)
vidj_THREE.place(x=200,y=50)
vidj_FOUR = HoverButton(root, text="Виджет canvas", width=10, height=5, activebackground='#555555', command=canvas)
vidj_FOUR.place(x=20,y=175)
vidj_FIVE = HoverButton(root, text="Виджет listbox", width=10, height=5, activebackground='#555555', command=listbox)
vidj_FIVE.place(x=110,y=175)
vidj_SIX = HoverButton(root, text="Виджет Scale", width=10, height=5, activebackground='#555555', command=scalar)
vidj_SIX.place(x=200,y=175)
lab1= Label(text="При нажатии на кнопку виджета открывается окно с ним", font="Arial 8")
lab1.pack(side="top")

root.mainloop()
