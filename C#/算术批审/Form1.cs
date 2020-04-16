using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace 算术批审
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        int correct = 0;
        int count = 0;
        
        private void Form1_Load(object sender, EventArgs e)
        {
            newWork();
            label4.Text = "=";
            button1.Text = "确定";
            button2.Text = "退出";
        }
        public void newWork()
        {
            Random rd = new Random();
            int i = rd.Next(1, 100);
            int j = rd.Next(1, 100);
            label1.Text = Convert.ToString(i);
            label3.Text = Convert.ToString(j);
            string[] fh = new string[] { "+", "-", "*", "/" };
            label2.Text = fh[rd.Next(0, 4)];
        }

        private void button1_Click(object sender, EventArgs e) 
        {
            int getresult = 0;
            int x = int.Parse(label1.Text);
            int y = int.Parse(label3.Text);
            switch (label2.Text)
            {
                case "+":
                    getresult = x + y;
                    break;
                case "-":
                    getresult = x - y;
                    break;
                case "*":
                    getresult = x * y;
                    break;
                case "/":
                    getresult = x / y;
                    break;
            }
            count ++;
            int result = int.Parse(textBox1.Text);
            if (getresult == result)
            {
                correct ++;
                richTextBox1.Text += label1.Text + label2.Text + label3.Text + label4.Text + textBox1.Text + "√";
                
            }
            else
            {
                richTextBox1.Text += label1.Text + label2.Text + label3.Text + label4.Text + textBox1.Text + "×"; 
            }

            newWork();

            label5.Text = "共答" + count.ToString() + "题，答对" + correct.ToString() + "题，正确率" + (correct / count * 100).ToString() + "%";

            textBox1.TextChanged += new EventHandler(TextBox_TextChanged);
        }
        
        public void TextBox_TextChanged(object sender, EventArgs e)
        {
            foreach(Control ctl in this.Controls)
            {
                if(ctl.Name == (sender as Control).Name)
                {
                    continue;
                }
                else
                {
                    if(ctl is TextBox)
                    {
                        (ctl as TextBox).Clear();
                    }
                }
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void richTextBox1_TextChanged(object sender, EventArgs e)
        {
            
        }

    }
}
