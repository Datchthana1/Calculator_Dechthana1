def FnameAndLname():
    First_Name = "Dechthana "
    Last_Name = "Arunchaiya "
    Student_ID = "65112948"
    print(First_Name ,Last_Name,Student_ID)
def UserName():
    Uname = str(input("ชื่อผู้ใช้คือ : "))
    UID = int(input("รหัสประจำตัวผู้ใช้ : "))
    print(Uname,UID)
import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_381=tk.Button(root)
        GButton_381["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=18)
        GButton_381["font"] = ft
        GButton_381["fg"] = "#000000"
        GButton_381["justify"] = "center"
        GButton_381["text"] = "1"
        GButton_381.place(x=100,y=350,width=100,height=100)
        GButton_381["command"] = self.GButton_1_command

        GButton_479=tk.Button(root)
        GButton_479["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=18)
        GButton_479["font"] = ft
        GButton_479["fg"] = "#000000"
        GButton_479["justify"] = "center"
        GButton_479["text"] = "2"
        GButton_479.place(x=200,y=350,width=100,height=100)
        GButton_479["command"] = self.GButton_2_command

        GButton_130=tk.Button(root)
        GButton_130["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=18)
        GButton_130["font"] = ft
        GButton_130["fg"] = "#000000"
        GButton_130["justify"] = "center"
        GButton_130["text"] = "3"
        GButton_130.place(x=300,y=350,width=100,height=100)
        GButton_130["command"] = self.GButton_3_command

        GButton_258=tk.Button(root)
        GButton_258["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=18)
        GButton_258["font"] = ft
        GButton_258["fg"] = "#000000"
        GButton_258["justify"] = "center"
        GButton_258["text"] = "4"
        GButton_258.place(x=100,y=250,width=100,height=100)
        GButton_258["command"] = self.GButton_4_command

        GButton_542=tk.Button(root)
        GButton_542["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=22)
        GButton_542["font"] = ft
        GButton_542["fg"] = "#000000"
        GButton_542["justify"] = "center"
        GButton_542["text"] = "5"
        GButton_542.place(x=200,y=250,width=100,height=100)
        GButton_542["command"] = self.GButton_5_command

        GButton_848=tk.Button(root)
        GButton_848["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=22)
        GButton_848["font"] = ft
        GButton_848["fg"] = "#000000"
        GButton_848["justify"] = "center"
        GButton_848["text"] = "6"
        GButton_848.place(x=300,y=250,width=100,height=100)
        GButton_848["command"] = self.GButton_6_command

        GButton_776=tk.Button(root)
        GButton_776["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=22)
        GButton_776["font"] = ft
        GButton_776["fg"] = "#000000"
        GButton_776["justify"] = "center"
        GButton_776["text"] = "7"
        GButton_776.place(x=100,y=150,width=100,height=100)
        GButton_776["command"] = self.GButton_7_command

        GButton_296=tk.Button(root)
        GButton_296["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=22)
        GButton_296["font"] = ft
        GButton_296["fg"] = "#000000"
        GButton_296["justify"] = "center"
        GButton_296["text"] = "8"
        GButton_296.place(x=200,y=150,width=100,height=100)
        GButton_296["command"] = self.GButton_8_command

        GButton_829=tk.Button(root)
        GButton_829["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=22)
        GButton_829["font"] = ft
        GButton_829["fg"] = "#000000"
        GButton_829["justify"] = "center"
        GButton_829["text"] = "9"
        GButton_829.place(x=300,y=150,width=100,height=100)
        GButton_829["command"] = self.GButton_9_command

        GButton_180=tk.Button(root)
        GButton_180["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_180["font"] = ft
        GButton_180["fg"] = "#000000"
        GButton_180["justify"] = "center"
        GButton_180["text"] = "0"
        GButton_180.place(x=200,y=450,width=100,height=50)
        GButton_180["command"] = self.GButton_15_command

        GLabel_280=tk.Label(root)
        ft = tkFont.Font(family='Times',size=38)
        GLabel_280["font"] = ft
        GLabel_280["fg"] = "#333333"
        GLabel_280["justify"] = "center"
        GLabel_280["text"] = "Output"
        GLabel_280.place(x=100,y=100,width=300,height=50)

        GButton_651=tk.Button(root)
        GButton_651["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_651["font"] = ft
        GButton_651["fg"] = "#000000"
        GButton_651["justify"] = "center"
        GButton_651["text"] = "+"
        GButton_651.place(x=400,y=250,width=50,height=50)
        GButton_651["command"] = self.GButton_10_command

        GButton_127=tk.Button(root)
        GButton_127["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_127["font"] = ft
        GButton_127["fg"] = "#000000"
        GButton_127["justify"] = "center"
        GButton_127["text"] = "%"
        GButton_127.place(x=400,y=150,width=50,height=50)
        GButton_127["command"] = self.GButton_11_command

        GButton_610=tk.Button(root)
        GButton_610["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_610["font"] = ft
        GButton_610["fg"] = "#000000"
        GButton_610["justify"] = "center"
        GButton_610["text"] = "-"
        GButton_610.place(x=400,y=300,width=50,height=50)
        GButton_610["command"] = self.GButton_12_command

        GButton_778=tk.Button(root)
        GButton_778["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_778["font"] = ft
        GButton_778["fg"] = "#000000"
        GButton_778["justify"] = "center"
        GButton_778["text"] = "X"
        GButton_778.place(x=400,y=200,width=50,height=50)
        GButton_778["command"] = self.GButton_13_command

        GButton_180=tk.Button(root)
        GButton_180["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_180["font"] = ft
        GButton_180["fg"] = "#000000"
        GButton_180["justify"] = "center"
        GButton_180["text"] = "Enter"
        GButton_180.place(x=400,y=350,width=50,height=100)
        GButton_180["command"] = self.GButton_14_command

    def GButton_1_command(self):
        self.Number = 1
        return self.Number

    def GButton_2_command(self):
        self.Number = 2
        return self.Number

    def GButton_3_command(self):
        self.Number = 3
        return self.Number

    def GButton_4_command(self):
        self.Number = 4
        return self.Number1

    def GButton_5_command(self):
        self.Number = 5
        return self.Number

    def GButton_6_command(self):
        self.Number = 6
        return self.Number 

    def GButton_7_command(self):
        self.Number = 7
        return self.Number 

    def GButton_8_command(self):
        self.Number = 8
        return self.Number

    def GButton_9_command(self):
        self.Number = 9
        return self.Number

    def GButton_10_command(self):
        print("command")


    def GButton_11_command(self):
        print("command")


    def GButton_12_command(self):
        print("command")


    def GButton_13_command(self):
        print("command")


    def GButton_14_command(self):
        print("command")
    
    def GButton_15_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()


    