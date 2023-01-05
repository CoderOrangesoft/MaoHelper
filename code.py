import os;
import tkinter;

window = tkinter.Tk();
window.title("编程猫社区访问助手");
window.geometry("500x500");

def visitBtn_click():
    os.system("start" + " https://shequ.codemao.cn/work/" + visitInput.get());
def visitBtnF_click():
    os.system("start" + " https://player.codemao.cn/new/" + visitInput.get());
def humanBtn_click():
    os.system("start" + " https://shequ.codemao.cn/user/" + humanInput.get());

visitInput = tkinter.Label(window,text="访问一个作品的各种信息(输入作品ID)");
visitInput.pack();

visitInput = tkinter.Entry(window,text="在这里输入作品ID");
visitInput.pack();

visitBtn = tkinter.Button(window,text='点击访问该作品');
visitBtn.config(command=visitBtn_click);
visitBtn.pack();

visitBtnF = tkinter.Button(window,text='破解该作品的防沉迷');
visitBtnF.config(command=visitBtnF_click);
visitBtnF.pack();

br = tkinter.Label(window,text=" ")
br.pack()

humanInput = tkinter.Label(window,text="访问一个人的空间(输入社区ID)");
humanInput.pack();

humanInput = tkinter.Entry(window,text="在这里输入社区ID");
humanInput.pack();

humanBtn = tkinter.Button(window,text='点击访问该作品');
humanBtn.config(command=humanBtn_click);
humanBtn.pack();

window.mainloop();