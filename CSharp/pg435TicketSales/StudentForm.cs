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
    public partial class StudentForm : Form {
        private Form myParent;
        public StudentForm(Form myParent) {
            InitializeComponent();
            this.myParent = myParent;
        }

        private void button1_Click(object sender, EventArgs e) {
            myParent.Show();
            this.Close();
        }

        private void StudentForm_FormClosing(object sender, FormClosingEventArgs e) {
            this.Parent.Show();
        }

        private void label3_Click(object sender, EventArgs e) {

        }

        private void label4_Click(object sender, EventArgs e) {

        }

        private void label5_Click(object sender, EventArgs e) {

        }

        private void button2_Click(object sender, EventArgs e) {
            int num = int.Parse(textBox4.Text);
            decimal ticket_cost = (decimal)num * 7;
            decimal sales_tax = (decimal)num * 0.06m;
            decimal total = ticket_cost + sales_tax;
            label10.Text = ticket_cost.ToString();
            label8.Text = sales_tax.ToString();
            label9.Text = total.ToString();
        }
    }
}
