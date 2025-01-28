import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._textBox4 = System.Windows.Forms.TextBox()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Cyan
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(27, 31)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(553, 41)
        self._label1.TabIndex = 0
        self._label1.Text = "Num 1:"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Yellow
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(27, 98)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(553, 41)
        self._label2.TabIndex = 1
        self._label2.Text = "Num 2:"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.Purple
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(27, 162)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(553, 41)
        self._label3.TabIndex = 2
        self._label3.Text = "Num 3:"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.Lime
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(27, 227)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(553, 41)
        self._label4.TabIndex = 3
        self._label4.Text = "Num 4:"
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.Red
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(27, 294)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(553, 41)
        self._label5.TabIndex = 4
        self._label5.Text = "Sum:"
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.Blue
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(27, 361)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(553, 41)
        self._label6.TabIndex = 5
        self._label6.Text = "Average:"
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.Color.FromArgb(255, 127, 0)
        self._textBox1.BorderStyle = System.Windows.Forms.BorderStyle.None
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(169, 39)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(361, 24)
        self._textBox1.TabIndex = 6
        # 
        # textBox2
        # 
        self._textBox2.BackColor = System.Drawing.Color.FromArgb(255, 127, 0)
        self._textBox2.BorderStyle = System.Windows.Forms.BorderStyle.None
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(169, 106)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(361, 24)
        self._textBox2.TabIndex = 7
        # 
        # textBox3
        # 
        self._textBox3.BackColor = System.Drawing.Color.FromArgb(255, 127, 0)
        self._textBox3.BorderStyle = System.Windows.Forms.BorderStyle.None
        self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(169, 170)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(361, 24)
        self._textBox3.TabIndex = 8
        # 
        # textBox4
        # 
        self._textBox4.BackColor = System.Drawing.Color.FromArgb(255, 127, 0)
        self._textBox4.BorderStyle = System.Windows.Forms.BorderStyle.None
        self._textBox4.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox4.Location = System.Drawing.Point(169, 234)
        self._textBox4.Name = "textBox4"
        self._textBox4.Size = System.Drawing.Size(361, 24)
        self._textBox4.TabIndex = 9
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.FromArgb(255, 127, 0)
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(169, 303)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(361, 23)
        self._label7.TabIndex = 10
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.FromArgb(255, 127, 0)
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(169, 369)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(361, 23)
        self._label8.TabIndex = 11
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Yellow
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(66, 440)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(157, 59)
        self._button1.TabIndex = 12
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Yellow
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(229, 440)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(157, 59)
        self._button2.TabIndex = 13
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Yellow
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(392, 440)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(157, 59)
        self._button3.TabIndex = 14
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(127, 127, 127)
        self.ClientSize = System.Drawing.Size(607, 531)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._textBox4)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "prog54b"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        n1 = float(self._textBox1.Text)
        n2 = float(self._textBox2.Text)
        n3 = float(self._textBox3.Text)
        n4 = float(self._textBox4.Text)
        sum = n1 + n2 + n3 + n4
        avg = (n1 + n2 + n3 + n4) // 4
        self._label7.Text = str(sum)
        self._label8.Text = str(avg)

    def Button2Click(self, sender, e):
        self._label7.Text = ""
        self._label8.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()