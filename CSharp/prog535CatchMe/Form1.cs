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
        public Form1() {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e) {

            string[] strCaption = { "Click Here", "Try Harder", "Too Slow", "Try Again", 
            "Not Even Close"};

            Random rand = new Random();

        }
    }
}
