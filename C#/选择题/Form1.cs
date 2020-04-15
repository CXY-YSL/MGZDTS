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
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        string[] question = new string[3];
        string[,] choose = new string[3, 4];
        string[] answer = new string[3];
        int s = 0;

        private void Form1_Load(object sender, EventArgs e)
        {
            question[0] = "王者荣耀里李白是什么职业？";
            choose[0, 0] = "A.刺客";
            choose[0, 1] = "B.坦克";
            choose[0, 2] = "C.法师";
            choose[0, 3] = "D.射手";
            answer[0] = "A";
            question[1] = "王者荣耀里白起是什么职业？";
            choose[1, 0] = "A.刺客";
            choose[1, 1] = "B.坦克";
            choose[1, 2] = "C.法师";
            choose[1, 3] = "D.射手";
            answer[1] = "B";
            question[2] = "王者荣耀里后裔是什么职业？";
            choose[2, 0] = "A.刺客";
            choose[2, 1] = "B.坦克";
            choose[2, 2] = "C.法师";
            choose[2, 3] = "D.射手";
            answer[2] = "D";
            Show_question();
        }

        public void Show_question()
        {
            label1.Text = question[s];
            radioButton1.Text = choose[s, 0];
            radioButton2.Text = choose[s, 1];
            radioButton3.Text = choose[s, 2];
            radioButton4.Text = choose[s, 3];
        }

        private void label1_Click(object sender, EventArgs e)
            {

            }

        private void radioButton1_CheckedChanged(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            string c = "";
            if (radioButton1.Checked) { c = "A"; }
            if (radioButton2.Checked) { c = "B"; }
            if (radioButton3.Checked) { c = "C"; }
            if (radioButton4.Checked) { c = "D"; }
            if (answer[s] == c)
            {
                MessageBox.Show("恭喜你答对了");
            }
            else
            {
                MessageBox.Show("很遗憾你答错了");
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Form2 form2 = new Form2();
            form2.Show();
            this.Hide();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            s++;
            if (s < 3)
            {
                Show_question();
            }
            else
            {
                MessageBox.Show("你已经答完了所有题目！");
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
