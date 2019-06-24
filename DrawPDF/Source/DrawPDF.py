import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class DrawPDF():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Draw PDF Graph')

        self._ConstructWidgets()
    def _ConstructWidgets(self):
        #Tab 컨트롤
        self.tabControl = ttk.Notebook(self.root)

        self.tab1 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab1,text = 'tab1')

        self.tabControl.pack()

        #------------
        # Tab1
        #------------

        #Frame 컨트롤
        self.mighty = ttk.LabelFrame(self.tab1,text='mighty')
        self.mighty.grid(row=0,column=0)#padx = 200,pady = 200

        #메시지
        tk.Label(self.mighty,text='평균입력').grid(row=0,column = 0)
        tk.Label(self.mighty, text='표준편차입력').grid(row=0, column=1)
        tk.Label(self.mighty, text='적용').grid(row=0, column=2)

        #text Box 평균 받기
        self.tmpMean = tk.StringVar()
        self.txtMean = ttk.Entry(self.mighty,textvariable=self.tmpMean)
        self.txtMean.grid(row  = 1, column = 0)
        #text Box 표준편차 받기
        self.tmpStd = tk.StringVar()
        self.txtStd = ttk.Entry(self.mighty,textvariable=self.tmpStd)
        self.txtStd.grid(row  = 1, column = 1)

        #button 적용
        self.btApply = tk.Button(self.mighty,text='적용!!')
        self.btApply.grid(row=1,column=2)
        #Combo Box
        #self.tmpStd = tk.IntVar()
        #self.

        #Label
        self.tmpInput = tk.StringVar()
        self.tmpInput.set('결과값은:')
        self.inputLabel = tk.Label(self.mighty,textvariable=self.tmpInput)
        self.inputLabel.grid(column = 0,row = 2,columnspan = 3)


        #그림영역 확보
        self.picture = ttk.LabelFrame(self.tab1,text='picture')
        self.picture.grid(row=1,column =0, padx = 5, pady = 5)
        #Canvas
        '''
        self.fig = Figure(figsize=[5,5])
        root.withdraw()
        root.protocol('WM_DELETE_WINDOW', _destroyWin)

        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        '''
if __name__ =='__main__':
    gui = DrawPDF()
    gui.root.mainloop()
