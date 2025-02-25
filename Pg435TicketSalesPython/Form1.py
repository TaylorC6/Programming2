
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form1(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button3 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button1 = System.Windows.Forms.Button()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label3 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label1 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.SystemColors.MenuHighlight
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(350, 316)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(168, 70)
        self._button3.TabIndex = 25
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.SystemColors.MenuHighlight
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(176, 316)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(168, 70)
        self._button2.TabIndex = 24
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.SystemColors.MenuHighlight
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(2, 316)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(168, 70)
        self._button1.TabIndex = 23
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.SystemColors.MenuHighlight
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(167, 5)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(238, 31)
        self._textBox1.TabIndex = 22
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.SystemColors.MenuHighlight
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(305, 76)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(100, 37)
        self._label3.TabIndex = 21
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.MenuHighlight
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(2, 76)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(297, 37)
        self._label2.TabIndex = 20
        self._label2.Text = "First Unique Character:"
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.MenuHighlight
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(2, 2)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(158, 37)
        self._label1.TabIndex = 19
        self._label1.Text = "Enter Text:"
        # 
        # Form1
        # 
        self.ClientSize = System.Drawing.Size(520, 391)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "Form1"
        self.Text = "Form1"
        self.ResumeLayout(False)
        self.PerformLayout()

