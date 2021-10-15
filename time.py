def pop_up_box():
    """
    使用tkinter弹出输入框输入数字, 具有确定输入和清除功能, 可在函数内直接调用num(文本框的值)使用
    """

    import tkinter
    import time
    
    def inputint():
        nonlocal timeStamp
        try:
            timeStamp = int(var.get().strip())
            timeArray = time.localtime(timeStamp)
            otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
            theLabel = tkinter.Label(root,text=otherStyleTime)
            theLabel.grid(row =2 ,column =0,sticky =tkinter.E)
        except:
            timeStamp = '非法时间戳'
            theLabel = tkinter.Label(root,text=timeStamp)
            theLabel.grid(row =2 ,column =0)


    def inputclear():
        nonlocal timeStamp
        var.set('')
        timeStamp = ''

    timeStamp = 0
    root = tkinter.Tk(className='unix时间戳转换')  # 弹出框框名
    root.geometry('400x200')     # 设置弹出框的大小 w x h

    var = tkinter.StringVar()   # 这即是输入框中的内容
    tkinter.Label(root,text="请输入时间戳：").grid(row = 0,column =0,sticky =tkinter.E)
    #var.set('Content of var') # 通过var.get()/var.set() 来 获取/设置var的值
    entry1 = tkinter.Entry(root, textvariable=var)  # 设置"文本变量"为var
    entry1.grid(row =0 ,column =1,sticky =tkinter.W)   # 将entry"打上去"
    btn1 = tkinter.Button(root, text='转换', command=inputint)     # 按下此按钮(Input), 触发inputint函数
    btn2 = tkinter.Button(root, text='清空', command=inputclear)   # 按下此按钮(Clear), 触发inputclear函数
    # 按钮定位
    btn1.grid(row =3 ,column =0,sticky =tkinter.E, padx=40,pady =10)
    btn2.grid(row =3 ,column =1,sticky =tkinter.W, padx=40,pady =10)
   

    # 上述完成之后, 开始真正弹出弹出框
    root.mainloop()

pop_up_box()