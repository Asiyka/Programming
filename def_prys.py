def view_func(event):
    prys = Tk()

    toolbox_prys = Frame(prys,bg="#FFFFFF",bd=2,height=150)
    toolbox_prys.pack(side=TOP,fill=X)

    green_img = PhotoImage(file='green.png')
    prog_osnow = Button(toolbox_prys, bg='#FFFFFF', bd=0,image=green_img)
    prog_osnow.bind('<Button-1>',green_func)
    prog_osnow.place(x=20,y=5)
    progone = Label(toolbox_prys,bg="#FFFFFF",fg="black",text="Програмування",font='arial 11')
    progone.place(x=15,y=105)
    progone = Label(toolbox_prys,bg="#FFFFFF",fg="black",text="1",font='arial 11')
    progone.place(x=65,y=125)

    biruza_img = PhotoImage(file='biruza.png')
    prog_group_two = Button(toolbox_prys, bg='#FFFFFF', bd=0,image=biruza_img)
    prog_group_two.bind('<Button-1>',biruza_func)
    prog_group_two.place(x=150,y=5)
    progone = Label(toolbox_prys,bg="#FFFFFF",fg="black",text="Програмування",font='arial 11')
    progone.place(x=145,y=105)
    progone = Label(toolbox_prys,bg="#FFFFFF",fg="black",text="2",font='arial 11')
    progone.place(x=195,y=125)

    blue_img = PhotoImage(file='blue.png')
    prog_group_one = Button(toolbox_prys, bg='#FFFFFF', bd=0,image=blue_img)
    prog_group_one.bind('<Button-1>',blue_func)
    prog_group_one.place(x=275,y=5)
    progone = Label(toolbox_prys,bg="#FFFFFF",fg="black",text="Основи",font='arial 11')
    progone.place(x=295,y=105)
    progone = Label(toolbox_prys,bg="#FFFFFF",fg="black",text="Програмування",font='arial 11')
    progone.place(x=270,y=125)

    red_img = PhotoImage(file='red.png')
    web = Button(toolbox_prys, bg='#FFFFFF', bd=0,image=red_img)
    web.bind('<Button-1>',red_func)
    web.place(x=405,y=5)
    progone = Label(toolbox_prys,bg="#FFFFFF",fg="black",text="Web-дизайн",font='arial 11')
    progone.place(x=410,y=105)

    orange_img = PhotoImage(file='orange.png')
    okt = Button(toolbox_prys, bg='#FFFFFF', bd=0,image=orange_img)
    okt.bind('<Button-1>',orange_func)
    okt.place(x=525,y=5)
    progone = Label(toolbox_prys,bg="#FFFFFF",fg="black",text="Основи КТ",font='arial 11')
    progone.place(x=535,y=105)
    
    prys.title("ПРИСУТНІСТЬ")
    prys["bg"] = "#A580D8"
    prys.geometry("550x390+350+250")
    prys.resizable(False,False)
    prys.mainloop()
