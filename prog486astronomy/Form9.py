
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form9(Form):
    def __init__(self, parent):
        self.myparent = parent
        self.InitializeComponent()
    
    def InitializeComponent(self):
        resources = System.Resources.ResourceManager("prog486astronomy.Form9", System.Reflection.Assembly.GetEntryAssembly())
        self._pictureBox1 = System.Windows.Forms.PictureBox()
        self._button1 = System.Windows.Forms.Button()
        self._pictureBox1.BeginInit()
        self.SuspendLayout()
        # 
        # pictureBox1
        # 
        self._pictureBox1.Image = resources.GetObject("pictureBox1.Image")
        self._pictureBox1.Location = System.Drawing.Point(-4, 31)
        self._pictureBox1.Name = "pictureBox1"
        self._pictureBox1.Size = System.Drawing.Size(552, 470)
        self._pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom
        self._pictureBox1.TabIndex = 4
        self._pictureBox1.TabStop = False
        # 
        # button1
        # 
        self._button1.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.Color.White
        self._button1.Location = System.Drawing.Point(420, 473)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(111, 51)
        self._button1.TabIndex = 5
        self._button1.Text = "Exit"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # Form9
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaptionText
        self.ClientSize = System.Drawing.Size(543, 536)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._pictureBox1)
        self.Name = "Form9"
        self.Text = "Form9"
        self._pictureBox1.EndInit()
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self.myparent.Show()
        self.Hide()