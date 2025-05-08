using Microsoft.VisualBasic;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace pg498Payroll {
    public partial class Form1 : Form {
        public Form1() {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e) {
            const int intMAX_EMPLOYEES = 5;
            const decimal decHOURLY_PAY_RATE = 6.0m;
            // Calc and display gross Pay Earned by Employees
            int[] Hours = new int[intMAX_EMPLOYEES];  // An array   [0,0,0,0,0]
            // <type>[] varName = new <type>[capacity];
            int Count = 0;
            int EmpHours = 0;
            decimal EmpPay = 0.0m;

            for (Count = 0; Count < intMAX_EMPLOYEES; Count++) {
                while (int.TryParse(Interaction.InputBox("Enter # of Hours Worked by Employee #" + (Count + 1).ToString(), "Need Hours Worked"), out EmpHours) == false) {
                    MessageBox.Show("Please Enter an Integer for Hours Worked");
                }
                Hours[Count] = EmpHours;
            }
            listBox1.Items.Clear();
            for (Count = 0; Count < intMAX_EMPLOYEES; Count++) {
                EmpPay = Hours[Count] * decHOURLY_PAY_RATE;
                listBox1.Items.Add("Employee " + (Count + 1).ToString() +
                " Earned " + EmpPay.ToString("$.00"));
            }
        }
        private void button2_Click(object sender, EventArgs e) {
            Application.Exit();
        }
    }
}