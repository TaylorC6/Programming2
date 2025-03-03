import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label4 = System.Windows.Forms.Label()
        self._button4 = System.Windows.Forms.Button()
        self._button5 = System.Windows.Forms.Button()
        self._button6 = System.Windows.Forms.Button()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.SystemColors.MenuHighlight
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(343, 15)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(168, 33)
        self._label4.TabIndex = 32
        self._label4.Text = "Sales"
        self._label4.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # button4
        # 
        self._button4.BackColor = System.Drawing.SystemColors.MenuHighlight
        self._button4.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button4.Location = System.Drawing.Point(343, 315)
        self._button4.Name = "button4"
        self._button4.Size = System.Drawing.Size(168, 70)
        self._button4.TabIndex = 31
        self._button4.Text = "Exit"
        self._button4.UseVisualStyleBackColor = False
        self._button4.Click += self.Button4Click
        # 
        # button5
        # 
        self._button5.BackColor = System.Drawing.SystemColors.MenuHighlight
        self._button5.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button5.Location = System.Drawing.Point(343, 186)
        self._button5.Name = "button5"
        self._button5.Size = System.Drawing.Size(168, 70)
        self._button5.TabIndex = 30
        self._button5.Text = "Student"
        self._button5.UseVisualStyleBackColor = False
        self._button5.Click += self.Button5Click
        # 
        # button6
        # 
        self._button6.BackColor = System.Drawing.SystemColors.MenuHighlight
        self._button6.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button6.Location = System.Drawing.Point(343, 62)
        self._button6.Name = "button6"
        self._button6.Size = System.Drawing.Size(168, 70)
        self._button6.TabIndex = 29
        self._button6.Text = "General"
        self._button6.UseVisualStyleBackColor = False
        self._button6.Click += self.Button6Click
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.SystemColors.MenuHighlight
        self._label5.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(15, 175)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(297, 93)
        self._label5.TabIndex = 28
        self._label5.Text = "Select Student Sales for all student ticket sales."
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.SystemColors.MenuHighlight
        self._label6.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(15, 52)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(297, 95)
        self._label6.TabIndex = 27
        self._label6.Text = "Select General Sales for all ticket sales to the general public."
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.MediumTurquoise
        self.ClientSize = System.Drawing.Size(527, 400)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._button4)
        self.Controls.Add(self._button5)
        self.Controls.Add(self._button6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label6)
        self.Name = "MainForm"
        self.Text = "Pg435TicketSalesPython"
        self.ResumeLayout(False)


    def Button6Click(self, sender, e):
        from Form1 import *
        form1 = Form1(self)
        form1.Show()
        self.Hide()

    def Button5Click(self, sender, e):
        from Form2 import *
        form2 = Form2(self)
        form2.Show()
        self.Hide()

    def Button4Click(self, sender, e):
        Application.Exit()