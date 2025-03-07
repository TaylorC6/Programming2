import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.price = 0
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button3 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._label12 = System.Windows.Forms.Label()
        self._label11 = System.Windows.Forms.Label()
        self._label1 = System.Windows.Forms.Label()
        self._label10 = System.Windows.Forms.Label()
        self._button4 = System.Windows.Forms.Button()
        self._button5 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.DarkSlateBlue
        self._button3.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.Color.White
        self._button3.Location = System.Drawing.Point(259, 288)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(125, 47)
        self._button3.TabIndex = 29
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.DarkSlateBlue
        self._button2.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.Color.White
        self._button2.Location = System.Drawing.Point(112, 288)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(125, 47)
        self._button2.TabIndex = 28
        self._button2.Text = "Reset"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # label12
        # 
        self._label12.BackColor = System.Drawing.Color.DodgerBlue
        self._label12.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label12.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label12.ForeColor = System.Drawing.Color.White
        self._label12.Location = System.Drawing.Point(349, 233)
        self._label12.Name = "label12"
        self._label12.Size = System.Drawing.Size(122, 28)
        self._label12.TabIndex = 26
        # 
        # label11
        # 
        self._label11.BackColor = System.Drawing.Color.RoyalBlue
        self._label11.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label11.ForeColor = System.Drawing.Color.White
        self._label11.Location = System.Drawing.Point(231, 233)
        self._label11.Name = "label11"
        self._label11.Size = System.Drawing.Size(122, 28)
        self._label11.TabIndex = 25
        self._label11.Text = "Total Cost:"
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
        self._label1.TabIndex = 23
        self._label1.Text = "Dorm and Meal Plan Calculator"
        self._label1.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # label10
        # 
        self._label10.BackColor = System.Drawing.Color.DarkSlateBlue
        self._label10.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label10.ForeColor = System.Drawing.Color.White
        self._label10.Location = System.Drawing.Point(12, 223)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(481, 49)
        self._label10.TabIndex = 24
        self._label10.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # button4
        # 
        self._button4.BackColor = System.Drawing.Color.RoyalBlue
        self._button4.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button4.Location = System.Drawing.Point(35, 59)
        self._button4.Name = "button4"
        self._button4.Size = System.Drawing.Size(202, 128)
        self._button4.TabIndex = 30
        self._button4.Text = "Dormatories"
        self._button4.UseVisualStyleBackColor = False
        self._button4.Click += self.Button4Click
        # 
        # button5
        # 
        self._button5.BackColor = System.Drawing.Color.RoyalBlue
        self._button5.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button5.Location = System.Drawing.Point(259, 59)
        self._button5.Name = "button5"
        self._button5.Size = System.Drawing.Size(202, 128)
        self._button5.TabIndex = 31
        self._button5.Text = "Meal Plans"
        self._button5.UseVisualStyleBackColor = False
        self._button5.Click += self.Button5Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaption
        self.ClientSize = System.Drawing.Size(504, 352)
        self.Controls.Add(self._button5)
        self.Controls.Add(self._button4)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._label12)
        self.Controls.Add(self._label11)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._label10)
        self.Name = "MainForm"
        self.Text = "pg848DormAndMealPlans"
        self.ResumeLayout(False)


    def Button4Click(self, sender, e):
        from Form1 import *
        Form1 = Form1(self)
        Form1.Show()
        self.Hide()

    def Button5Click(self, sender, e):
        from Form2 import *
        Form2 = Form2(self)
        Form2.Show()
        self.Hide()

    def Button2Click(self, sender, e):
        self._label12.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()