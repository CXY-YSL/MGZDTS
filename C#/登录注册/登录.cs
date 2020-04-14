using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Data.SqlClient;
using 登录;

namespace 登录注册
{
    public partial class 登录 : Form
    {
        public 登录()
        {
            InitializeComponent();
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {
            this.textBox2.PasswordChar = '*';
        }

        private void button1_Click(object sender, EventArgs e)
        {
            String userid, password;
            userid = textBox1.Text;
            password = textBox2.Text;
            String ConnstrWindows = @"Data Source=LAPTOP-6HF7DH62;Initial Catalog=Demo;Integrated Security=True";
            SqlConnection SqlCon = new SqlConnection(ConnstrWindows);
            SqlCon.Open(); //打开数据库
            String Sql = "select userid,password from [user] where userid='" + userid + "' and password='" + password + "'";
            SqlCommand sqlCommand = new SqlCommand(Sql, SqlCon);
            SqlDataReader sqlDataReader = sqlCommand.ExecuteReader();
            if (sqlDataReader.HasRows)
            {
                Form3 form3 = new Form3();
                form3.Show();
                this.Hide();
            }
            else
            {
                DialogResult dr = MessageBox.Show("是否注册新用户？", "登录失败", MessageBoxButtons.YesNo, MessageBoxIcon.Question);
                if (dr == DialogResult.Yes)
                {
                    注册 form2 = new 注册();
                    form2.Show();
                    this.Hide();
                }
                else
                {
                    this.Show();
                }
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            注册 form2 = new 注册();
            form2.Show();
            this.Hide();
        }

        private void panel1_Paint(object sender, PaintEventArgs e)
        {

        }

    }
}
