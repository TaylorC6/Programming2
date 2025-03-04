
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
        # Misc
        # 
        self.BackColor = System.Drawing.Color.Maroon
        self.ClientSize = System.Drawing.Size(586, 534)
        self.Controls.Add(self._button5)
        self.Controls.Add(self._label2)
        self.Name = "Misc"
        self.Text = "Misc"
        self.ResumeLayout(False)


    def Button5Click(self, sender, e):
        self.myparent.Show()
        self.Hide()