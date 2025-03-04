
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form1(Form):
    def __init__(self, parent):
        self.myparent = parent
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button5 = System.Windows.Forms.Button()
        self._label2 = System.Windows.Forms.Label()
        self._label1 = System.Windows.Forms.Label()
        self._radioButton1 = System.Windows.Forms.RadioButton()
        self._radioButton2 = System.Windows.Forms.RadioButton()
        self._radioButton3 = System.Windows.Forms.RadioButton()
        self.SuspendLayout()
        # 
        # button5
        # 
        self._button5.BackColor = System.Drawing.Color.IndianRed
        self._button5.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._button5.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button5.Location = System.Drawing.Point(72, 450)
        self._button5.Name = "button5"
        self._button5.Size = System.Drawing.Size(450, 52)
        self._button5.TabIndex = 8
        self._button5.Text = "Skate Shop"
        self._button5.UseVisualStyleBackColor = False
        self._button5.Click += self.Button5Click
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Brown
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(12, 435)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(562, 83)
        self._label2.TabIndex = 7
        self._label2.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Brown
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(562, 389)
        self._label1.TabIndex = 9
        self._label1.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # radioButton1
        # 
        self._radioButton1.BackColor = System.Drawing.Color.IndianRed
        self._radioButton1.FlatStyle = System.Windows.Forms.FlatStyle.Popup
        self._radioButton1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton1.Location = System.Drawing.Point(72, 57)
        self._radioButton1.Name = "radioButton1"
        self._radioButton1.Size = System.Drawing.Size(450, 53)
        self._radioButton1.TabIndex = 10
        self._radioButton1.TabStop = True
        self._radioButton1.Text = "The Master Thrasher $60"
        self._radioButton1.UseVisualStyleBackColor = False
        # 
        # radioButton2
        # 
        self._radioButton2.BackColor = System.Drawing.Color.IndianRed
        self._radioButton2.FlatStyle = System.Windows.Forms.FlatStyle.Popup
        self._radioButton2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton2.Location = System.Drawing.Point(72, 160)
        self._radioButton2.Name = "radioButton2"
        self._radioButton2.Size = System.Drawing.Size(450, 53)
        self._radioButton2.TabIndex = 11
        self._radioButton2.TabStop = True
        self._radioButton2.Text = "The Dictator of Grind $45"
        self._radioButton2.UseVisualStyleBackColor = False
        # 
        # radioButton3
        # 
        self._radioButton3.BackColor = System.Drawing.Color.IndianRed
        self._radioButton3.FlatStyle = System.Windows.Forms.FlatStyle.Popup
        self._radioButton3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton3.Location = System.Drawing.Point(72, 264)
        self._radioButton3.Name = "radioButton3"
        self._radioButton3.Size = System.Drawing.Size(450, 53)
        self._radioButton3.TabIndex = 12
        self._radioButton3.TabStop = True
        self._radioButton3.Text = "The Street King $50"
        self._radioButton3.UseVisualStyleBackColor = False
        # 
        # Form1
        # 
        self.BackColor = System.Drawing.Color.Maroon
        self.ClientSize = System.Drawing.Size(584, 527)
        self.Controls.Add(self._radioButton3)
        self.Controls.Add(self._radioButton2)
        self.Controls.Add(self._radioButton1)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button5)
        self.Controls.Add(self._label2)
        self.Name = "Form1"
        self.Text = "Form1"
        self.ResumeLayout(False)


    def Button5Click(self, sender, e):
        self.myparent.Show()
        self.Hide()
        if self._radioButton1.Checked:
            self.myparent.price += 60
        if self._radioButton2.Checked:
            self.myparent.price += 45
        if self._radioButton3.Checked:
            self.myparent.price += 50
        else:
            pass
        

