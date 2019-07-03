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
        # Tab 컨트롤
        tabControl = ttk.Notebook(self.root)

        self._AddTab1(tabControl)
        tabControl.pack()

    def _AddTab1(self,tabControl):
        tab1 = ttk.Frame(tabControl)
        tabControl.add(tab1,text = 'tab1')

        #Frame 컨트롤
        mighty = ttk.LabelFrame(tab1,text='mighty')
        mighty.grid(row=0,column=0)#padx = 200,pady = 200

        #메시지
        tk.Label(mighty,text='평균입력').grid(row=0,column = 0)
        tk.Label(mighty, text='표준편차입력').grid(row=0, column=1)
        #tk.Label(self.mighty, text='적용').grid(row=0, column=2)

        #text Box 평균 받기
        self.tmpMean = tk.StringVar()
        self.txtMean = ttk.Entry(mighty,textvariable=self.tmpMean)
        self.txtMean.grid(row  = 1, column = 0)
        #text Box 표준편차 받기
        self.tmpStd = tk.StringVar()
        self.txtStd = ttk.Entry(mighty,textvariable=self.tmpStd)
        self.txtStd.grid(row  = 1, column = 1)

        def _buttonAction():
            mean = self.tmpMean.get()
            std = self.tmpMean.get()
            txt = '입력값! >> \n평균 : {m}\n표준편차 : {s}'.format(m=mean,s=std)
            self.tmpInput.set(txt)


        #button 적용
        self.btApply = tk.Button(mighty,text='적용!!',command = _buttonAction)
        self.btApply.grid(row=1,column=2)


        #Combo Box
        #self.tmpStd = tk.IntVar()
        #self.

        #Label
        self.tmpInput = tk.StringVar()
        self.tmpInput.set('입력값 >>')
        self.inputLabel = tk.Label(mighty,textvariable=self.tmpInput)
        self.inputLabel.grid(column = 0,row = 2,columnspan = 3)


        #그림영역 확보
        self.picture = ttk.LabelFrame(tab1,text='picture')
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
