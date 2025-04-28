using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace prog85c {
    public partial class Form1 : Form {
        public Form1() {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e) {
            label3.Text = "1.Determine your birth month(January = 1, February = 2, March = 3, …)." +
                "2.Multiply that number by 5." +
                "6 to that number." +
                "4.Multiply that number  by 4." +
                "5.Add 9 to the number." +
                "6.Multiply that number by 5." +
                "7.Add your birth day to the number.";

        }
    }
}
