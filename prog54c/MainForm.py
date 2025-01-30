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
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.IndianRed
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(44, 47)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(504, 41)
        self._label1.TabIndex = 0
        self._label1.Text = "Radius:"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.IndianRed
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(44, 109)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(504, 41)
        self._label2.TabIndex = 1
        self._label2.Text = "Circumference:"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.IndianRed
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(44, 171)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(504, 41)
        self._label3.TabIndex = 2
        self._label3.Text = "Area:"
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Firebrick
        self._button1.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(44, 244)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(140, 60)
        self._button1.TabIndex = 3
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Firebrick
        self._button2.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(227, 244)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(140, 60)
        self._button2.TabIndex = 4
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Firebrick
        self._button3.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(408, 244)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(140, 60)
        self._button3.TabIndex = 5
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.LightCoral
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(303, 117)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(227, 26)
        self._label4.TabIndex = 6
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.LightCoral
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(303, 180)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(227, 26)
        self._label5.TabIndex = 7
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.Color.LightCoral
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(303, 53)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(227, 29)
        self._textBox1.TabIndex = 8
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Maroon
        self.ClientSize = System.Drawing.Size(586, 354)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "prog54c"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        r = float(self._textBox1.Text)
        pi = 3.14159
        c = 2 * r * pi
        a = pi * (r ** 2)
        self._label4.Text = "%.3f" % c
        self._label5.Text = "%.3f" % a

    def Button2Click(self, sender, e):
        self._label4.Text = ""
        self._label5.Text = ""
        self._textBox1.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()