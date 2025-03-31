import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._button4 = System.Windows.Forms.Button()
        self._button5 = System.Windows.Forms.Button()
        self._button6 = System.Windows.Forms.Button()
        self._button7 = System.Windows.Forms.Button()
        self._button8 = System.Windows.Forms.Button()
        self._button9 = System.Windows.Forms.Button()
        self._button10 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Silver
        self._button1.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(42, 83)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(191, 64)
        self._button1.TabIndex = 21
        self._button1.Text = "Mercury"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Yellow
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(179, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(133, 54)
        self._label1.TabIndex = 22
        self._label1.Text = "Planets"
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(255, 128, 0)
        self._button2.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(263, 83)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(191, 64)
        self._button2.TabIndex = 23
        self._button2.Text = "Venus"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(192, 0, 0)
        self._button3.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(263, 166)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(191, 64)
        self._button3.TabIndex = 25
        self._button3.Text = "Mars"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # button4
        # 
        self._button4.BackColor = System.Drawing.Color.FromArgb(0, 192, 0)
        self._button4.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._button4.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button4.Location = System.Drawing.Point(42, 166)
        self._button4.Name = "button4"
        self._button4.Size = System.Drawing.Size(191, 64)
        self._button4.TabIndex = 24
        self._button4.Text = "Earth"
        self._button4.UseVisualStyleBackColor = False
        self._button4.Click += self.Button4Click
        # 
        # button5
        # 
        self._button5.BackColor = System.Drawing.Color.RoyalBlue
        self._button5.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._button5.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button5.Location = System.Drawing.Point(263, 339)
        self._button5.Name = "button5"
        self._button5.Size = System.Drawing.Size(191, 64)
        self._button5.TabIndex = 29
        self._button5.Text = "Neptune"
        self._button5.UseVisualStyleBackColor = False
        self._button5.Click += self.Button5Click
        # 
        # button6
        # 
        self._button6.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
        self._button6.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._button6.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button6.Location = System.Drawing.Point(42, 339)
        self._button6.Name = "button6"
        self._button6.Size = System.Drawing.Size(191, 64)
        self._button6.TabIndex = 28
        self._button6.Text = "Uranus"
        self._button6.UseVisualStyleBackColor = False
        self._button6.Click += self.Button6Click
        # 
        # button7
        # 
        self._button7.BackColor = System.Drawing.Color.PaleGoldenrod
        self._button7.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._button7.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button7.Location = System.Drawing.Point(263, 250)
        self._button7.Name = "button7"
        self._button7.Size = System.Drawing.Size(191, 64)
        self._button7.TabIndex = 27
        self._button7.Text = "Saturn"
        self._button7.UseVisualStyleBackColor = False
        self._button7.Click += self.Button7Click
        # 
        # button8
        # 
        self._button8.BackColor = System.Drawing.Color.DarkKhaki
        self._button8.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._button8.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button8.Location = System.Drawing.Point(42, 250)
        self._button8.Name = "button8"
        self._button8.Size = System.Drawing.Size(191, 64)
        self._button8.TabIndex = 26
        self._button8.Text = "Jupiter"
        self._button8.UseVisualStyleBackColor = False
        self._button8.Click += self.Button8Click
        # 
        # button9
        # 
        self._button9.BackColor = System.Drawing.Color.White
        self._button9.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._button9.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button9.Location = System.Drawing.Point(263, 426)
        self._button9.Name = "button9"
        self._button9.Size = System.Drawing.Size(191, 64)
        self._button9.TabIndex = 31
        self._button9.Text = "Exit"
        self._button9.UseVisualStyleBackColor = False
        self._button9.Click += self.Button9Click
        # 
        # button10
        # 
        self._button10.BackColor = System.Drawing.Color.SandyBrown
        self._button10.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._button10.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button10.Location = System.Drawing.Point(42, 426)
        self._button10.Name = "button10"
        self._button10.Size = System.Drawing.Size(191, 64)
        self._button10.TabIndex = 30
        self._button10.Text = "Pluto"
        self._button10.UseVisualStyleBackColor = False
        self._button10.Click += self.Button10Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaptionText
        self.ClientSize = System.Drawing.Size(495, 564)
        self.Controls.Add(self._button9)
        self.Controls.Add(self._button10)
        self.Controls.Add(self._button5)
        self.Controls.Add(self._button6)
        self.Controls.Add(self._button7)
        self.Controls.Add(self._button8)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button4)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "prog486astronomy"
        self.ResumeLayout(False)


    def Button3Click(self, sender, e):
        from Form3 import *
        Form3 = Form3(self)
        Form3.Show()
        self.Hide() # mars

    def Button1Click(self, sender, e):
        from Form1 import *
        Form1 = Form1(self)
        Form1.Show()
        self.Hide() # mercury

    def Button2Click(self, sender, e):
        from Form2 import *
        Form2 = Form2(self)
        Form2.Show()
        self.Hide() # venus

    def Button4Click(self, sender, e):
        from Form4 import *
        Form4 = Form4(self)
        Form4.Show()
        self.Hide() # earth

    def Button8Click(self, sender, e):
        from Form8 import *
        Form8 = Form8(self)
        Form8.Show()
        self.Hide() # jupiter

    def Button7Click(self, sender, e):
        from Form7 import *
        Form7 = Form7(self)
        Form7.Show()
        self.Hide() # saturn

    def Button6Click(self, sender, e):
        from Form6 import *
        Form6 = Form6(self)
        Form6.Show()
        self.Hide() # uranus

    def Button5Click(self, sender, e):
        from Form5 import *
        Form5 = Form5(self)
        Form5.Show()
        self.Hide() # neptune

    def Button10Click(self, sender, e):
        from Form9 import *
        Form9 = Form9(self)
        Form9.Show()
        self.Hide() # pluto

    def Button9Click(self, sender, e):
        Application.Exit()