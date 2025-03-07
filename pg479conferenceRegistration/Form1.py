
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form1(Form):
    def __init__(self, parent):
        self.myparent = parent
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button2 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._checkBox1 = System.Windows.Forms.CheckBox()
        self._checkBox2 = System.Windows.Forms.CheckBox()
        self._comboBox1 = System.Windows.Forms.ComboBox()
        self._button1 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.DarkSeaGreen
        self._button2.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(242, 182)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(112, 33)
        self._button2.TabIndex = 24
        self._button2.Text = "Reset"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.DarkSeaGreen
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(247, 160)
        self._label1.TabIndex = 23
        self._label1.Text = "Conference"
        self._label1.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.DarkSeaGreen
        self._label2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(265, 9)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(243, 160)
        self._label2.TabIndex = 26
        self._label2.Text = "Preference Workshops"
        self._label2.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # checkBox1
        # 
        self._checkBox1.BackColor = System.Drawing.Color.LightGreen
        self._checkBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox1.Location = System.Drawing.Point(28, 40)
        self._checkBox1.Name = "checkBox1"
        self._checkBox1.Size = System.Drawing.Size(218, 51)
        self._checkBox1.TabIndex = 27
        self._checkBox1.Text = "Conference Registration: $895"
        self._checkBox1.UseVisualStyleBackColor = False
        self._checkBox1.CheckedChanged += self.CheckBox1CheckedChanged
        # 
        # checkBox2
        # 
        self._checkBox2.BackColor = System.Drawing.Color.LightGreen
        self._checkBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox2.Location = System.Drawing.Point(28, 106)
        self._checkBox2.Name = "checkBox2"
        self._checkBox2.Size = System.Drawing.Size(218, 44)
        self._checkBox2.TabIndex = 28
        self._checkBox2.Text = "Opening Night Dinner and Keynote: $30"
        self._checkBox2.UseVisualStyleBackColor = False
        self._checkBox2.CheckedChanged += self.CheckBox2CheckedChanged
        # 
        # comboBox1
        # 
        self._comboBox1.BackColor = System.Drawing.Color.LightGreen
        self._comboBox1.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._comboBox1.FormattingEnabled = True
        self._comboBox1.Items.AddRange(System.Array[System.Object](
            ["Introduction to E-commerce $295",
            "The Future of the Web $295",
            "Advanced Visual Basic $395",
            "Network Security $395"]))
        self._comboBox1.Location = System.Drawing.Point(282, 40)
        self._comboBox1.Name = "comboBox1"
        self._comboBox1.Size = System.Drawing.Size(207, 21)
        self._comboBox1.TabIndex = 29
        self._comboBox1.SelectedIndexChanged += self.ComboBox1SelectedIndexChanged
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.DarkSeaGreen
        self._button1.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(377, 182)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(112, 33)
        self._button1.TabIndex = 30
        self._button1.Text = "Exit"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # Form1
        # 
        self.BackColor = System.Drawing.Color.SeaGreen
        self.ClientSize = System.Drawing.Size(523, 230)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._comboBox1)
        self.Controls.Add(self._checkBox2)
        self.Controls.Add(self._checkBox1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._label1)
        self.Name = "Form1"
        self.Text = "Form1"
        self.ResumeLayout(False)


    def Button2Click(self, sender, e):
        self._checkBox1.Checked = False
        self._checkBox2.Checked = False
        self._comboBox1.Text = ""

    def Button1Click(self, sender, e):
        self.myparent.Show()
        self.Hide()
        if self._checkBox1.Checked:
            self.myparent.price += 895
        if self._checkBox2.Checked:
            self.myparent.price += 30
        c = self._comboBox1.Text
        if c == "Introduction to E-commerce $295":
            self.myparent.price += 295
        elif c == "The Future of the Web $295":
            self.myparent.price += 295
        elif c == "Advanced Visual Basic $395":
            self.myparent.price += 395
        elif c == "Network Security $395":
            self.myparent.price += 395
        self.myparent._label12.Text = str(self.myparent.price)

    def CheckBox1CheckedChanged(self, sender, e):
#        self.myparent.price += 895
#        self._label1.Text = str(self.myparent.price)
         pass

    def CheckBox2CheckedChanged(self, sender, e):
#        self.myparent.price += 30
#        self._label1.Text = str(self.myparent.price)
         pass
 
    def ComboBox1SelectedIndexChanged(self, sender, e):
#        c = self._comboBox1.Text
#        if c == "Introduction to E-commerce $295":
#            self.myparent.price += 295
#        elif c == "The Future of the Web $295":
#            self.myparent.price += 295
#        elif c == "Advanced Visual Basic $395":
#            self.myparent.price += 395
#        elif c == "Network Security $395":
#            self.myparent.price += 395
         pass
        



    def Button3Click(self, sender, e):
#        self._label3.Text = str(self.myparent.price)
        pass