from tkinter import *
from def_prys
PROG_ONE=["Вобліков Георгій","Боднар Анастасія","Мірва Данило","Asiyka","Asiyka","Asiyka","Угорь","Asiyka","Asiyka","Asiyka","Угорь","Asiyka","Asiyka"]
PROG_TWO=['gergrfg','ewrferf']
WEB=['ergregwer','ryiwnfd']
PROG_OSN=['etujrtht','retfyhrtuh']
OS_KT=['ruy54yer','t46rqytq64']
DATA=['25.12','26.12','27.12','28.12']
root = Tk()
var=IntVar()
variable_progone = StringVar()
variable_progone.set(PROG_ONE[0])

variable_progtwo = StringVar()
variable_progtwo.set(PROG_TWO[0])

variable_web = StringVar()
variable_web.set(WEB[0])

variable_progosn = StringVar()
variable_progosn.set(PROG_OSN[0])

variable_kt = StringVar()
variable_kt.set(OS_KT[0])

variable_data = StringVar()
variable_data.set(DATA[0])

def send_func(event):
    print('тіпа сенд') 
    
def green_func(event):
    kt.pack_forget()
    web.pack_forget()
    prog_osnow.pack_forget()
    prog.pack()
    prog_eng.pack()
    km.pack()
    ps.pack_forget()
    menu_km_one.pack(pady=8,side=TOP)
    menu_eng_one.pack(pady=8,side=TOP)
    menu_prog_one.pack(pady=8,side=TOP)
    menu_km_two.pack_forget()
    menu_eng_two.pack_forget()
    menu_prog_two.pack_forget()
    menu_km_web.pack_forget()
    menu_eng_web.pack_forget()
    menu_prog_web.pack_forget()
    menu_km_kt.pack_forget()
    menu_eng_kt.pack_forget()
    menu_prog_kt.pack_forget()
    menu_km_osn.pack_forget()
    menu_eng_osn.pack_forget()
    menu_prog_osn.pack_forget()

def biruza_func(event):
    kt.pack_forget()
    web.pack_forget()
    prog_osnow.pack_forget()
    prog.pack()
    prog_eng.pack()
    km.pack()
    ps.pack_forget()
    menu_km_two.pack(side=TOP,pady=8)
    menu_eng_two.pack(pady=8,side=TOP)
    menu_prog_two.pack(pady=8,side=TOP)
    menu_km_one.pack_forget()
    menu_eng_one.pack_forget()
    menu_prog_one.pack_forget()
    menu_km_web.pack_forget()
    menu_eng_web.pack_forget()
    menu_prog_web.pack_forget()
    menu_km_osn.pack_forget()
    menu_eng_osn.pack_forget()
    menu_prog_osn.pack_forget()
    menu_km_kt.pack_forget()
    menu_eng_kt.pack_forget()
    menu_prog_kt.pack_forget()

def blue_func(event):
    kt.pack_forget()
    web.pack_forget()
    prog_osnow.pack()
    prog.pack_forget()
    km.pack_forget()
    ps.pack()
    prog_eng.pack()
    menu_km_osn.pack(side=TOP,pady=8)
    menu_eng_osn.pack(pady=8,side=TOP)
    menu_prog_osn.pack(pady=8,side=TOP)
    menu_km_web.pack_forget()
    menu_eng_web.pack_forget()
    menu_prog_web.pack_forget()
    menu_km_one.pack_forget()
    menu_eng_one.pack_forget()
    menu_prog_one.pack_forget()
    menu_km_two.pack_forget()
    menu_eng_two.pack_forget()
    menu_prog_two.pack_forget()
    menu_km_kt.pack_forget()
    menu_eng_kt.pack_forget()
    menu_prog_kt.pack_forget()

def red_func(event):
    kt.pack_forget()
    web.pack()
    prog_osnow.pack_forget()
    prog.pack_forget()
    prog_eng.pack()
    km.pack()
    ps.pack_forget()
    menu_km_web.pack(side=TOP,pady=8)
    menu_eng_web.pack(pady=8,side=TOP)
    menu_prog_web.pack(pady=8,side=TOP)
    menu_km_one.pack_forget()
    menu_eng_one.pack_forget()
    menu_prog_one.pack_forget()
    menu_km_two.pack_forget()
    menu_eng_two.pack_forget()
    menu_prog_two.pack_forget()
    menu_km_osn.pack_forget()
    menu_eng_osn.pack_forget()
    menu_prog_osn.pack_forget()
    menu_km_kt.pack_forget()
    menu_eng_kt.pack_forget()
    menu_prog_kt.pack_forget()

def orange_func(event):
    kt.pack()
    web.pack_forget()
    prog_osnow.pack_forget()
    prog.pack_forget()
    prog_eng.pack()
    ps.pack()
    km.pack_forget()
    menu_km_kt.pack(side=TOP,pady=8)
    menu_eng_kt.pack(pady=8,side=TOP)
    menu_prog_kt.pack(pady=8,side=TOP)
    menu_km_one.pack_forget()
    menu_eng_one.pack_forget()
    menu_prog_one.pack_forget()
    menu_km_two.pack_forget()
    menu_eng_two.pack_forget()
    menu_prog_two.pack_forget()
    menu_km_osn.pack_forget()
    menu_eng_osn.pack_forget()
    menu_prog_osn.pack_forget()
    menu_km_web.pack_forget()
    menu_eng_web.pack_forget()
    menu_prog_web.pack_forget()

#toolbox
toolbox = Frame(root,bg="#FFFFFF",bd=2,height=150)
toolbox.pack(side=TOP,fill=X)

green_img = PhotoImage(file='green.png')
prog_osnow = Button(toolbox, bg='#FFFFFF', bd=0,image=green_img)
prog_osnow.bind('<Button-1>',green_func)
prog_osnow.place(x=20,y=5)
progone = Label(toolbox,bg="#FFFFFF",fg="black",text="Програмування",font='arial 11')
progone.place(x=15,y=105)
progone = Label(toolbox,bg="#FFFFFF",fg="black",text="1",font='arial 11')
progone.place(x=65,y=125)

biruza_img = PhotoImage(file='biruza.png')
prog_group_two = Button(toolbox, bg='#FFFFFF', bd=0,image=biruza_img)
prog_group_two.bind('<Button-1>',biruza_func)
prog_group_two.place(x=150,y=5)
progone = Label(toolbox,bg="#FFFFFF",fg="black",text="Програмування",font='arial 11')
progone.place(x=145,y=105)
progone = Label(toolbox,bg="#FFFFFF",fg="black",text="2",font='arial 11')
progone.place(x=195,y=125)

blue_img = PhotoImage(file='blue.png')
prog_group_one = Button(toolbox, bg='#FFFFFF', bd=0,image=blue_img)
prog_group_one.bind('<Button-1>',blue_func)
prog_group_one.place(x=275,y=5)
progone = Label(toolbox,bg="#FFFFFF",fg="black",text="Основи",font='arial 11')
progone.place(x=295,y=105)
progone = Label(toolbox,bg="#FFFFFF",fg="black",text="Програмування",font='arial 11')
progone.place(x=270,y=125)

red_img = PhotoImage(file='red.png')
web = Button(toolbox, bg='#FFFFFF', bd=0,image=red_img)
web.bind('<Button-1>',red_func)
web.place(x=405,y=5)
progone = Label(toolbox,bg="#FFFFFF",fg="black",text="Web-дизайн",font='arial 11')
progone.place(x=410,y=105)

orange_img = PhotoImage(file='orange.png')
okt = Button(toolbox, bg='#FFFFFF', bd=0,image=orange_img)
okt.bind('<Button-1>',orange_func)
okt.place(x=525,y=5)
progone = Label(toolbox,bg="#FFFFFF",fg="black",text="Основи КТ",font='arial 11')
progone.place(x=535,y=105)

#hardskill menu
hardskillshadow = Frame(root,bg="#535353",bd=2,height=330,width=200)
hardskillshadow.place(x=0,y=155)

hardskill = Frame(root,bg="#FFFFFF",bd=2,height=100,width=100)
hardskill.pack(side=LEFT,ipady=140,ipadx=25,pady=10)

prog = Label(hardskill,width=15,bg="#FFFFFF",fg="black",text="Програмування",font='arial 13')#буде мінятися
web = Label(hardskill,width=15,bg="#FFFFFF",fg="black",text="Web-Дизайн",font='arial 13')#буде мінятися
prog_osnow = Label(hardskill,width=15,bg="#FFFFFF",fg="black",text="Основи прог.",font='arial 13')#буде мінятися
kt = Label(hardskill,width=15,bg="#FFFFFF",fg="black",text="Основи КТ",font='arial 13')#буде мінятися
prog.pack()

menu_prog_one=OptionMenu(hardskill,variable_progone,*PROG_ONE)#буде мінятися
menu_prog_two=OptionMenu(hardskill,variable_progtwo,*PROG_TWO)#буде мінятися
menu_prog_web=OptionMenu(hardskill,variable_web,*WEB)#буде мінятися
menu_prog_osn=OptionMenu(hardskill,variable_progosn,*PROG_OSN)#буде мінятися
menu_prog_kt=OptionMenu(hardskill,variable_kt,*OS_KT)#буде мінятися
menu_prog_one.pack(pady=8,side=TOP)

pr = Label(hardskill,bg="#FFFFFF",fg="black",text="Присутність",font='arial 13')
pr.place(x=40,y=70)

rbutton1=Radiobutton(hardskill,text='✔',variable=var,value=1,bg="#FFFFFF")
rbutton1.place(x=40,y=100)

rbutton2=Radiobutton(hardskill,text='✖',variable=var,value=2,bg="#FFFFFF")
rbutton2.place(x=100,y=100)

dz = Label(hardskill,bg="#FFFFFF",fg="black",text="Домашнє завдання",font='arial 13')
dz.place(x=15,y=130)

dzpoint = Entry(hardskill,width=20,bg='#A580D8')
dzpoint.place(x=30,y=160)

cw = Label(hardskill,bg="#FFFFFF",fg="black",text="Урок",font='arial 13')
cw.place(x=70,y=190)

cwpoint = Entry(hardskill,width=20,bg='#A580D8')
cwpoint.place(x=30,y=220)

send = Button(hardskill,width=20, bg="#FFCF77", text="Send")
send.bind("<Button-1>",send_func)
send.place(x=17,y=265)

#engmenu
hardskillshadow = Frame(root,bg="#535353",bd=2,height=330,width=220)
hardskillshadow.place(x=469,y=155)

eng = Frame(root,bg="#FFFFFF",bd=2,height=100,width=100)
eng.pack(side=RIGHT,ipadx=6,ipady=122)

prog_eng = Label(eng,width=17,bg="#FFFFFF",fg="black",text="Англійська",font='arial 13')#буде мінятися
prog_eng.pack()

menu_eng_one=OptionMenu(eng,variable_progone,*PROG_ONE)#буде мінятися
menu_eng_two=OptionMenu(eng,variable_progtwo,*PROG_TWO)#буде мінятися
menu_eng_web=OptionMenu(eng,variable_web,*WEB)#буде мінятися
menu_eng_osn=OptionMenu(eng,variable_progosn,*PROG_OSN)#буде мінятися
menu_eng_kt=OptionMenu(eng,variable_kt,*OS_KT)#буде мінятися
menu_eng_one.pack(pady=8,side=TOP)

pr = Label(eng,bg="#FFFFFF",fg="black",text="Присутність",font='arial 13')
pr.place(x=35,y=70)

rbutton1=Radiobutton(eng,text='✔',variable=var,value=1,bg="#FFFFFF")
rbutton1.place(x=40,y=100)

rbutton2=Radiobutton(eng,text='✖',variable=var,value=2,bg="#FFFFFF")
rbutton2.place(x=100,y=100)

dz = Label(eng,bg="#FFFFFF",fg="black",text="Домашнє завдання",font='arial 13')
dz.place(x=15,y=130)

dzpoint = Entry(eng,width=20,bg='#A580D8')
dzpoint.place(x=30,y=160)

cw = Label(eng,bg="#FFFFFF",fg="black",text="Урок",font='arial 13')
cw.place(x=70,y=190)

cwpoint = Entry(eng,width=20,bg='#A580D8')
cwpoint.place(x=30,y=220)

send = Button(eng,width=20, bg="#FFCF77", text="Send")
send.bind("<Button-1>",send_func)
send.place(x=17,y=265)

#softmenu
hardskillshadow = Frame(root,bg="#535353",bd=2,height=300,width=220)
hardskillshadow.place(x=225,y=155)

softskill = Frame(root,bg="#FFFFFF",bd=2,height=100,width=100)
softskill.pack(padx=30,ipady=106,ipadx=23,pady=10)

km = Label(softskill,width=17,bg="#FFFFFF",fg="black",text="Критичне мислення",font='arial 13')
km.pack()

ps = Label(softskill,width=17,bg="#FFFFFF",fg="black",text="Психологія спілк.",font='arial 13')

menu_km_one=OptionMenu(softskill,variable_progone,*PROG_ONE)#буде мінятися
menu_km_two=OptionMenu(softskill,variable_progtwo,*PROG_TWO)#буде мінятися
menu_km_web=OptionMenu(softskill,variable_web,*WEB)#буде мінятися
menu_km_osn=OptionMenu(softskill,variable_progosn,*PROG_OSN)#буде мінятися
menu_km_kt=OptionMenu(softskill,variable_kt,*OS_KT)#буде мінятися
menu_km_one.pack(pady=8,side=TOP)

smm = Label(softskill,bg="#FFFFFF",fg="black",text="Присутність",font='arial 13')
smm.place(x=50,y=70)

rbutton12=Radiobutton(softskill,text='✔',variable=var,value=1,bg="#FFFFFF")
rbutton12.place(x=50,y=100)

rbutton22=Radiobutton(softskill,text='✖',variable=var,value=2,bg="#FFFFFF")
rbutton22.place(x=110,y=100)

dzsm = Label(softskill,bg="#FFFFFF",fg="black",text="Домашнє завдання",font='arial 13')
dzsm.place(x=25,y=130)

dzsmpoint = Entry(softskill,width=20,bg='#A580D8')
dzsmpoint.place(x=40,y=160)

cwsm = Label(softskill,bg="#FFFFFF",fg="black",text="Урок",font='arial 13')
cwsm.place(x=80,y=190)

cwsmpoint = Entry(softskill,width=20,bg='#A580D8')
cwsmpoint.place(x=40,y=220)

sendsm = Button(softskill,width=20, bg="#BED371", text="Send")
sendsm.bind("<Button-1>",send_func)
sendsm.place(x=27,y=255)

menu_prog_data=OptionMenu(root,variable_data,*DATA)#буде мінятися
menu_prog_data.place(x=235,y=457.5)

view = Button(root,width=16, bg="#FFCF77", text="Подив. Присутність")
view.bind("<Button-1>",view_func)
view.place(x=315,y=459)

root.title("SoVA")
root["bg"] = "#A580D8"
photo = PhotoImage(file = "fly.png")
root.iconphoto(False, photo)
root.geometry("650x490+300+200")
root.resizable(False,False)
root.mainloop()
