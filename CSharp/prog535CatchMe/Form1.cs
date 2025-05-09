using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace prog535CatchMe {
    public partial class Form1 : Form {

        string[] strCaption = { "Click Here", "Try Harder", "Too Slow", "Try Again",
            "Not Even Close", "I'm over here"};

        Random rand = new Random();

        public Form1() {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e) {

            MessageBox.Show("You Got Me!", "", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
            Application.Exit();
        }

        private void button1_MouseEnter(object sender, EventArgs e) {
            int intIndex = rand.Next(strCaption.Length);
            button1.Text = strCaption[intIndex];
            button1.Left = rand.Next(this.Width - button1.Width);
            button1.Top = rand.Next(this.Height - button1.Height);
        }
    }
}
