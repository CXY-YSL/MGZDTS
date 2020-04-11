using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace 多边形图
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void richTextBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            label1.Text = "三角形";
            for (int i = 1; i <= 10; i++)
            {
                for (int j = 1; j <= 12 - i; j++)
                    richTextBox1.Text += " ";
                for (int k = 0; k < 2 * i - 1; k++)
                    richTextBox1.Text += "*";
                richTextBox1.Text += Environment.NewLine;
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            label1.Text = "平行四边形";
            for (int i = 1; i <= 5; i++)
            {
                for (int j = 1; j <= 2 * i - 2; j++)
                    richTextBox1.Text += " ";
                for (int j = 1; j <= 1; j++)
                    richTextBox1.Text += " ";
                for (int j = 1; j <= 8; j++)
                    richTextBox1.Text += " *";
                richTextBox1.Text += Environment.NewLine;
            }
            richTextBox1.Text += Environment.NewLine;
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }
    }
}

