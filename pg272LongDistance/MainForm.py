import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._radioButton1 = System.Windows.Forms.RadioButton()
        self._radioButton2 = System.Windows.Forms.RadioButton()
        self._radioButton3 = System.Windows.Forms.RadioButton()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.DarkSeaGreen
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(66, 457)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(149, 62)
        self._button1.TabIndex = 0
        self._button1.Text = "Show"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.DarkSeaGreen
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(241, 457)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(149, 62)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.DarkSeaGreen
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(418, 457)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(149, 62)
        self._button3.TabIndex = 2
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # radioButton1
        # 
        self._radioButton1.BackColor = System.Drawing.Color.LightGreen
        self._radioButton1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton1.Location = System.Drawing.Point(40, 61)
        self._radioButton1.Name = "radioButton1"
        self._radioButton1.Size = System.Drawing.Size(149, 44)
        self._radioButton1.TabIndex = 3
        self._radioButton1.TabStop = True
        self._radioButton1.Text = "Daytime"
        self._radioButton1.UseVisualStyleBackColor = False

        # 
        # radioButton2
        # 
        self._radioButton2.BackColor = System.Drawing.Color.LightGreen
        self._radioButton2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton2.Location = System.Drawing.Point(40, 135)
        self._radioButton2.Name = "radioButton2"
        self._radioButton2.Size = System.Drawing.Size(149, 44)
        self._radioButton2.TabIndex = 4
        self._radioButton2.TabStop = True
        self._radioButton2.Text = "Evening"
        self._radioButton2.UseVisualStyleBackColor = False

        # 
        # radioButton3
        # 
        self._radioButton3.BackColor = System.Drawing.Color.LightGreen
        self._radioButton3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton3.Location = System.Drawing.Point(40, 209)
        self._radioButton3.Name = "radioButton3"
        self._radioButton3.Size = System.Drawing.Size(149, 44)
        self._radioButton3.TabIndex = 5
        self._radioButton3.TabStop = True
        self._radioButton3.Text = "Off-Peak"
        self._radioButton3.UseVisualStyleBackColor = False

        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.Color.DarkSeaGreen
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(266, 313)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(194, 40)
        self._textBox1.TabIndex = 6
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.LightGreen
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(40, 315)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(211, 34)
        self._label1.TabIndex = 7
        self._label1.Text = "Enter Minutes:"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.LightGreen
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(40, 393)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(91, 34)
        self._label2.TabIndex = 8
        self._label2.Text = "Cost:"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.LightGreen
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(171, 393)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(289, 34)
        self._label3.TabIndex = 9
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.LightGreen
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(204, 67)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(434, 34)
        self._label4.TabIndex = 10
        self._label4.Text = "(6:00 a.m. through 5:59 P.M.)      $0.07"
        self._label4.Click += self.Label4Click
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.LightGreen
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(467, 22)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(171, 28)
        self._label5.TabIndex = 11
        self._label5.Text = "Rate Per Minute"
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.LightGreen
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(204, 141)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(434, 34)
        self._label6.TabIndex = 12
        self._label6.Text = "(6:00 p.m. through 11:59 P.M.)    $0.12"
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.LightGreen
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(204, 215)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(434, 34)
        self._label7.TabIndex = 13
        self._label7.Text = "(12:00 a.m. through 5:59 A.M.)    $0.05"
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.SeaGreen
        self.ClientSize = System.Drawing.Size(650, 557)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._radioButton3)
        self.Controls.Add(self._radioButton2)
        self.Controls.Add(self._radioButton1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "pg272LongDistance"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Label4Click(self, sender, e):
        pass

    def Button1Click(self, sender, e):
        price = 0.0
        if self._radioButton1.Checked == True:
            price = 0.07
        elif self._radioButton2.Checked == True:
            price = 0.12
        elif self._radioButton3.Checked == True:
            price = 0.05
        else:
            MessageBox.Show("No. Select time dummy.")
            return
        mins = int(self._textBox1.Text)
        self._label3.Text = "$ %.2f" % (mins * price)

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._label3.Text = ""
        self._radioButton1.Checked = False
        self._radioButton2.Checked = False
        self._radioButton3.Checked = False

    def Button3Click(self, sender, e):
        Application.Exit()