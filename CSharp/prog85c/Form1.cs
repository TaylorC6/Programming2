﻿using System;
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
            label2.Text = "";
            int num1 = int.Parse(textBox2.Text);
            int month = ((num1 - 165) / 100);
            double day = ((num1 - 165) % 100);
            label2.Text = "Your birthday is " + month.ToString() + "/" + day.ToString();

        }

        private void Form1_Load(object sender, EventArgs e) {
            label3.Text = "1.Determine your birth month(January = 1, February = 2, March = 3, …)." +
                "\n2.Multiply that number by 5." +
                "\n3.Add 6 to that number." +
                "\n4.Multiply that number  by 4." +
                "\n5.Add 9 to the number." +
                "\n6.Multiply that number by 5." +
                "\n7.Add your birth day to the number.";
        }

        private void button2_Click(object sender, EventArgs e) {
            label2.Text = "";
            textBox2.Text = "";
        }
    }
}
