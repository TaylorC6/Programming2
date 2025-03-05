
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Misc(Form):
    def __init__(self, parent):
        self.myparent = parent
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button5 = System.Windows.Forms.Button()
        self._label2 = System.Windows.Forms.Label()
        self._checkBox1 = System.Windows.Forms.CheckBox()
        self._checkBox2 = System.Windows.Forms.CheckBox()
        self._checkBox3 = System.Windows.Forms.CheckBox()
        self._checkBox4 = System.Windows.Forms.CheckBox()
        self._checkBox5 = System.Windows.Forms.CheckBox()
        self.SuspendLayout()
        # 
        # button5
        # 
        self._button5.BackColor = System.Drawing.Color.IndianRed
        self._button5.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._button5.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button5.Location = System.Drawing.Point(72, 458)
        self._button5.Name = "button5"
        self._button5.Size = System.Drawing.Size(450, 52)
        self._button5.TabIndex = 10
        self._button5.Text = "Skate Shop"
        self._button5.UseVisualStyleBackColor = False
        self._button5.Click += self.Button5Click
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Brown
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(12, 443)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(562, 83)
        self._label2.TabIndex = 9
        self._label2.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # checkBox1
        # 
        self._checkBox1.BackColor = System.Drawing.Color.IndianRed
        self._checkBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox1.Location = System.Drawing.Point(72, 29)
        self._checkBox1.Name = "checkBox1"
        self._checkBox1.Size = System.Drawing.Size(450, 53)
        self._checkBox1.TabIndex = 11
        self._checkBox1.Text = "Grip tape $10"
        self._checkBox1.UseVisualStyleBackColor = False
        # 
        # checkBox2
        # 
        self._checkBox2.BackColor = System.Drawing.Color.IndianRed
        self._checkBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox2.Location = System.Drawing.Point(72, 110)
        self._checkBox2.Name = "checkBox2"
        self._checkBox2.Size = System.Drawing.Size(450, 53)
        self._checkBox2.TabIndex = 12
        self._checkBox2.Text = "Bearings $30"
        self._checkBox2.UseVisualStyleBackColor = False
        # 
        # checkBox3
        # 
        self._checkBox3.BackColor = System.Drawing.Color.IndianRed
        self._checkBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox3.Location = System.Drawing.Point(72, 193)
        self._checkBox3.Name = "checkBox3"
        self._checkBox3.Size = System.Drawing.Size(450, 53)
        self._checkBox3.TabIndex = 13
        self._checkBox3.Text = "Riser pads $ 2"
        self._checkBox3.UseVisualStyleBackColor = False
        # 
        # checkBox4
        # 
        self._checkBox4.BackColor = System.Drawing.Color.IndianRed
        self._checkBox4.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox4.Location = System.Drawing.Point(72, 278)
        self._checkBox4.Name = "checkBox4"
        self._checkBox4.Size = System.Drawing.Size(450, 53)
        self._checkBox4.TabIndex = 14
        self._checkBox4.Text = "Nuts and bolts kit $ 3"
        self._checkBox4.UseVisualStyleBackColor = False
        # 
        # checkBox5
        # 
        self._checkBox5.BackColor = System.Drawing.Color.IndianRed
        self._checkBox5.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox5.Location = System.Drawing.Point(72, 361)
        self._checkBox5.Name = "checkBox5"
        self._checkBox5.Size = System.Drawing.Size(450, 53)
        self._checkBox5.TabIndex = 15
        self._checkBox5.Text = "Assembly $10"
        self._checkBox5.UseVisualStyleBackColor = False
        # 
        # Misc
        # 
        self.BackColor = System.Drawing.Color.Maroon
        self.ClientSize = System.Drawing.Size(586, 534)
        self.Controls.Add(self._checkBox5)
        self.Controls.Add(self._checkBox4)
        self.Controls.Add(self._checkBox3)
        self.Controls.Add(self._checkBox2)
        self.Controls.Add(self._checkBox1)
        self.Controls.Add(self._button5)
        self.Controls.Add(self._label2)
        self.Name = "Misc"
        self.Text = "Misc"
        self.ResumeLayout(False)


    def Button5Click(self, sender, e):
        self.myparent.Show()
        self.Hide()
        if self._checkBox1.Checked:
            self.myparent.price += 10
        if self._checkBox2.Checked:
            self.myparent.price += 30
        if self._checkBox3.Checked:
            self.myparent.price += 2
        if self._checkBox4.Checked:
            self.myparent.price += 3
        if self._checkBox5.Checked:
            self.myparent.price += 10
        else:
            pass
        

