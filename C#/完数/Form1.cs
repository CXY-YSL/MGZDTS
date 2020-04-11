using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace 完数
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            textBox2.Text = "";
            for (int i = 2; i < 1000; i++)
            {
                int count = 0;
                for (int j = 1; j < i; j++)
                {
                    if (i % j == 0)
                    {
                        count += j;
                    }
                }
                if (count == i)
                {
                    textBox2.Text = textBox2.Text + i.ToString() + ",";
                }
            }
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
