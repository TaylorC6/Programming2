import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._label6 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(155, 56)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(225, 38)
        self._textBox1.TabIndex = 0
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(155, 140)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(225, 38)
        self._textBox2.TabIndex = 1
        # 
        # label1
        # 
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.White
        self._label1.Location = System.Drawing.Point(35, 58)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(114, 36)
        self._label1.TabIndex = 2
        self._label1.Text = "Length:"
        # 
        # label2
        # 
        self._label2.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.Color.White
        self._label2.Location = System.Drawing.Point(35, 142)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(114, 36)
        self._label2.TabIndex = 3
        self._label2.Text = "Width:"
        # 
        # label3
        # 
        self._label3.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.Color.White
        self._label3.Location = System.Drawing.Point(35, 242)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(114, 36)
        self._label3.TabIndex = 4
        self._label3.Text = "Area:"
        # 
        # label4
        # 
        self._label4.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.Color.White
        self._label4.Location = System.Drawing.Point(35, 321)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(114, 36)
        self._label4.TabIndex = 5
        self._label4.Text = "Perimeter:"
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(46, 420)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(123, 50)
        self._button1.TabIndex = 6
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(218, 420)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(123, 50)
        self._button2.TabIndex = 7
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.White
        self._label6.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.ForeColor = System.Drawing.Color.Black
        self._label6.Location = System.Drawing.Point(155, 321)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(225, 36)
        self._label6.TabIndex = 9
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.White
        self._label5.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.ForeColor = System.Drawing.Color.Black
        self._label5.Location = System.Drawing.Point(155, 242)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(225, 36)
        self._label5.TabIndex = 10
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(386, 420)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(123, 50)
        self._button3.TabIndex = 11
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaptionText
        self.ClientSize = System.Drawing.Size(548, 515)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Name = "MainForm"
        self.Text = "Prog52a"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        l = int(self._textBox1.Text)
        w = int(self._textBox2.Text)
        a = l * w
        p = l * 2 + w * 2
        self._label5.Text = str(a)
        self._label6.Text = str(p)

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._label5.Text = ""
        self._label6.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()