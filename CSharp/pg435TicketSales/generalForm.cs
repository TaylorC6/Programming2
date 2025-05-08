using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace pg435TicketSales {
    public partial class generalForm : Form {
        private Form myParent;
        public generalForm(Form myParent) { // Constructor / __init__
            InitializeComponent();
            this.myParent = myParent;
        }

        private void button1_Click(object sender, EventArgs e) {
            // this.Parent.Show();
            myParent.Show();
            this.Hide();
        }

        private void generalForm_FormClosing(object sender, FormClosingEventArgs e) {
            this.myParent.Show();
            this.Hide();
        }

        private void radioButton3_CheckedChanged(object sender, EventArgs e) {

        }

        private void radioButton2_CheckedChanged(object sender, EventArgs e) {

        }

        private void radioButton1_CheckedChanged(object sender, EventArgs e) {

        }

        private void label6_Click(object sender, EventArgs e) {

        }

        private void textBox4_TextChanged(object sender, EventArgs e) {

        }

        private void button2_Click(object sender, EventArgs e) {
            int price = 0;
            if (radioButton1.Checked) {
                price = 20;
            } else if (radioButton2.Checked) {
                price = 15;
            } else if (radioButton3.Checked) {
                price = 10;
            }
            int num = int.Parse(textBox4.Text);
            decimal ticket_cost = (decimal)num * price;
            decimal sales_tax = (decimal)num * 0.06m;
            decimal total = ticket_cost + sales_tax;
            label10.Text = ticket_cost.ToString("$.00");
            label8.Text = sales_tax.ToString("$.00");
            label9.Text = total.ToString("$.00");
        }
    }
}
