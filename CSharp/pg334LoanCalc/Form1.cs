using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace pg334LoanCalc {
    public partial class Form1 : Form {

        int Count = 0;
        int Month = 0;
        double Loan = 0;
        double Payment = 0;
        double Interest = 0;
        double Principle = 0;

        public Form1() {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e) {
            
        }

        private void button2_Click(object sender, EventArgs e) {
            listBox1.Text = "";
            textBox1.Text = "";
            textBox2.Text = "";
            textBox3.Text = "";
            textBox4.Text = "";
            radioButton1.Checked = false;
            radioButton2.Checked = false;
        }

        private void button3_Click(object sender, EventArgs e) {
            Application.Exit();
        }
    }
}
