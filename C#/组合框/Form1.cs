using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace 组合框
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            insertComboItem();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            label1.Text = "所有的国家";
            label2.Text = "选中的国家";
            label3.Text = "添加或删除的国家";
            button1.Text = "添加国家";
            button2.Text = "删除国家";
            button3.Text = "退出";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            comboBox1.Items.Remove(textBox1.Text);
            MessageBox.Show("删除成功！");
        }

        private void button1_Click(object sender, EventArgs e)
        {
            comboBox1.Items.Add(textBox1.Text);
            MessageBox.Show("添加成功！");
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            ComboBox cb = sender as ComboBox;
            string itemText = cb.SelectedItem as string;
            if (!string.IsNullOrWhiteSpace(itemText) && richTextBox1 != null)
            {
                this.richTextBox1.Text = string.Format("{0}", itemText);
            }
        }
        private void insertComboItem()
        {
            comboBox1.Items.Add("中国");
            comboBox1.Items.Add("美国");
            comboBox1.Items.Add("英国"); 
            comboBox1.Items.Add("法国");
            comboBox1.Items.Add("俄罗斯");
            //默认选择第一项
            comboBox1.SelectedIndex = 0;
        }

        private void richTextBox1_TextChanged(object sender, EventArgs e)
        {

        }
    }
}
