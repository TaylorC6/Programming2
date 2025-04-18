﻿
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form3(Form):
    def __init__(self, parent):
        self.myparent = parent
        self.InitializeComponent()
    
    def InitializeComponent(self):
        resources = System.Resources.ResourceManager("prog486astronomy.Form3", System.Reflection.Assembly.GetEntryAssembly())
        self._pictureBox1 = System.Windows.Forms.PictureBox()
        self._button1 = System.Windows.Forms.Button()
        self._label5 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label1 = System.Windows.Forms.Label()
        self._pictureBox1.BeginInit()
        self.SuspendLayout()
        # 
        # pictureBox1
        # 
        self._pictureBox1.Image = resources.GetObject("pictureBox1.Image")
        self._pictureBox1.Location = System.Drawing.Point(2, 32)
        self._pictureBox1.Name = "pictureBox1"
        self._pictureBox1.Size = System.Drawing.Size(552, 470)
        self._pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom
        self._pictureBox1.TabIndex = 3
        self._pictureBox1.TabStop = False
        # 
        # button1
        # 
        self._button1.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.Color.White
        self._button1.Location = System.Drawing.Point(430, 480)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(111, 51)
        self._button1.TabIndex = 5
        self._button1.Text = "Exit"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.FromArgb(192, 0, 0)
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.ForeColor = System.Drawing.Color.White
        self._label5.Location = System.Drawing.Point(9, 434)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(349, 47)
        self._label5.TabIndex = 19
        self._label5.Text = "Surface temperature –50°C to 50°C"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.FromArgb(192, 0, 0)
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.Color.White
        self._label4.Location = System.Drawing.Point(9, 387)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(349, 47)
        self._label4.TabIndex = 18
        self._label4.Text = "Mass 5.967 × 1024 kg"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.FromArgb(192, 0, 0)
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.Color.White
        self._label3.Location = System.Drawing.Point(9, 340)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(362, 47)
        self._label3.TabIndex = 17
        self._label3.Text = "Average distance from the sun 1.5237 AU"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.FromArgb(192, 0, 0)
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.Color.White
        self._label2.Location = System.Drawing.Point(9, 292)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(284, 242)
        self._label2.TabIndex = 16
        self._label2.Text = "Type Terrestrial"
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.FromArgb(192, 0, 0)
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.White
        self._label1.Location = System.Drawing.Point(9, 239)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(362, 295)
        self._label1.TabIndex = 15
        self._label1.Text = "Mars"
        # 
        # Form3
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaptionText
        self.ClientSize = System.Drawing.Size(553, 543)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._pictureBox1)
        self.Name = "Form3"
        self.Text = "Form3"
        self._pictureBox1.EndInit()
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self.myparent.Show()
        self.Hide()