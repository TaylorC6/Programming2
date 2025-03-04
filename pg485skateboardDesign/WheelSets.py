
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class WheelSets(Form):
    def __init__(self, parent):
        self.myparent = parent
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button5 = System.Windows.Forms.Button()
        self._label2 = System.Windows.Forms.Label()
        self._radioButton3 = System.Windows.Forms.RadioButton()
        self._radioButton2 = System.Windows.Forms.RadioButton()
        self._radioButton1 = System.Windows.Forms.RadioButton()
        self._label1 = System.Windows.Forms.Label()
        self._radioButton4 = System.Windows.Forms.RadioButton()
        self.SuspendLayout()
        # 
        # button5
        # 
        self._button5.BackColor = System.Drawing.Color.IndianRed
        self._button5.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._button5.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button5.Location = System.Drawing.Point(65, 444)
        self._button5.Name = "button5"
        self._button5.Size = System.Drawing.Size(450, 52)
        self._button5.TabIndex = 12
        self._button5.Text = "Skate Shop"
        self._button5.UseVisualStyleBackColor = False
        self._button5.Click += self.Button5Click
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Brown
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(5, 429)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(562, 83)
        self._label2.TabIndex = 11
        self._label2.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # radioButton3
        # 
        self._radioButton3.BackColor = System.Drawing.Color.IndianRed
        self._radioButton3.FlatStyle = System.Windows.Forms.FlatStyle.Popup
        self._radioButton3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton3.Location = System.Drawing.Point(65, 230)
        self._radioButton3.Name = "radioButton3"
        self._radioButton3.Size = System.Drawing.Size(450, 53)
        self._radioButton3.TabIndex = 20
        self._radioButton3.TabStop = True
        self._radioButton3.Text = "58 mm $24"
        self._radioButton3.UseVisualStyleBackColor = False
        self._radioButton3.CheckedChanged += self.RadioButton3CheckedChanged
        # 
        # radioButton2
        # 
        self._radioButton2.BackColor = System.Drawing.Color.IndianRed
        self._radioButton2.FlatStyle = System.Windows.Forms.FlatStyle.Popup
        self._radioButton2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton2.Location = System.Drawing.Point(65, 126)
        self._radioButton2.Name = "radioButton2"
        self._radioButton2.Size = System.Drawing.Size(450, 53)
        self._radioButton2.TabIndex = 19
        self._radioButton2.TabStop = True
        self._radioButton2.Text = "55 mm $22"
        self._radioButton2.UseVisualStyleBackColor = False
        self._radioButton2.CheckedChanged += self.RadioButton2CheckedChanged
        # 
        # radioButton1
        # 
        self._radioButton1.BackColor = System.Drawing.Color.IndianRed
        self._radioButton1.FlatStyle = System.Windows.Forms.FlatStyle.Popup
        self._radioButton1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton1.Location = System.Drawing.Point(65, 23)
        self._radioButton1.Name = "radioButton1"
        self._radioButton1.Size = System.Drawing.Size(450, 53)
        self._radioButton1.TabIndex = 18
        self._radioButton1.TabStop = True
        self._radioButton1.Text = "51 mm $20"
        self._radioButton1.UseVisualStyleBackColor = False
        self._radioButton1.CheckedChanged += self.RadioButton1CheckedChanged
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Brown
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(5, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(562, 389)
        self._label1.TabIndex = 17
        self._label1.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # radioButton4
        # 
        self._radioButton4.BackColor = System.Drawing.Color.IndianRed
        self._radioButton4.FlatStyle = System.Windows.Forms.FlatStyle.Popup
        self._radioButton4.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton4.Location = System.Drawing.Point(65, 333)
        self._radioButton4.Name = "radioButton4"
        self._radioButton4.Size = System.Drawing.Size(450, 53)
        self._radioButton4.TabIndex = 21
        self._radioButton4.TabStop = True
        self._radioButton4.Text = "61 mm $28"
        self._radioButton4.UseVisualStyleBackColor = False
        # 
        # WheelSets
        # 
        self.BackColor = System.Drawing.Color.Maroon
        self.ClientSize = System.Drawing.Size(573, 524)
        self.Controls.Add(self._radioButton4)
        self.Controls.Add(self._radioButton3)
        self.Controls.Add(self._radioButton2)
        self.Controls.Add(self._radioButton1)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button5)
        self.Controls.Add(self._label2)
        self.Name = "WheelSets"
        self.Text = "WheelSets"
        self.ResumeLayout(False)


    def Button5Click(self, sender, e):
        self.myparent.Show()
        self.Hide()
        




    def RadioButton1CheckedChanged(self, sender, e):
        pass