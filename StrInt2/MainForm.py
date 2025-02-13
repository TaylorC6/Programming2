import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button2 = System.Windows.Forms.Button()
        self._button1 = System.Windows.Forms.Button()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label1 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._textBox2 = System.Windows.Forms.TextBox()
        self.SuspendLayout()
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.SystemColors.MenuHighlight
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.Color.Transparent
        self._button2.Location = System.Drawing.Point(247, 248)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(168, 70)
        self._button2.TabIndex = 11
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.SystemColors.MenuHighlight
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.Color.Transparent
        self._button1.Location = System.Drawing.Point(13, 248)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(168, 70)
        self._button1.TabIndex = 10
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.SystemColors.MenuHighlight
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(202, 17)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(213, 31)
        self._textBox1.TabIndex = 9
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.MenuHighlight
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.Transparent
        self._label1.Location = System.Drawing.Point(12, 14)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(184, 37)
        self._label1.TabIndex = 6
        self._label1.Text = "Enter Word1:"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.SystemColors.MenuHighlight
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(177, 174)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(239, 37)
        self._label4.TabIndex = 13
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.SystemColors.MenuHighlight
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.ForeColor = System.Drawing.Color.Transparent
        self._label5.Location = System.Drawing.Point(13, 174)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(158, 37)
        self._label5.TabIndex = 12
        self._label5.Text = "Anagrams?"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.MenuHighlight
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.Color.Transparent
        self._label2.Location = System.Drawing.Point(12, 95)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(184, 37)
        self._label2.TabIndex = 7
        self._label2.Text = "Enter Word2:"
        # 
        # textBox2
        # 
        self._textBox2.BackColor = System.Drawing.SystemColors.MenuHighlight
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(202, 98)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(214, 31)
        self._textBox2.TabIndex = 14
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.DeepSkyBlue
        self.ClientSize = System.Drawing.Size(428, 330)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "StrInt2"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        self._label4.Text = ""
        word1 = self._textBox1.Text.lower()
        word2 = self._textBox2.Text.lower()
        
        if len(word1) != len(word2):
            self._label4.Text = "False"
        else:
            for lcv in range(len(word1)):
                c = word1[lcv]
                index = word2.find(c)
                if index == -1:
                    self._label4.Text = "False"
                else:
                    word2 = word2[0:index] + word2[index + 1:]
        self._label4.Text = str(len(word2) == 0)
            

    def Button2Click(self, sender, e):
        self._label4.Text = ""