import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
        self.price = 0
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._label9 = System.Windows.Forms.Label()
        self._label10 = System.Windows.Forms.Label()
        self._label11 = System.Windows.Forms.Label()
        self._label12 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._textBox4 = System.Windows.Forms.TextBox()
        self._textBox5 = System.Windows.Forms.TextBox()
        self._textBox6 = System.Windows.Forms.TextBox()
        self._textBox7 = System.Windows.Forms.TextBox()
        self._textBox8 = System.Windows.Forms.TextBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.DarkSeaGreen
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(481, 214)
        self._label1.TabIndex = 0
        self._label1.Text = "Registrant"
        self._label1.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.DarkSeaGreen
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(33, 40)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(100, 28)
        self._label2.TabIndex = 1
        self._label2.Text = "Name:"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.DarkSeaGreen
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(33, 87)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(112, 28)
        self._label3.TabIndex = 2
        self._label3.Text = "Company:"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.DarkSeaGreen
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(33, 135)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(100, 28)
        self._label4.TabIndex = 3
        self._label4.Text = "Address:"
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.DarkSeaGreen
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(33, 187)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(100, 28)
        self._label5.TabIndex = 4
        self._label5.Text = "City:"
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.DarkSeaGreen
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(274, 40)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(100, 28)
        self._label6.TabIndex = 5
        self._label6.Text = "Phone:"
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.DarkSeaGreen
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(274, 87)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(100, 28)
        self._label7.TabIndex = 6
        self._label7.Text = "Email:"
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.DarkSeaGreen
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(209, 187)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(100, 28)
        self._label8.TabIndex = 7
        self._label8.Text = "State:"
        # 
        # label9
        # 
        self._label9.BackColor = System.Drawing.Color.DarkSeaGreen
        self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.Location = System.Drawing.Point(349, 187)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(100, 28)
        self._label9.TabIndex = 8
        self._label9.Text = "Zip:"
        # 
        # label10
        # 
        self._label10.BackColor = System.Drawing.Color.DarkSeaGreen
        self._label10.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label10.Location = System.Drawing.Point(12, 223)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(481, 49)
        self._label10.TabIndex = 9
        self._label10.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # label11
        # 
        self._label11.BackColor = System.Drawing.Color.DarkSeaGreen
        self._label11.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label11.Location = System.Drawing.Point(231, 233)
        self._label11.Name = "label11"
        self._label11.Size = System.Drawing.Size(122, 28)
        self._label11.TabIndex = 10
        self._label11.Text = "Total Cost:"
        # 
        # label12
        # 
        self._label12.BackColor = System.Drawing.Color.DarkSeaGreen
        self._label12.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label12.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label12.Location = System.Drawing.Point(349, 233)
        self._label12.Name = "label12"
        self._label12.Size = System.Drawing.Size(122, 28)
        self._label12.TabIndex = 11
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.Color.LightGreen
        self._textBox1.BorderStyle = System.Windows.Forms.BorderStyle.None
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(107, 40)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(161, 24)
        self._textBox1.TabIndex = 12
        # 
        # textBox2
        # 
        self._textBox2.BackColor = System.Drawing.Color.LightGreen
        self._textBox2.BorderStyle = System.Windows.Forms.BorderStyle.None
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(349, 40)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(128, 24)
        self._textBox2.TabIndex = 13
        # 
        # textBox3
        # 
        self._textBox3.BackColor = System.Drawing.Color.LightGreen
        self._textBox3.BorderStyle = System.Windows.Forms.BorderStyle.None
        self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(349, 87)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(128, 24)
        self._textBox3.TabIndex = 14
        # 
        # textBox4
        # 
        self._textBox4.BackColor = System.Drawing.Color.LightGreen
        self._textBox4.BorderStyle = System.Windows.Forms.BorderStyle.None
        self._textBox4.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox4.Location = System.Drawing.Point(140, 91)
        self._textBox4.Name = "textBox4"
        self._textBox4.Size = System.Drawing.Size(128, 24)
        self._textBox4.TabIndex = 15
        # 
        # textBox5
        # 
        self._textBox5.BackColor = System.Drawing.Color.LightGreen
        self._textBox5.BorderStyle = System.Windows.Forms.BorderStyle.None
        self._textBox5.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox5.Location = System.Drawing.Point(140, 139)
        self._textBox5.Name = "textBox5"
        self._textBox5.Size = System.Drawing.Size(337, 24)
        self._textBox5.TabIndex = 16
        # 
        # textBox6
        # 
        self._textBox6.BackColor = System.Drawing.Color.LightGreen
        self._textBox6.BorderStyle = System.Windows.Forms.BorderStyle.None
        self._textBox6.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox6.Location = System.Drawing.Point(89, 187)
        self._textBox6.Name = "textBox6"
        self._textBox6.Size = System.Drawing.Size(114, 24)
        self._textBox6.TabIndex = 17
        # 
        # textBox7
        # 
        self._textBox7.BackColor = System.Drawing.Color.LightGreen
        self._textBox7.BorderStyle = System.Windows.Forms.BorderStyle.None
        self._textBox7.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox7.Location = System.Drawing.Point(274, 187)
        self._textBox7.Name = "textBox7"
        self._textBox7.Size = System.Drawing.Size(69, 24)
        self._textBox7.TabIndex = 18
        # 
        # textBox8
        # 
        self._textBox8.BackColor = System.Drawing.Color.LightGreen
        self._textBox8.BorderStyle = System.Windows.Forms.BorderStyle.None
        self._textBox8.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox8.Location = System.Drawing.Point(396, 187)
        self._textBox8.Name = "textBox8"
        self._textBox8.Size = System.Drawing.Size(81, 24)
        self._textBox8.TabIndex = 19
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.DarkSeaGreen
        self._button1.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 279)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(191, 64)
        self._button1.TabIndex = 20
        self._button1.Text = "Select Conference Options"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.DarkSeaGreen
        self._button2.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(218, 288)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(125, 47)
        self._button2.TabIndex = 21
        self._button2.Text = "Reset"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.DarkSeaGreen
        self._button3.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(352, 288)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(125, 47)
        self._button3.TabIndex = 22
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.SeaGreen
        self.ClientSize = System.Drawing.Size(505, 354)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox8)
        self.Controls.Add(self._textBox7)
        self.Controls.Add(self._textBox6)
        self.Controls.Add(self._textBox5)
        self.Controls.Add(self._textBox4)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label12)
        self.Controls.Add(self._label11)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._label10)
        self.Name = "MainForm"
        self.Text = "pg479conferenceRegistration"
        self.Load += self.MainFormLoad
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button3Click(self, sender, e):
        Application.Exit()

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox3.Text = ""
        self._textBox4.Text = ""
        self._textBox5.Text = ""
        self._textBox6.Text = ""
        self._textBox7.Text = ""
        self._textBox8.Text = ""
        self._label12.Text = ""

    def Button1Click(self, sender, e):
        from Form1 import *
        Form1 = Form1(self)
        Form1.Show()
        self.Hide()
        self.price = 0

    def MainFormLoad(self, sender, e):
        self._label12.Text = str(self.price)

    def Button4Click(self, sender, e):
        self._label12.Text = str(self.price)