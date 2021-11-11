import tkinter  as tk
from tkinter import font
import tkinter.ttk as ttk
from sympy import *
import random

#シンボル定義
x = Symbol("x")
y = Symbol("y")
z = Symbol("z")
a = Symbol("a")
b = Symbol("b")
c = Symbol("c")

#問題定義
function_dic1 = {1:sin(x),2:cos(x),3:tan(x),4:exp(x),5:log(x)}
function_dic2 = {1:sin(2*x),2:cos(2*x),3:tan(2*x)}

def Basic_Question(Question_No,index1,index2,index3,Value1,Value2,Value3,Value4):
    if Question_No == 1:
        Integ = (1+x)**index1/x**index2
        ans = simplify(integrate(Integ))
        out_Integ = "∫"
        out_Val = "(1+x)^"+str(index1)+"/"+"x^"+str(index2)
    elif Question_No == 2:
        Integ = x**index1*(Value1*x+Value2)**index2
        ans = simplify(integrate(Integ))
        out_Integ = "∫"
        out_Val = "x^"+str(index1)+"("+str(Value1)+"x"+"+"+str(Value2)+")^"+str(index2)
    elif Question_No == 3:
        Integ = Value1*x**index1/(x**index2+Value2)**index3
        ans = simplify(integrate(Integ))
        out_Integ = "∫"
        out_Val = str(Value1)+"x^"+str(index1)+"/"+"(x"+str(index2)+"+"+str(Value2)+")^"+str(index3)
    elif Question_No == 4:
        Integ = x*(x-Value1)**index1
        ans = simplify(integrate(Integ))
        out_Integ =  "∫"
        out_Val = "x"+"(x-"+str(Value1)+")^"+str(index1)
    elif Question_No == 5:
        Integ = (Value1*x - Value2)*(Value3*x + Value4)**index1
        ans = simplify(integrate(Integ))
        out_Integ = "∫"
        out_Val = "("+str(Value1)+"x"+"-"+str(Value2)+")"+"("+str(Value3)+"x"+"+"+str(Value4)+")^"+str(index1)
    elif Question_No == 6:
        function_no = random.randint(1,5)
        funtcion_No = function_dic1[function_no]
        Integ = funtcion_No**index1
        ans = simplify(integrate(Integ))
        out_Integ = "∫"
        out_Val = str(funtcion_No)+"^"+str(index1)
    elif Question_No == 7:
        function_no = random.randint(1,5)
        function_no_2 = random.randint(1,5)
        function_No = function_dic1[function_no]
        function_No_2 = function_dic1[function_no_2]
        if  function_no == function_no_2:
            Integ = x*function_No**2
            ans = simplify(integrate(Integ))
            out_Integ = "∫"
            out_Val = "x"+str(function_No)+"^2"
        else:
            Integ = x*function_No*function_No_2**index1
            ans = simplify(integrate(Integ))
            out_Integ = "∫"
            out_Val = "x"+str(function_No)+str(function_No_2)+"^"+str(index1)
    elif Question_No == 8:
        function_no = random.randint(1,5)
        function_No = function_dic1[function_no]
        Integ = Value1+function_No**index1
        ans = simplify(integrate(Integ))
        out_Integ =  "∫"
        out_Val = str(Value1)+"+"+str(function_No)+"^"+str(index1)
    elif Question_No == 9:
        function_no = random.randint(1,3)
        function_No = function_dic2[function_no]
        Integ = Value1*function_No
        ans = simplify(integrate(Integ))
        out_Integ = "∫"
        out_Val = str(Value1)+str(function_No)
    else:
        function_no = random.randint(1,3)
        function_No = function_dic2[function_no]
        Integ = Value1+function_No**index1
        ans = ans = simplify(integrate(Integ))
        out_Integ = "∫"
        out_Val = str(Value1)+"+"+str(function_No)+"^"+str(index1)
    return ans,out_Val,out_Integ
        
def Standard_Question(Question_No,index1,index2,index3,Value1,Value2,Value3,Value4):


    if Question_No == 1:
        Integ = 1/sqrt(Value1+sqrt(x))
        ans = simplify(integrate(Integ))
        out_Integ = "∫"
        out_Val = "1/"+"√"+str(Value1)+"+"+"√x"
    elif Question_No == 2:
        Integ = x**index1*sqrt(x**index2+Value1)
        ans = simplify(integrate(Integ))
        out_Integ = "∫"
        out_Val  = "x^"+str(index1)+"√(x^"+str(index2)+"+"+str(Value1)+")"
    elif Question_No  == 3:
        Integ = x**index1+Value1*x**index2*x/x**index1+1
        ans = simplify(integrate(Integ))
        out_Val = "x^"+str(index1)+"+"+str(Value1)+"x^"+str(index2)+"x"+"/"+"x^"+str(index1)+"1"
    elif Question_No == 4:
        Integ = x+Value1/Value2*sqrt(x+Value1)
        ans = simplify(integrate(Integ))
        out_Integ = "∫"
        out_Val = "x"+"+"+str(Value1)+"/"+str(Value2)+"√(x+"+str(Value1)+")"
    elif Question_No == 5:
        Integ = Value1/exp(x)-exp(-x)
        ans = simplify(integrate(Integ))
        out_Integ = "∫"
        out_Val = str(Value1)+"/"+"e^x"+"-"+"e^-x"
    elif Question_No == 6:
        Integ = x**index1*log(x+1)
        ans = simplify(integrate(Integ))
        out_Integ = "∫"
        out_Val = "x^"+str(index1)+"log(x+1)"
    elif  Question_No == 7:
        Integ = log(x)/(x+Value1)**index1
        ans = simplify(integrate(Integ))
        out_Integ = "∫"
        out_Val = "log(x)/(x+"+str(Value1)+")^"+str(index1)
    elif Question_No ==  8:
        Integ = log(x+sqrt(x**index1+Value1))
        ans = simplify(integrate(Integ))
        out_Integ = "∫"
        out_Val = "log(x+√x^"+str(index1)+"+"+str(Value1)+")"
    elif Question_No == 9:
        Integ = (Value1*x/x**index1+1)*log(x**2+1)
        ans = simplify(integrate(Integ))
        out_Integ = "∫"
        out_Val= "("+str(Value1)+"x"+"/"+"x^"+str(index1)+"1)"+"log(x^2+1)"
    elif  Question_No == 10:
        Integ = sqrt(x)*exp(sqrt(x))
        ans = simplify(integrate(Integ))
        out_Integ = "∫"
        out_Val = "√x"+"e^"+"√x"
    return ans,out_Integ,out_Val

def Difficult_Question(Question_No):
    if Question_No == 1:
        Integ = 1/(x**3+1)
        ans = simplify(integrate(Integ,(x,0,1)))
        out_Integ = "∫"
        Range_min = "0"
        Range_max = "1" 
        out_Val = "1/(x^3+1)"
    elif  Question_No == 2:
        Integ = 1/sin(x)+cos(x)+1
        ans = simplify(integrate(Integ))
        out_Integ = "∫"
        out_Val = "1/sin(x)+cos(x)+1"
    elif Question_No == 3:
        Integ = sin(x)/sin(x)+cos(x)
        ans = simplify(integrate(Integ,(x,0,pi/2)))
        out_Integ = "∫"
        Range_min = "0"
        Range_max = "π/2"
        out_Val = "sin(x)/sin(x)+cos(x)"
    elif Question_No == 4:
        Integ = log(x**2+1)
        ans = simplify(integrate(Integ,(x,0,1)))
        out_Integ = "∫"
        Range_min = "0"
        Range_max = "1"
        out_Val = "log(x^2+1"
    elif Question_No == 5:
        Integ = (sqrt(x**2+1))/x
        ans = simplify(integrate(Integ))
        out_Integ = "∫"
        out_Val = "√x^2+1/x"
    elif Question_No == 6:
        Integ = x*exp(x)*sin(x)*cos(x)
        ans = simplify(integrate(Integ))
        out_Integ = "∫"
        out_Val = "xe^xsin(x)cos(x)"
    elif Question_No == 7:
        Integ = exp(-2*x)*sin(3*x)
        ans = simplify(integrate(Integ))
        out_Integ = "∫"
        out_Val = "e^-2xsin(3x)"
    elif Question_No == 8:
        Integ = 2*x+1/sqrt(x**2+4)
        ans = simplify(integrate(Integ,(x,0,2)))
        out_Integ = "∫"
        Range_min = "0"
        Range_max = "2"
        out_Val =  "2x+1/√x^2+4"
    elif Question_No == 9:
        Integ  = (x+1)*sqrt(1-2*x**2)
        ans = simplify(integrate(Integ,(x,0,1/2)))
        Range_min = "0"
        Range_max = "1/2"
        out_Integ = "∫"
        out_Val = "(x+1)√(1-2x^2)"
    elif Question_No == 10:
        Integ = (1/x**2)*log(sqrt(1+x**2))
        ans = simplify(integrate(Integ,(x,1,sqrt(3))))
        Range_min = "1"
        Range_max = "√3"
        out_Integ = "∫"
        out_Val = "1/x^2log(√1+x^2)"
    return ans,out_Integ,out_Val,Range_min,Range_max

#画面遷移関数
def change_window(window):
    window.tkraise()
#問題ページ作成関数
def question_label(frame_name,out_Integ):
    label_app = ttk.Label(frame_name,text="以下の問題を解きなさい")
    label2_app = ttk.Label(frame_name,text=out_Integ)
    Entry_app = ttk.Entry(frame_name,width=20)
    label_app.pack()
    label2_app.pack()
    Entry_app.place(x=200,y=400)

def frame_grid_config(frame):
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)


def frame_create(parent):
    Frame_name = ttk.Frame(parent)
    Frame_name.grid(row=0,column=0,sticky="nsew",pady=20)
    return Frame_name

def create_question(frame_name,ans,Out_Integ,Out_Val):
    label_1 = ttk.Label(frame_name,text="以下の問題を解いてください",font=("MSゴシック","50"))
    label_2 = ttk.Label(frame_name,text="回答を表示します")
    label_app = ttk.Label(frame_name,text=Out_Integ,font=("MSゴシック","80","bold"))
    label_app_2 =  ttk.Label(frame_name,text=Out_Val,font=("@ＭＳ Ｐ明朝","40"))
    Entry_app = ttk.Entry(frame_name,width=70)
    answer_button = ttk.Button(frame_name,text="回答",command=lambda:Answer_button(Entry_app,ans,label_2))
    label_1.pack()
    label_2.place(x=400,y=550)
    label_app.place(x=150,y=85)
    label_app_2.place(x=300,y=100)
    Entry_app.place(x=100,y=300)
    answer_button.place(x=200,y=400)
    print(ans)


def create_question_2(frame_name,ans,out_Integ,out_Val,Range_min,Range_max):
    label_1 = ttk.Label(frame_name,text="以下の問題を解いてください",font=("MSゴシック","50"))
    label_2 = ttk.Label(frame_name,text="回答を表示します")
    label_app = ttk.Label(frame_name,text=out_Integ,font=("MSゴシック","80","bold"))
    label_app_2 =  ttk.Label(frame_name,text=out_Val,font=("@ＭＳ Ｐ明朝","40"))
    label_app_2_min = ttk.Label(frame_name,text=Range_min,font=("@ＭＳ Ｐ明朝","30"))
    label_app_2_max = ttk.Label(frame_name,text=Range_max,font=("@ＭＳ Ｐ明朝","30"))
    Entry_app = ttk.Entry(frame_name,width=70)
    answer_button = ttk.Button(frame_name,text="回答",command=lambda:Answer_button(Entry_app,ans,label_2))
    over_answer_button = ttk.Button(frame_name,text="回答をみる",command=lambda:Over_Ansewer_button(ans,label_2))
    label_1.pack()
    label_2.place(x=350,y=550)
    label_app.place(x=140,y=85)
    label_app_2.place(x=300,y=100)
    label_app_2_max.place(x=180,y=90)
    label_app_2_min.place(x=180,y=150)
    Entry_app.place(x=100,y=300)
    answer_button.place(x=200,y=400)
    over_answer_button.place(x=200,y=500)
    print(ans)

answer_list = []
#回答ボタンの動き
def Answer_button(Entry_name,ans,label_name):
    Entry_ans = Entry_name.get()
    str_ans = str(ans)
    if str_ans == Entry_ans:
        label_name.configure(text="正解",font=("@ＭＳ Ｐ明朝","30"))
        answer_list.append = ([label_name,"正解"])

    else:
        label_name.configure(text="不正解",font=("@ＭＳ Ｐ明朝","30"))
        answer_list.append = ([label_name,"不正解"])
    

#回答を表示する
def Over_Ansewer_button(ans,label_name):
    str_ans = str(ans)
    label_name.configure(text=str_ans,font=("@ＭＳ Ｐ明朝","20"))

#ラベル作成
def label_create(frame_name,text_name):
    label_name = ttk.Label(frame_name,text=text_name)
    return label_name
#ボタン生成
def button_create(frame_name,text_name,button_name,change_window_name):
    button_frame = ttk.Button(frame_name,text=text_name,command=lambda:button_name(change_window_name))
    return button_frame
#ラベル配置
def label_placcement(label_name,x_coord,y_coord):
    label_name.place(x=x_coord,y=y_coord)
#ボタン配置
def button_placcement(button_name,x_coord,y_coord):
    button_name.place(x=x_coord,y=y_coord)
    


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x800")
    frame_home = frame_create(root)
    frame_app_1 = frame_create(root)
    frame_app_2 = frame_create(root)
    frame_app_3 = frame_create(root)
    frame_app_4 = frame_create(root)

    frame_grid_config(root)
    frame_grid_config(frame_app_1)
    frame_grid_config(frame_app_2)
    frame_grid_config(frame_app_3)
    frame_grid_config(frame_app_4)

    #ホームウィジェット作成
    label_1 = ttk.Label(frame_home,text="積分力向上",font=("MSゴシック","80","bold"))
    label_2 = ttk.Label(frame_home,text="⚠️x**は各数字の累乗を表します例：x**2は２の２乗",font=("Msゴシック","10","bold"))
    label_2_a = ttk.Label(frame_home,text="⚠️e^を回答する際はexp(x)としてください例：e^2xはexp(2*x)",font=("Msゴシック","10","bold"))
    label_2_b = ttk.Label(frame_home,text="⚠️√を表す際はsqrt()としてください例：√2xはsqrt(2*x)",font=("Msゴシック","10","bold"))
    label_2_c = ttk.Label(frame_home,text="⚠️+,-を入力する際は半角スペースを入れてください例：2x+4の際は2*x + 4",font=("Msゴシック","10","bold"))
    label_2_d = ttk.Label(frame_home,text="⚠️sinx,cosx,logxを入力する際は(x)としてください例：sin2xの際はsin(2*x)",font=("Msゴシック","10","bold"))
    label_2_e = ttk.Label(frame_home,text="⚠️分数を入力する際は()で囲み,分子/分母とします例：1+sinx+cosx/sinxの際は(1+sin(x)+cos(x))/sin(x)",font=("Msゴシック","10","bold"))
    label_3 = label_create(frame_home,"１：基本レベル")
    label_4 = label_create(frame_home,"２：標準レベル")
    label_5 = label_create(frame_home,"３：難問レベル")
    label_6 = label_create(frame_home,"６：弱点レベル")
    #ラベル配置
    label_1.place(x=240,y=50)
    label_2.place(x=200,y=150)
    label_2_a.place(x=200,y=170)
    label_2_b.place(x=200,y=190)
    label_2_c.place(x=200,y=210)
    label_2_d.place(x=200,y=230)
    label_2_e.place(x=200,y=250)
    label_placcement(label_3,330,300)
    label_placcement(label_4,330,380)
    label_placcement(label_5,330,460)
    label_placcement(label_6,330,540)

    #問題ページボタン作成
    button_1 = button_create(frame_home,"問題へ",change_window,frame_app_1)
    button_2 = button_create(frame_home,"問題へ",change_window,frame_app_2)
    button_3 = button_create(frame_home,"問題へ",change_window,frame_app_3)
    button_4 = button_create(frame_home,"問題へ",change_window,frame_app_4)


    #ボタン配置
    button_placcement(button_1,350,330)
    button_placcement(button_2,350,410)
    button_placcement(button_3,350,490)
    button_placcement(button_4,350,570)

    def create_app_1(parent):
        frames = []

        def back_home():
            frames[0].tkraise()
            frame_home.tkraise()

        for i,_ in enumerate(range(2),start=1):
            frame = frame_create(parent)
            frames.append(frame)
            Question_No = random.randint(1,10)
            index1 = random.randint(2,3)
            index2 = random.randint(2,3)
            index3 = random.randint(2,3)
            Value1 = random.randint(2,3)
            Value2 = random.randint(2,3)
            Value3 = random.randint(2,3)
            Value4 = random.randint(2,3)
            ans,Out_Val,Out_Integ = Basic_Question(Question_No,index1,index2,index3,Value1,Value2,Value3,Value4)
            create_question(frame,ans,Out_Integ,Out_Val)
            label = ttk.Label(frame,text=f"問題{i}")
            label.pack()

            home_button = ttk.Button(frame,text="ホームに戻る",command=back_home)
            home_button.place(x=400,y=400)

        for frame, next_frame in zip(frames,frames[1:]):
            next_button = ttk.Button(frame,text="次の問題へ",command=next_frame.tkraise)
            next_button.place(x=600,y=400)
        
        else:
            frame = frames[-1]

        frames[0].tkraise()

    def create_app_2(parent):
        frames = []

        def back_home():
            frames[0].tkraise()
            frame_home.tkraise()

        for i,_ in enumerate(range(2),start=1):
            frame = frame_create(parent)
            frames.append(frame)
            Question_No = random.randint(1,10)
            index1 = random.randint(2,3)
            index2 = random.randint(2,3)
            index3 = random.randint(2,4)
            Value1 = random.randint(2,3)
            Value2 = random.randint(2,3)
            Value3 = random.randint(2,3)
            Value4 = random.randint(2,3)
            ans,Out_Integ,Out_Val = Standard_Question(Question_No,index1,index2,index3,Value1,Value2,Value3,Value4)
            create_question(frame,ans,Out_Integ,Out_Val)
            label = ttk.Label(frame,text=f"問題{i}")
            label.pack()

            home_button = ttk.Button(frame,text="ホームに戻る",command=back_home)
            home_button.place(x=400,y=400)

        for frame, next_frame in zip(frames,frames[1:]):
            next_button = ttk.Button(frame,text="次の問題へ",command=next_frame.tkraise)
            next_button.place(x=600,y=400)
        
        else:
            frame = frames[-1]

        frames[0].tkraise()
    
    def create_app_3(parent):
        frames = []

        def back_home():
            frames[0].tkraise()
            frame_home.tkraise()

        for i,_ in enumerate(range(2),start=1):
            frame = frame_create(parent)
            frames.append(frame)
            Question_No = random.randint(1,10)
            ans,out_Integ,out_Val,Range_min,Range_max = Difficult_Question(Question_No)
            create_question_2(frame,ans,out_Integ,out_Val,Range_min,Range_max)
            label = ttk.Label(frame,text=f"問題{i}")
            label.pack()

            home_button = ttk.Button(frame,text="ホームに戻る",command=back_home)
            home_button.place(x=400,y=400)

        for frame, next_frame in zip(frames,frames[1:]):
            next_button = ttk.Button(frame,text="次の問題へ",command=next_frame.tkraise)
            next_button.place(x=600,y=400)
        
        else:
            frame = frames[-1]

        frames[0].tkraise()


    create_app_1(frame_app_1)
    create_app_2(frame_app_2)
    create_app_3(frame_app_3)


    frame_home.tkraise()
    root.mainloop()