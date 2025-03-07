
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form1(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._radioButton1 = System.Windows.Forms.RadioButton()
        self._radioButton2 = System.Windows.Forms.RadioButton()
        self._radioButton3 = System.Windows.Forms.RadioButton()
        self._radioButton4 = System.Windows.Forms.RadioButton()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.DarkSlateBlue
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.White
        self._label1.Location = System.Drawing.Point(12, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(481, 214)
        self._label1.TabIndex = 24
        self._label1.Text = "Dorm and Meal Plan Calculator"
        self._label1.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # radioButton1
        # 
        self._radioButton1.BackColor = System.Drawing.Color.RoyalBlue
        self._radioButton1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton1.ForeColor = System.Drawing.Color.White
        self._radioButton1.Location = System.Drawing.Point(71, 44)
        self._radioButton1.Name = "radioButton1"
        self._radioButton1.RightToLeft = System.Windows.Forms.RightToLeft.No
        self._radioButton1.Size = System.Drawing.Size(369, 33)
        self._radioButton1.TabIndex = 25
        self._radioButton1.Text = "Allen Hall $1,500 per semester"
        self._radioButton1.UseVisualStyleBackColor = False
        self._radioButton1.CheckedChanged += self.RadioButton1CheckedChanged
        # 
        # radioButton2
        # 
        self._radioButton2.BackColor = System.Drawing.Color.RoyalBlue
        self._radioButton2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton2.ForeColor = System.Drawing.Color.White
        self._radioButton2.Location = System.Drawing.Point(71, 83)
        self._radioButton2.Name = "radioButton2"
        self._radioButton2.RightToLeft = System.Windows.Forms.RightToLeft.No
        self._radioButton2.Size = System.Drawing.Size(369, 33)
        self._radioButton2.TabIndex = 26
        self._radioButton2.Text = "Pike Hall $1,600 per semester"
        self._radioButton2.UseVisualStyleBackColor = False
        self._radioButton2.CheckedChanged += self.RadioButton2CheckedChanged
        # 
        # radioButton3
        # 
        self._radioButton3.BackColor = System.Drawing.Color.RoyalBlue
        self._radioButton3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton3.ForeColor = System.Drawing.Color.White
        self._radioButton3.Location = System.Drawing.Point(71, 122)
        self._radioButton3.Name = "radioButton3"
        self._radioButton3.RightToLeft = System.Windows.Forms.RightToLeft.No
        self._radioButton3.Size = System.Drawing.Size(369, 33)
        self._radioButton3.TabIndex = 27
        self._radioButton3.Text = "Farthing Hall $1,200 per semester"
        self._radioButton3.UseVisualStyleBackColor = False
        self._radioButton3.CheckedChanged += self.RadioButton3CheckedChanged
        # 
        # radioButton4
        # 
        self._radioButton4.BackColor = System.Drawing.Color.RoyalBlue
        self._radioButton4.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton4.ForeColor = System.Drawing.Color.White
        self._radioButton4.Location = System.Drawing.Point(71, 161)
        self._radioButton4.Name = "radioButton4"
        self._radioButton4.RightToLeft = System.Windows.Forms.RightToLeft.No
        self._radioButton4.Size = System.Drawing.Size(369, 33)
        self._radioButton4.TabIndex = 28
        self._radioButton4.Text = "University Suites $1,800 per semester"
        self._radioButton4.UseVisualStyleBackColor = False
        self._radioButton4.CheckedChanged += self.RadioButton4CheckedChanged
        # 
        # Form1
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaption
        self.ClientSize = System.Drawing.Size(503, 236)
        self.Controls.Add(self._radioButton4)
        self.Controls.Add(self._radioButton3)
        self.Controls.Add(self._radioButton2)
        self.Controls.Add(self._radioButton1)
        self.Controls.Add(self._label1)
        self.Name = "Form1"
        self.Text = "Form1"
        self.ResumeLayout(False)


    def RadioButton1CheckedChanged(self, sender, e):
        self.myparent.price += 1500
        
    def RadioButton2CheckedChanged(self, sender, e):
        self.myparent.price += 1600

    def RadioButton3CheckedChanged(self, sender, e):
        self.myparent.price += 1200

    def RadioButton4CheckedChanged(self, sender, e):
        self.myparent.price += 1800