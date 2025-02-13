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
        self._label3 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label1 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.SystemColors.MenuHighlight
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(243, 148)
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
        self._button1.Location = System.Drawing.Point(9, 148)
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
        self._textBox1.Location = System.Drawing.Point(173, 12)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(238, 31)
        self._textBox1.TabIndex = 9
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.SystemColors.MenuHighlight
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(311, 83)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(100, 37)
        self._label3.TabIndex = 8
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.MenuHighlight
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(8, 83)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(297, 37)
        self._label2.TabIndex = 7
        self._label2.Text = "First Unique Character:"
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.MenuHighlight
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(8, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(158, 37)
        self._label1.TabIndex = 6
        self._label1.Text = "Enter Text:"
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.IndianRed
        self.ClientSize = System.Drawing.Size(425, 232)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "strInt3"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        self._label3.Text = ""
        word = str(self._textBox1.Text)
        sub = 0
        for i in range(len(word)):
            letter = word[i]
            int = word.rfind(letter)
            if int == -1:
                break
        if word[i] == word[int]:
            self._label3.Text = letter

    def Button2Click(self, sender, e):
        self._label3.Text = ""