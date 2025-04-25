using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace AboutMe {
    public partial class Form1 : Form {
        public Form1() {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e) {
            label7.Text = "Taylor Cahill";
            label6.Text = "Robotics";
            label5.Text = "Yesterday is history," +
                " tomorrow is a mystery, but today is a gift. " +
                "That is why it is called the present.";
        }

        private void button2_Click(object sender, EventArgs e) {
            label7.Text = "";
            label6.Text = "";
            label5.Text = "";
        }
    }
}
