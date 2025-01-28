import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._button4 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Green
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 48, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.Aquamarine
        self._label1.Location = System.Drawing.Point(207, 137)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(591, 170)
        self._label1.TabIndex = 0
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.PaleGreen
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(76, 439)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(225, 83)
        self._button1.TabIndex = 1
        self._button1.Text = "Show"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.PaleGreen
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(399, 439)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(225, 83)
        self._button2.TabIndex = 2
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.PaleGreen
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(725, 439)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(225, 83)
        self._button3.TabIndex = 3
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # button4
        # 
        self._button4.BackColor = System.Drawing.Color.MediumSeaGreen
        self._button4.FlatStyle = System.Windows.Forms.FlatStyle.Popup
        self._button4.Location = System.Drawing.Point(954, 595)
        self._button4.Name = "button4"
        self._button4.Size = System.Drawing.Size(33, 28)
        self._button4.TabIndex = 4
        self._button4.Text = "No."
        self._button4.UseVisualStyleBackColor = False
        self._button4.UseWaitCursor = True
        self._button4.Click += self.Button4Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.MediumSeaGreen
        self.ClientSize = System.Drawing.Size(989, 625)
        self.Controls.Add(self._button4)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Hello"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self._label1.Text = "Hello World!"
        

    def Button2Click(self, sender, e):
        self._label1.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()

    def Button4Click(self, sender, e):
        self._label1.Text = "Goodbye World!"