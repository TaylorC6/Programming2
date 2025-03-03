
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form2(Form):
    def __init__(self, parent):
        myparent = parent
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button3 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button1 = System.Windows.Forms.Button()
        self._label2 = System.Windows.Forms.Label()
        self._label1 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.SystemColors.MenuHighlight
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(340, 309)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(168, 70)
        self._button3.TabIndex = 25
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.SystemColors.MenuHighlight
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(340, 180)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(168, 70)
        self._button2.TabIndex = 24
        self._button2.Text = "Student"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.SystemColors.MenuHighlight
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(340, 56)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(168, 70)
        self._button1.TabIndex = 23
        self._button1.Text = "General"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.MenuHighlight
        self._label2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(12, 169)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(297, 93)
        self._label2.TabIndex = 20
        self._label2.Text = "Select Student Sales for all student ticket sales."
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.MenuHighlight
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 46)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(297, 95)
        self._label1.TabIndex = 19
        self._label1.Text = "Select General Sales for all ticket sales to the general public."
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.SystemColors.MenuHighlight
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(340, 9)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(168, 33)
        self._label3.TabIndex = 26
        self._label3.Text = "Sales"
        self._label3.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # Form2
        # 
        self.BackColor = System.Drawing.Color.CadetBlue
        self.ClientSize = System.Drawing.Size(520, 391)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "Form2"
        self.Text = "Form2"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self.myparent.Show()

    def Button2Click(self, sender, e):
        from Form1 import *

    def Button3Click(self, sender, e):
        Application.Exit()