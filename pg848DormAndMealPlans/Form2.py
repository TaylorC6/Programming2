
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form2(Form):
    def __init__(self, parent):
        self.myparent = parent
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._radioButton3 = System.Windows.Forms.RadioButton()
        self._radioButton2 = System.Windows.Forms.RadioButton()
        self._radioButton1 = System.Windows.Forms.RadioButton()
        self._label1 = System.Windows.Forms.Label()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
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
        self._radioButton3.TabIndex = 32
        self._radioButton3.TabStop = True
        self._radioButton3.Text = "Unlimited meals              $1,500 per semester"
        self._radioButton3.UseVisualStyleBackColor = False
        self._radioButton3.CheckedChanged += self.RadioButton3CheckedChanged
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
        self._radioButton2.TabIndex = 31
        self._radioButton2.TabStop = True
        self._radioButton2.Text = "14 meals per week             $1,095 per semester"
        self._radioButton2.UseVisualStyleBackColor = False
        self._radioButton2.CheckedChanged += self.RadioButton2CheckedChanged
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
        self._radioButton1.TabIndex = 30
        self._radioButton1.TabStop = True
        self._radioButton1.Text = "7 meals per week                $ 560 per semester"
        self._radioButton1.UseVisualStyleBackColor = False
        self._radioButton1.CheckedChanged += self.RadioButton1CheckedChanged
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.DarkSlateBlue
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.White
        self._label1.Location = System.Drawing.Point(12, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(481, 168)
        self._label1.TabIndex = 29
        self._label1.Text = "Dorm and Meal Plan Calculator"
        self._label1.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.DarkSlateBlue
        self._button3.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.Color.White
        self._button3.Location = System.Drawing.Point(183, 180)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(125, 47)
        self._button3.TabIndex = 33
        self._button3.Text = "Calculator"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # Form2
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaption
        self.ClientSize = System.Drawing.Size(507, 232)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._radioButton3)
        self.Controls.Add(self._radioButton2)
        self.Controls.Add(self._radioButton1)
        self.Controls.Add(self._label1)
        self.Name = "Form2"
        self.Text = "Form2"
        self.ResumeLayout(False)


    def Button3Click(self, sender, e):
        self.myparent.Show()
        self.Hide()

    def RadioButton3CheckedChanged(self, sender, e):
        self.myparent.mealprice = 0
        self.myparent.mealprice += 1500
        self.myparent._label12.Text = str(self.myparent.mealprice + self.myparent.price)

    def RadioButton2CheckedChanged(self, sender, e):
        self.myparent.mealprice = 0
        self.myparent.mealprice += 1095
        self.myparent._label12.Text = str(self.myparent.mealprice + self.myparent.price)

    def RadioButton1CheckedChanged(self, sender, e):
        self.myparent.mealprice = 0
        self.myparent.mealprice += 560
        self.myparent._label12.Text = str(self.myparent.mealprice + self.myparent.price)