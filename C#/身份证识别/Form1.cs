using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace 身份证识别
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            try
            {
                string identityCard = textBox1.Text.Trim();
                if (string.IsNullOrEmpty(identityCard))
                {
                    MessageBox.Show("身份证号码不能为空！");
                    if (button1.CanFocus)
                    {
                        button1.Focus();
                    }
                    return;
                }
                else
                {
                    if (identityCard.Length != 15 && identityCard.Length != 18)
                    {
                        MessageBox.Show("身份证号码为15位或18位，请检查！");
                        if (button1.CanFocus)
                        {
                            button1.Focus();
                        }
                        return;
                    }
                }
                string birthday = "";
                string sex = "";
                if (identityCard.Length == 18)
                {
                    birthday = identityCard.Substring(6, 4) + "-" + identityCard.Substring(10, 2) + "-" + identityCard.Substring(12, 2);
                    sex = identityCard.Substring(14, 3);
                }
                if (identityCard.Length == 15)
                {
                    birthday = "19" + identityCard.Substring(6, 2) + "-" + identityCard.Substring(8, 2) + "-" + identityCard.Substring(10, 2);
                    sex = identityCard.Substring(12, 3);
                }
                textBox2.Text = birthday;
                if (int.Parse(sex) % 2 == 0)
                {
                    this.comboBox1.Text = "女";
                }
                else
                {
                    this.comboBox1.Text = "男";
                }
            }
            catch (Exception)
            {
                MessageBox.Show("身份证号码输入有误");
                if (textBox1.CanFocus)
                {
                    textBox1.Focus();
                }
                return;
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void label3_Click(object sender, EventArgs e)
        {

        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }
    }
}
