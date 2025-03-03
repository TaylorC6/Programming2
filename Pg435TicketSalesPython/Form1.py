
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form1(Form):
    def __init__(self, parent):
        myparent = parent
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button3 = System.Windows.Forms.Button()
        self._button1 = System.Windows.Forms.Button()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label3 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label1 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._radioButton1 = System.Windows.Forms.RadioButton()
        self._radioButton2 = System.Windows.Forms.RadioButton()
        self._radioButton3 = System.Windows.Forms.RadioButton()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._label9 = System.Windows.Forms.Label()
        self._label10 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.SystemColors.MenuHighlight
        self._button3.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(298, 349)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(176, 70)
        self._button3.TabIndex = 25
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.SystemColors.MenuHighlight
        self._button1.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(68, 349)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(170, 70)
        self._button1.TabIndex = 23
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.SystemColors.MenuHighlight
        self._textBox1.BorderStyle = System.Windows.Forms.BorderStyle.None
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(329, 127)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(170, 24)
        self._textBox1.TabIndex = 22
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.SystemColors.MenuHighlight
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(11, 175)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(248, 153)
        self._label3.TabIndex = 21
        self._label3.Text = "Section:"
        self._label3.Click += self.Label3Click
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.LightSkyBlue
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(86, 120)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(422, 37)
        self._label2.TabIndex = 20
        self._label2.Text = "Number of Tickets:"
        self._label2.Click += self.Label2Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.MenuHighlight
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(11, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(506, 158)
        self._label1.TabIndex = 19
        self._label1.Text = "How Many Tickets?"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.SystemColors.MenuHighlight
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(265, 175)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(253, 153)
        self._label4.TabIndex = 26
        self._label4.Text = "Total Cost:"
        # 
        # radioButton1
        # 
        self._radioButton1.BackColor = System.Drawing.Color.LightSkyBlue
        self._radioButton1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton1.ForeColor = System.Drawing.Color.Black
        self._radioButton1.Location = System.Drawing.Point(25, 215)
        self._radioButton1.Name = "radioButton1"
        self._radioButton1.Size = System.Drawing.Size(213, 29)
        self._radioButton1.TabIndex = 27
        self._radioButton1.TabStop = True
        self._radioButton1.Text = "Section A"
        self._radioButton1.UseVisualStyleBackColor = False
        # 
        # radioButton2
        # 
        self._radioButton2.BackColor = System.Drawing.Color.LightSkyBlue
        self._radioButton2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton2.ForeColor = System.Drawing.Color.Black
        self._radioButton2.Location = System.Drawing.Point(25, 250)
        self._radioButton2.Name = "radioButton2"
        self._radioButton2.Size = System.Drawing.Size(213, 29)
        self._radioButton2.TabIndex = 28
        self._radioButton2.TabStop = True
        self._radioButton2.Text = "Section B"
        self._radioButton2.UseVisualStyleBackColor = False
        # 
        # radioButton3
        # 
        self._radioButton3.BackColor = System.Drawing.Color.LightSkyBlue
        self._radioButton3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton3.ForeColor = System.Drawing.Color.Black
        self._radioButton3.Location = System.Drawing.Point(25, 285)
        self._radioButton3.Name = "radioButton3"
        self._radioButton3.Size = System.Drawing.Size(213, 29)
        self._radioButton3.TabIndex = 29
        self._radioButton3.TabStop = True
        self._radioButton3.Text = "Section C"
        self._radioButton3.UseVisualStyleBackColor = False
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.LightSkyBlue
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(273, 209)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(240, 37)
        self._label5.TabIndex = 30
        self._label5.Text = "Number of Tickets:"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.LightSkyBlue
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(273, 246)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(240, 37)
        self._label6.TabIndex = 32
        self._label6.Text = "Tax:"
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.LightSkyBlue
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(273, 283)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(240, 37)
        self._label7.TabIndex = 34
        self._label7.Text = "Total:"
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.SystemColors.MenuHighlight
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(418, 285)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(83, 30)
        self._label8.TabIndex = 35
        # 
        # label9
        # 
        self._label9.BackColor = System.Drawing.SystemColors.MenuHighlight
        self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.Location = System.Drawing.Point(418, 250)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(83, 30)
        self._label9.TabIndex = 36
        # 
        # label10
        # 
        self._label10.BackColor = System.Drawing.SystemColors.MenuHighlight
        self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label10.Location = System.Drawing.Point(418, 215)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(83, 30)
        self._label10.TabIndex = 37
        # 
        # Form1
        # 
        self.BackColor = System.Drawing.Color.SteelBlue
        self.ClientSize = System.Drawing.Size(527, 431)
        self.Controls.Add(self._label10)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._radioButton3)
        self.Controls.Add(self._radioButton2)
        self.Controls.Add(self._radioButton1)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "Form1"
        self.Text = "Form1"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Label3Click(self, sender, e):
        pass

    def Button1Click(self, sender, e):
        sectionA = False
        sectionB = False
        sectionC = False
        Ticketslbl = self._label10.Text
        Taxlbl = self._label9.Text
        Total = 0
        Totallbl = self._label8.Text
        A = 20
        B = 15
        C = 10
        Tax = 0.06
        
         if self._radioButton1.Checked == True:
             sectionA = True
         elif self._radioButton2.Checked == True:
             sectionB = True
         elif self._radioButton3.Checked == True:
             sectionC = True

    def Button3Click(self, sender, e):
        self.myparent.Show()
        self.Hide()
        