using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace 判断素数
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            int zh = Convert.ToInt32(textBox1.Text);

            int t = (int)Math.Sqrt(zh);

            int i;

            for (i = 2; i <= t; i++)

            {

                if (zh % i == 0)

                {

                    break;

                }

            }

            if (i <= t)

            {

                label2.Text = zh + "不是素数";

            }

            else

            {

                label2.Text = zh + "是素数";

            }

            textBox1.Text = textBox1.Text;
        }

        private void label2_Click(object sender, EventArgs e)
        {

        }
    }
}
