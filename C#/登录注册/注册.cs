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

namespace 登录注册
{
    public partial class 注册 : Form
    {
        public 注册()
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

        private void textBox3_TextChanged(object sender, EventArgs e)
        {
            this.textBox3.PasswordChar = '*';
        }

        private void button2_Click(object sender, EventArgs e)
        {
                String userid, password, repassword;
                userid = textBox1.Text;
                password = textBox2.Text;
                repassword = textBox3.Text;
            if (password == repassword)
            {
                String ConnstrWindows = @"Data Source=LAPTOP-6HF7DH62;Initial Catalog=Demo;Integrated Security=True";
                SqlConnection SqlCon = new SqlConnection(ConnstrWindows);
                SqlCon.Open();
                String Sql = "INSERT INTO [user](userid,password) VALUES('" + userid + "','" + password + "')";
                    SqlCommand sqlCommand = new SqlCommand(Sql, SqlCon);
                    sqlCommand.ExecuteNonQuery();
                    MessageBox.Show("注册成功");
                }
                else
                {
                    MessageBox.Show("密码不一致");
                }
            }

        private void button1_Click(object sender, EventArgs e)
        {
            this.Close();
            登录 form = new 登录();
            form.Show();
        }

        private void panel1_Paint(object sender, PaintEventArgs e)
        {

        }
    }
}
