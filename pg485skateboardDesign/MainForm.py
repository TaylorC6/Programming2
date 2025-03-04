import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.price = 0.0
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._button4 = System.Windows.Forms.Button()
        self._label2 = System.Windows.Forms.Label()
        self._button5 = System.Windows.Forms.Button()
        self._button6 = System.Windows.Forms.Button()
        self._label3 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Brown
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(39, 29)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(562, 338)
        self._label1.TabIndex = 0
        self._label1.Text = "Skate Shop"
        self._label1.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.IndianRed
        self._button1.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(100, 77)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(450, 52)
        self._button1.TabIndex = 1
        self._button1.Text = "Decks"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.IndianRed
        self._button2.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(100, 148)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(450, 52)
        self._button2.TabIndex = 2
        self._button2.Text = "Truck Assemblies"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.IndianRed
        self._button3.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(100, 220)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(450, 52)
        self._button3.TabIndex = 3
        self._button3.Text = "Wheel Sets"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # button4
        # 
        self._button4.BackColor = System.Drawing.Color.IndianRed
        self._button4.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._button4.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button4.Location = System.Drawing.Point(100, 289)
        self._button4.Name = "button4"
        self._button4.Size = System.Drawing.Size(450, 52)
        self._button4.TabIndex = 4
        self._button4.Text = "Misc. Products"
        self._button4.UseVisualStyleBackColor = False
        self._button4.Click += self.Button4Click
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Brown
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(39, 381)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(562, 83)
        self._label2.TabIndex = 5
        self._label2.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # button5
        # 
        self._button5.BackColor = System.Drawing.Color.IndianRed
        self._button5.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._button5.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button5.Location = System.Drawing.Point(203, 395)
        self._button5.Name = "button5"
        self._button5.Size = System.Drawing.Size(71, 52)
        self._button5.TabIndex = 6
        self._button5.Text = "Exit"
        self._button5.UseVisualStyleBackColor = False
        self._button5.Click += self.Button5Click
        # 
        # button6
        # 
        self._button6.BackColor = System.Drawing.Color.IndianRed
        self._button6.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._button6.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button6.Location = System.Drawing.Point(54, 395)
        self._button6.Name = "button6"
        self._button6.Size = System.Drawing.Size(143, 52)
        self._button6.TabIndex = 7
        self._button6.Text = "Checkout"
        self._button6.UseVisualStyleBackColor = False
        self._button6.Click += self.Button6Click
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.IndianRed
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(280, 395)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(310, 55)
        self._label3.TabIndex = 8
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Maroon
        self.ClientSize = System.Drawing.Size(636, 478)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._button6)
        self.Controls.Add(self._button5)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._button4)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "pg485skateboardDesign"
        self.ResumeLayout(False)


    def Button5Click(self, sender, e):
        Application.Exit()

    def Button1Click(self, sender, e):
        from Decks import *
        Decks = Form1(self)
        Decks.Show()
        self.Hide()

    def Button2Click(self, sender, e):
        from TruckAssemblies import *
        TruckAssemblies = TruckAssemblies(self)
        TruckAssemblies.Show()
        self.Hide()

    def Button3Click(self, sender, e):
        from WheelSets import *
        WheelSets = WheelSets(self)
        WheelSets.Show()
        self.Hide()

    def Button4Click(self, sender, e):
        from Misc import *
        Misc = Misc(self)
        Misc.Show()
        self.Hide()

    def Button6Click(self, sender, e):
        self._label3.Text = str(self.price)