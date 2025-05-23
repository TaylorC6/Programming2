﻿import System.Drawing
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
        self._textBox1 = System.Windows.Forms.TextBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.MenuHighlight
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 47)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(158, 37)
        self._label1.TabIndex = 0
        self._label1.Text = "Enter Text:"
        self._label1.Click += self.Label1Click
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.MenuHighlight
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(12, 121)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(158, 37)
        self._label2.TabIndex = 1
        self._label2.Text = "Duplicates:"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.SystemColors.MenuHighlight
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(176, 121)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(239, 37)
        self._label3.TabIndex = 2
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.SystemColors.MenuHighlight
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(177, 50)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(238, 31)
        self._textBox1.TabIndex = 3
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.SystemColors.MenuHighlight
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(13, 186)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(168, 70)
        self._button1.TabIndex = 4
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.SystemColors.MenuHighlight
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(247, 186)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(168, 70)
        self._button2.TabIndex = 5
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Maroon
        self.ClientSize = System.Drawing.Size(446, 297)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "StrInt"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Label1Click(self, sender, e):
        pass

    def Button1Click(self, sender, e):
        self._label3.Text = ""
        myStr = self._textBox1.Text.lower()
        for lcv in range(len(myStr)):
            for lcv2 in range(lcv + 1, len(myStr)):
                ltr1 = myStr[lcv]
                ltr2 = myStr[lcv2]
                if ltr1 == ltr2:
                    self._label3.Text += ltr1 + " "

    def Button2Click(self, sender, e):
        self._label3.Text = ""
        self._textBox1.Text = ""