
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form7(Form):
    def __init__(self, parent):
        self.myparent = parent
        self.InitializeComponent()
    
    def InitializeComponent(self):
        resources = System.Resources.ResourceManager("prog486astronomy.Form7", System.Reflection.Assembly.GetEntryAssembly())
        self._pictureBox1 = System.Windows.Forms.PictureBox()
        self._button1 = System.Windows.Forms.Button()
        self._label5 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label1 = System.Windows.Forms.Label()
        self._pictureBox1.BeginInit()
        self.SuspendLayout()
        # 
        # pictureBox1
        # 
        self._pictureBox1.Image = resources.GetObject("pictureBox1.Image")
        self._pictureBox1.Location = System.Drawing.Point(-30, -120)
        self._pictureBox1.Name = "pictureBox1"
        self._pictureBox1.Size = System.Drawing.Size(597, 506)
        self._pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom
        self._pictureBox1.TabIndex = 4
        self._pictureBox1.TabStop = False
        # 
        # button1
        # 
        self._button1.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.Color.White
        self._button1.Location = System.Drawing.Point(420, 471)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(111, 51)
        self._button1.TabIndex = 5
        self._button1.Text = "Exit"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.PaleGoldenrod
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.ForeColor = System.Drawing.Color.Black
        self._label5.Location = System.Drawing.Point(12, 436)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(363, 29)
        self._label5.TabIndex = 39
        self._label5.Text = "Surface temperature –180°C"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.PaleGoldenrod
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.Color.Black
        self._label4.Location = System.Drawing.Point(12, 389)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(363, 29)
        self._label4.TabIndex = 38
        self._label4.Text = "Mass 5.69 × 10^26 kg"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.PaleGoldenrod
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.Color.Black
        self._label3.Location = System.Drawing.Point(12, 342)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(363, 29)
        self._label3.TabIndex = 37
        self._label3.Text = "Average distance from the sun 9.5388 AU"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.PaleGoldenrod
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.Color.Black
        self._label2.Location = System.Drawing.Point(12, 294)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(334, 224)
        self._label2.TabIndex = 36
        self._label2.Text = "Type Jovian"
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.PaleGoldenrod
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.Black
        self._label1.Location = System.Drawing.Point(12, 241)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(363, 277)
        self._label1.TabIndex = 35
        self._label1.Text = "Saturn"
        # 
        # Form7
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaptionText
        self.ClientSize = System.Drawing.Size(543, 534)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._pictureBox1)
        self.Name = "Form7"
        self.Text = "Form7"
        self._pictureBox1.EndInit()
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self.myparent.Show()
        self.Hide()