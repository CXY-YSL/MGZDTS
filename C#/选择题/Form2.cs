using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace 选择题
{
    public partial class Form2 : Form
    {
        int Num = 0;
        public Form2()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Check(groupBox1, "A");
            Check(groupBox2, "B");
            Check(groupBox3, "C");
            Check(groupBox4, "D");
            Check(groupBox5, "A");
            Check(groupBox6, "B");
            Check(groupBox7, "C");
            Check(groupBox8, "D");
            Check(groupBox9, "A");
            MessageBox.Show("你的等分是：" + (Num * 100).ToString() + "分");
            Num = 0;
        }

        private void Check(GroupBox gb,string zhengque)
        {
            foreach(Control D in gb.Controls)
            {
                if(((RadioButton)D).Checked == true && ((RadioButton)D).Text.Substring(0,1) == zhengque)
                {
                    Num++;
                }
            }
        }

        private void groupBox1_Enter(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Form1 form1 = new Form1();
            form1.Show();
            this.Hide();
        }
    }
}
