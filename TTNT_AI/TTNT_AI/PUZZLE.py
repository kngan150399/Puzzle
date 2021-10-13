import tkinter
import time
from RUN import Run
start=[]; goal=[]


def Input():
    
    tkNhap=tkinter.Toplevel()
    tkNhap.title("Màn hình Nhập")
    tkNhap.geometry("800x400")
    tkNhap.configure(bg="#FAEBD7")

    # LABEL
    var4=tkinter.StringVar()
    label_Start=tkinter.Label(tkNhap, font=("Arial",30),textvariable=var4,pady=20,padx=20,bg="#FAEBD7")
    var4.set("Start")

        # LABEL
    var5=tkinter.StringVar()
    label_Goal=tkinter.Label(tkNhap, font=("Arial",30),textvariable=var5,pady=20,bg="#FAEBD7")
    var5.set("Goal")

        # LABEL
    var6=tkinter.StringVar()
    label_Chose=tkinter.Label(tkNhap,textvariable=var6,pady=20,bg="#FAEBD7")
    var6.set("   ")

     # LABLE
    label_Start.grid(row=0,column=0)
    label_Goal.grid(row=0,column=5)
    label_Chose.grid(row=0,column=9)
    
    txt1 = tkinter.Entry(tkNhap,width=5)
    txt1.grid(column=1, row=1)

    txt2 = tkinter.Entry(tkNhap,width=5)
    txt2.grid(column=2, row=1)

    txt3 = tkinter.Entry(tkNhap,width=5)
    txt3.grid(column=3, row=1)

    txt4 = tkinter.Entry(tkNhap,width=5)
    txt4.grid(column=1, row=2)
    txt5 = tkinter.Entry(tkNhap,width=5)
    txt5.grid(column=2, row=2)

    txt6 = tkinter.Entry(tkNhap,width=5)
    txt6.grid(column=3, row=2)

    txt7 = tkinter.Entry(tkNhap,width=5)
    txt7.grid(column=1, row=3)

    txt8 = tkinter.Entry(tkNhap,width=5)
    txt8.grid(column=2, row=3)

    txt9 = tkinter.Entry(tkNhap,width=5)
    txt9.grid(column=3, row=3) 

        # KHUNG GOAL
    tbox1 = tkinter.Entry(tkNhap,width=5)
    tbox1.grid(column=6, row=1)

    tbox2 = tkinter.Entry(tkNhap,width=5)
    tbox2.grid(column=7, row=1)

    tbox3 = tkinter.Entry(tkNhap,width=5)
    tbox3.grid(column=8, row=1)

    tbox4 = tkinter.Entry(tkNhap,width=5)
    tbox4.grid(column=6, row=2)

    tbox5 = tkinter.Entry(tkNhap,width=5)
    tbox5.grid(column=7, row=2)

    tbox6 = tkinter.Entry(tkNhap,width=5)
    tbox6.grid(column=8, row=2)

    tbox7 = tkinter.Entry(tkNhap,width=5)
    tbox7.grid(column=6, row=3)

    tbox8 = tkinter.Entry(tkNhap,width=5)
    tbox8.grid(column=7, row=3)

    tbox9 = tkinter.Entry(tkNhap,width=5)
    tbox9.grid(column=8, row=3)

    #==================================================================================

        
    
    def Submit():
        global start,goal
        row=[]
        row+=[txt1.get()]
        row+=[txt2.get()]
        row+=[txt3.get()]
        start+=[row]

        row=[txt4.get()]
        row+=[txt5.get()]
        row+=[txt6.get()]
        start+=[row]
           

        row=[txt7.get()]
        row+=[txt8.get()]
        row+=[txt9.get()]
        start+=[row]
            
        
        row=[]
        row+=[tbox1.get()]
        row+=[tbox2.get()]
        row+=[tbox3.get()]
        goal+=[row]
           
        row=[tbox4.get()]  
        row+=[tbox5.get()]
        row+=[tbox6.get()]
        goal+=[row]
            
        row=[tbox7.get()]
        row+=[tbox8.get()]
        row+=[tbox9.get()]
        goal+=[row]
        
        #tkNhap.destroy()
    # BUTTON
    btnOK=tkinter.Button(tkNhap,text="OK",command=Submit,width=20,height=2,bg="#20B2AA")
    btnExit=tkinter.Button(tkNhap,text="Exit",command=tkNhap.destroy,width=20,height=2,bg="#20B2AA")
    btnOK.grid(row=2,column=10)
    btnExit.grid(row=3,column=10)
    
    
        
    
    tkNhap.mainloop()
    #return start,goal
#==================== End of Input ===============================
def RunMain():
    Run(start, goal)

def Main():
    main=tkinter.Tk()
    main.title("Tri Tue Nhan Tao - 8 Puzzle A*")
    main.configure(bg="#FAEBD7")
    main.geometry("260x300")

    
    label = tkinter.Label(main, text="8 PUZZLE A*", font=("Arial",30),bg="#FAEBD7").grid(row=0, columnspan=3)
    gia_lb1 = tkinter.Label(main,width=3,bg="#FAEBD7")
    gia_lb2 = tkinter.Label(main,width=3,bg="#FAEBD7")
    gia_lb3 = tkinter.Label(main,width=3,bg="#FAEBD7")

    # BUTTON
    btnNhap=tkinter.Button(main,text="Nhập",command=Input,width=20,height=2,bg="#20B2AA")
    btnBat_dau=tkinter.Button(main,text="Bắt Đầu",command=RunMain,width=20,height=2,bg="#20B2AA")
    btnThoat=tkinter.Button(main,text="Thoát",command=main.destroy,width=20,height=2,bg="#20B2AA")


    gia_lb1.grid(row=1,column=0)
    btnNhap.grid(row=2,column=1)
    gia_lb2.grid(row=3,column=1)
    btnBat_dau.grid(row=4,column=1)
    gia_lb3.grid(row=5,column=1)
    btnThoat.grid(row=6,column=1)


    main.mainloop()

if __name__ == '__main__':
    Main()
