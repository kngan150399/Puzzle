import tkinter
from tkinter import *
import tkinter as tk
import time
#start=[['1','2','3'],['_','4','6'],['7','5','8']]; goal=[['1','2','3'],['4','5','6'],['7','8','_']]

def Run(start,goal):
    
    mainRun=tkinter.Toplevel()
    mainRun.title("Run")
    mainRun.geometry("700x250")
    mainRun.configure(bg="#FFDAB9")


    # KHUNG START
    # 0,0
    gia_lb1 = Label(mainRun,width=2,bg="#FFDAB9")
    gia_lb1.grid(column=2, row=1)

    mainRunlb1 = Label(mainRun,width=5)
    mainRunlb1.grid(column=1, row=1)
    # gia dong
    gia_row00=Label(mainRun,width=5,bg="#FFDAB9")
    gia_row00.grid(column=1, row=2)



    #0,1
    gia_lb2 = Label(mainRun,width=2,bg="#FFDAB9")
    gia_lb2.grid(column=4, row=1)

    mainRunlb2 = Label(mainRun,width=5)
    mainRunlb2.grid(column=3, row=1)



    #02
    gia_lb3 = Label(mainRun,width=10,bg="#FFDAB9")
    gia_lb3.grid(column=6, row=1)

    mainRunlb3 = Label(mainRun,width=5)
    mainRunlb3.grid(column=5, row=1)





    mainRunlb4 = Label(mainRun,width=5)
    mainRunlb4.grid(column=1, row=3)
    # gia dong
    gia_row13=Label(mainRun,width=5,bg="#FFDAB9")
    gia_row13.grid(column=3, row=4)



    mainRunlb5 = Label(mainRun,width=5)
    mainRunlb5.grid(column=3, row=3)


    mainRunlb6 = Label(mainRun,width=5)
    mainRunlb6.grid(column=5, row=3)


    mainRunlb7 = Label(mainRun,width=5)
    mainRunlb7.grid(column=1, row=5)
    # gia dong
    gia_row15=Label(mainRun,width=5,bg="#FFDAB9")
    gia_row15.grid(column=3, row=6)



    mainRunlb8 = Label(mainRun,width=5)
    mainRunlb8.grid(column=3, row=5)

    mainRunlb9 = Label(mainRun,width=5)
    mainRunlb9.grid(column=5, row=5)


    # KHUNG GOAL
    # 00
    mainRunlb1_goal = Label(mainRun,width=5)
    mainRunlb1_goal.grid(column=7, row=1)
    # gia dong
    gia_row17=Label(mainRun,width=5,bg="#FFDAB9")
    gia_row17.grid(column=7, row=2)

    gia_lb1_goal = Label(mainRun,width=2,bg="#FFDAB9")
    gia_lb1_goal.grid(column=8, row=1)




    mainRunlb2_goal = Label(mainRun,width=5)
    mainRunlb2_goal.grid(column=9, row=1)
    gia_lb2_goal = Label(mainRun,width=2,bg="#FFDAB9")
    gia_lb2_goal.grid(column=10, row=1)


    # 02
    mainRunlb3_goal = Label(mainRun,width=5)
    mainRunlb3_goal.grid(column=11, row=1)
    gia_lb3_goal = Label(mainRun,width=2,bg="#FFDAB9")
    gia_lb3_goal.grid(column=12, row=1)

    #10
    mainRunlb4_goal = Label(mainRun,width=5)
    mainRunlb4_goal.grid(column=7, row=3)
    # gia dong
    gia_row19=Label(mainRun,width=5,bg="#FFDAB9")
    gia_row19.grid(column=7, row=4)

    #11
    mainRunlb5_goal = Label(mainRun,width=5)
    mainRunlb5_goal.grid(column=9, row=3)

    #12
    mainRunlb6_goal = Label(mainRun,width=5)
    mainRunlb6_goal.grid(column=11, row=3)

    #20
    mainRunlb7_goal = Label(mainRun,width=5)
    mainRunlb7_goal.grid(column=7, row=5)
    # gia dong
    gia_row21=Label(mainRun,width=5,bg="#FFDAB9")
    gia_row21.grid(column=7, row=6)

    #21
    mainRunlb8_goal = Label(mainRun,width=5)
    mainRunlb8_goal.grid(column=9, row=5)

    #22
    mainRunlb9_goal = Label(mainRun,width=5)
    mainRunlb9_goal.grid(column=11, row=5)



    #==================================================
    def XuatRaStart(start):
        mainRunlb1.configure(text= start[0][0])
        mainRunlb2.configure(text= start[0][1])
        mainRunlb3.configure(text= start[0][2])
        mainRunlb4.configure(text= start[1][0])
        mainRunlb5.configure(text= start[1][1])
        mainRunlb6.configure(text= start[1][2])
        mainRunlb7.configure(text= start[2][0])
        mainRunlb8.configure(text= start[2][1])
        mainRunlb9.configure(text= start[2][2])
    #==================================================
    def XuatRaGoal(goal):
        mainRunlb1_goal.configure(text= goal[0][0])
        mainRunlb2_goal.configure(text= goal[0][1])
        mainRunlb3_goal.configure(text= goal[0][2])
        mainRunlb4_goal.configure(text= goal[1][0])
        mainRunlb5_goal.configure(text= goal[1][1])
        mainRunlb6_goal.configure(text= goal[1][2])
        mainRunlb7_goal.configure(text= goal[2][0])
        mainRunlb8_goal.configure(text= goal[2][1])
        mainRunlb9_goal.configure(text= goal[2][2])
    #==================================================
    def BatDau():
        class Node:
            def __init__(self,data,level,fval):
                """ Kh???i t???o n??t v???i d??? li???u, m???c c???a n??t v?? gi?? tr??? ???????c t??nh to??n """
                self.data = data
                self.level = level
                self.fval = fval

            def generate_child(self):
                """ T???o c??c n??t con t??? n??t ???? cho b???ng c??ch di chuy???n kho???ng tr???ng
                    theo b???n h?????ng {l??n, xu???ng, tr??i, ph???i} """
                x,y = self.find(self.data,'_')
                """ val_list ch???a c??c gi?? tr??? v??? tr?? ????? di chuy???n kho???ng tr???ng ??? m???t trong hai
                    4 h?????ng [l??n, xu???ng, tr??i, ph???i] t????ng ???ng. """
                val_list = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]
                children = []
                for i in val_list:
                    child = self.shuffle(self.data,x,y,i[0],i[1])
                    if child is not None:
                        child_node = Node(child,self.level+1,0)
                        children.append(child_node)
                return children
                
            def shuffle(self,puz,x1,y1,x2,y2):
                """ Di chuy???n kho???ng tr???ng theo h?????ng ???? cho v?? n???u gi?? tr??? v??? tr?? n???m ngo??i
                    gi???i h???n tr??? l???i Kh??ng c?? """
                if x2 >= 0 and x2 < len(self.data) and y2 >= 0 and y2 < len(self.data):
                    temp_puz = []
                    temp_puz = self.copy(puz)
                    temp = temp_puz[x2][y2]
                    temp_puz[x2][y2] = temp_puz[x1][y1]
                    temp_puz[x1][y1] = temp
                    return temp_puz
                else:
                    return None
                    

            def copy(self,root):
                """ Sao ch??p h??m ????? t???o m???t ma tr???n t????ng t??? c???a n??t ???? cho"""
                temp = []
                for i in root:
                    t = []
                    for j in i:
                        t.append(j)
                    temp.append(t)
                return temp    
                    
            def find(self,puz,x):
                """ ?????c bi???t ???????c s??? d???ng ????? t??m v??? tr?? c???a kho???ng tr???ng """
                for i in range(0,len(self.data)):
                    for j in range(0,len(self.data)):
                        if puz[i][j] == x:
                            return i,j


        class Puzzle:
            def __init__(self,size):
                """ Kh???i t???o k??ch th?????c c??u ????? theo k??ch th?????c ???????c ch??? ?????nh, danh s??ch m??? v?? ????ng th??nh tr???ng"""
                self.n = size
                self.open = []
                self.closed = []

            def accept(self):
                """ Ch???p nh???n c??u ????? t??? ng?????i d??ng """
                puz = []
                for i in range(0,self.n):
                    temp = input().split(" ")
                    puz.append(temp)
                return puz
                



            def f(self,start,goal):
                """H??m Heuristic ????? t??nh to??n gi?? tr??? hueristic f (x) = h (x) + g (x)"""
                return self.h(start.data,goal)+start.level                                                                                                                                                                                                                                                                                                                                      

            def h(self,start,goal):
                """ T??nh to??n s??? kh??c bi???t gi???a c??c c??u ????? ???? cho """
                temp = 0
                for i in range(0,self.n):
                    for j in range(0,self.n):
                        if start[i][j] != goal[i][j] and start[i][j] != '_':
                            temp += 1
                return temp
                

            def process(self,start,goal):
                """ Ch???p nh???n tr???ng th??i C??u ????? b???t ?????u v?? M???c ti??u"""
                
                start = Node(start,0,0)
                start.fval = self.f(start,goal)
                """ Ch???p nh???n c??u ????? b???t ?????u tr???ng th??i v?? ti??u ?????"""
                self.open.append(start)
                
                while True:
                    cur = self.open[0]
                    XuatRaStart(cur.data)                    
                    mainRun.update()
                    time.sleep(2)
                    """ If the difference between current and goal node is 0 we have reached the goal node"""
                    if(self.h(cur.data,goal) == 0):
                        break
                    for i in cur.generate_child():
                        i.fval = self.f(i,goal)
                        self.open.append(i)
                    self.closed.append(cur)
                    del self.open[0]

                    """ sort the opne list based on f value """
                    self.open.sort(key = lambda x:x.fval,reverse=False)
        puz = Puzzle(3)
        puz.process(start,goal)
#==================================================
# # CODE 8 PUZZLE A*

    # LABEL
    var4=tkinter.StringVar()
    label_Run=tkinter.Label(mainRun, font=("Arial",10),textvariable=var4,pady=20,padx=20,bg="#FFDAB9")
    var4.set("***??ang ch???y..........***")
    label_Run.grid(row=0,column=0)
    XuatRaGoal(goal)
    
    BatDau()
    var4.set("***Th??nh C??ng***")
    mainRun.mainloop()
    
        

     
    

if __name__ == '__main__':  
    Run(start,goal)
    
    
